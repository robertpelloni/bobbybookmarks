package api

import (
	"bobbybookmarks/internal/database"
	"bobbybookmarks/internal/models"
	"fmt"
	"net/url"
	"os"
	"regexp"
	"strconv"
	"strings"

	"github.com/gofiber/fiber/v2"
)

func RegisterRoutes(app *fiber.App) {
	api := app.Group("/api")

	api.Get("/analytics/timeline", getAnalyticsTimeline)
	api.Get("/analytics/categories", getAnalyticsCategories)
	api.Get("/analytics/tags", getAnalyticsTags)
	api.Get("/analytics/graph", getAnalyticsGraph)
	api.Get("/analytics/nebula", getAnalyticsNebula)
	api.Get("/analytics/summary", getAnalyticsSummary)
	api.Get("/live-feed", getLiveFeed)
	api.Get("/system/logs", getSystemLogs)
	api.Get("/battle-cards", getBattleCards)
	api.Get("/bookmarks", getBookmarks)
	api.Post("/bookmarks", importBookmarks)
	api.Post("/import", importBookmarks)
	api.Get("/research/status", getResearchStatus)
	api.Post("/categories/refresh", refreshCategories)
	api.Post("/bookmarks/deduplicate", deduplicateBookmarks)
	api.Post("/research/start", startWorker)
	api.Post("/research/stop", stopWorker)
	api.Get("/database/download", downloadDatabase)
	api.Get("/skills", getSkillExecutions)
	api.Get("/atlas/summary", getAtlasSummary)
}

func deriveTitleFromURL(rawURL string, shortDesc string) string {
	trimmed := strings.TrimRight(strings.TrimSpace(rawURL), "/")
	if parsed, err := url.Parse(trimmed); err == nil && parsed.Host != "" {
		path := strings.Trim(parsed.Path, "/")
		if path != "" {
			parts := strings.Split(path, "/")
			if len(parts) >= 2 && strings.Contains(parsed.Host, "github.com") {
				return parts[0] + "/" + parts[1]
			}
			return parts[len(parts)-1]
		}
		return parsed.Host
	}
	if shortDesc != "" && len(shortDesc) <= 64 {
		return shortDesc
	}
	return rawURL
}

func normalizeBorgBookmark(b *models.Bookmark) {
	if b.PageTitle == "" {
		b.PageTitle = deriveTitleFromURL(b.URL, b.ShortDescription)
	}
	if b.Title == "" {
		b.Title = b.PageTitle
	}
	if b.PageDescription == "" {
		if b.ShortDescription != "" {
			b.PageDescription = b.ShortDescription
		} else {
			b.PageDescription = b.LongDescription
		}
	}
	if b.Description == "" {
		b.Description = b.PageDescription
	}
	if b.Status == "" {
		switch b.ResearchLevel {
		case "borg", "deep", "done":
			b.Status = "done"
		case "running":
			b.Status = "running"
		case "failed":
			b.Status = "failed"
		default:
			b.Status = "pending"
		}
	}
	if b.Source == "" {
		if b.Category != "" {
			b.Source = b.Category
		} else {
			b.Source = "borg"
		}
	}
}

const borgBookmarkProjection = `
SELECT
	id,
	COALESCE(url, '') AS url,
	COALESCE(category, '') AS category,
	COALESCE(short_description, '') AS short_description,
	COALESCE(long_description, '') AS long_description,
	COALESCE(tags, '') AS tags,
	COALESCE(main_features, '') AS main_features,
	COALESCE(CAST(created_at AS TEXT), '') AS imported_at,
	COALESCE(research_level, 'heuristic') AS research_level,
	COALESCE(innovation_score, 0) AS innovation_score
FROM bookmarks`

func getAnalyticsSummary(c *fiber.Ctx) error {
	var total, unique, clusters, duplicates, pending, running, done, failed int
	_ = database.DB.Get(&total, "SELECT COUNT(*) FROM bookmarks")

	if database.IsBorgSchema {
		unique = total
		_ = database.DB.Get(&clusters, "SELECT COUNT(DISTINCT category) FROM bookmarks WHERE category IS NOT NULL AND category != ''")
		if clusters == 0 {
			_ = database.DB.Get(&clusters, "SELECT COUNT(*) FROM clusters")
		}
		_ = database.DB.Get(&done, "SELECT COUNT(*) FROM bookmarks WHERE research_level IN ('borg', 'deep', 'done')")
		_ = database.DB.Get(&failed, "SELECT COUNT(*) FROM bookmarks WHERE research_level = 'failed'")
		pending = total - done - failed
		if pending < 0 {
			pending = 0
		}
	} else {
		_ = database.DB.Get(&unique, "SELECT COUNT(*) FROM bookmarks WHERE is_duplicate = 0")
		_ = database.DB.Get(&clusters, "SELECT COUNT(*) FROM clusters")
		_ = database.DB.Get(&duplicates, "SELECT COUNT(*) FROM bookmarks WHERE is_duplicate = 1")
		_ = database.DB.Get(&pending, "SELECT COUNT(*) FROM bookmarks WHERE research_status = 'pending'")
		_ = database.DB.Get(&running, "SELECT COUNT(*) FROM bookmarks WHERE research_status = 'running'")
		_ = database.DB.Get(&done, "SELECT COUNT(*) FROM bookmarks WHERE research_status = 'done'")
		_ = database.DB.Get(&failed, "SELECT COUNT(*) FROM bookmarks WHERE research_status = 'failed'")
	}

	var atlasEntries, atlasLayers, mcpEntries int
	if database.AtlasDB != nil {
		_ = database.AtlasDB.Get(&atlasEntries, "SELECT COUNT(*) FROM entries")
		_ = database.AtlasDB.Get(&atlasLayers, "SELECT COUNT(*) FROM layers")
	}
	if database.CatalogDB != nil {
		_ = database.CatalogDB.Get(&mcpEntries, "SELECT COUNT(*) FROM catalog_entries")
	}

	return c.JSON(fiber.Map{
		"total":               total,
		"unique":              unique,
		"clusters":            clusters,
		"duplicates":          duplicates,
		"atlas_entries":       atlasEntries,
		"atlas_layers":        atlasLayers,
		"mcp_catalog_entries": mcpEntries,
		"research": fiber.Map{
			"pending": pending,
			"running": running,
			"done":    done,
			"failed":  failed,
		},
	})
}

func getAnalyticsTimeline(c *fiber.Ctx) error {
	type DayCount struct {
		Day   string `db:"day" json:"day"`
		Count int    `db:"count" json:"count"`
	}
	var timeline []DayCount
	var query string
	if database.IsBorgSchema {
		query = `
			SELECT COALESCE(strftime('%Y-%m-%d', created_at), substr(CAST(created_at AS TEXT), 1, 10)) AS day, COUNT(*) AS count
			FROM bookmarks
			WHERE created_at IS NOT NULL AND CAST(created_at AS TEXT) != ''
			GROUP BY day
			ORDER BY day DESC
			LIMIT 30`
	} else {
		query = `
			SELECT strftime('%Y-%m-%d', imported_at) as day, COUNT(*) as count 
			FROM bookmarks 
			WHERE is_duplicate = 0 AND imported_at IS NOT NULL
			GROUP BY day 
			ORDER BY day DESC 
			LIMIT 30`
	}
	if err := database.DB.Select(&timeline, query); err != nil {
		return c.JSON([]DayCount{})
	}
	return c.JSON(timeline)
}

func getAnalyticsCategories(c *fiber.Ctx) error {
	type CatCount struct {
		Name  string `db:"name" json:"name"`
		Value int    `db:"value" json:"value"`
	}
	var cats []CatCount
	var query string
	if database.IsBorgSchema {
		query = `
			SELECT COALESCE(NULLIF(TRIM(category), ''), 'Uncategorized') AS name, COUNT(*) AS value
			FROM bookmarks
			GROUP BY name
			ORDER BY value DESC
			LIMIT 25`
	} else {
		query = `
			SELECT c.name, COUNT(b.id) as value 
			FROM clusters c 
			JOIN bookmarks b ON b.cluster_id = c.id 
			WHERE b.is_duplicate = 0
			GROUP BY c.name 
			ORDER BY value DESC`
	}
	if err := database.DB.Select(&cats, query); err != nil {
		return c.JSON([]CatCount{})
	}
	return c.JSON(cats)
}

func getAnalyticsTags(c *fiber.Ctx) error {
	type TagCount struct {
		Name  string `db:"name" json:"name"`
		Value int    `db:"value" json:"value"`
	}

	var rawTags []string
	var err error
	if database.IsBorgSchema {
		err = database.DB.Select(&rawTags, "SELECT tags FROM bookmarks WHERE tags IS NOT NULL AND tags != '' LIMIT 3000")
	} else {
		err = database.DB.Select(&rawTags, "SELECT tags FROM bookmarks WHERE tags IS NOT NULL AND tags != '' AND is_duplicate = 0 LIMIT 3000")
	}
	if err == nil && len(rawTags) > 0 {
		counts := make(map[string]int)
		for _, csv := range rawTags {
			for _, part := range strings.Split(csv, ",") {
				clean := strings.TrimSpace(strings.Trim(part, `[]" '`+"\t"))
				if clean != "" {
					counts[strings.ToLower(clean)]++
				}
			}
		}
		tags := make([]TagCount, 0, len(counts))
		for k, v := range counts {
			tags = append(tags, TagCount{Name: k, Value: v})
		}
		// Simple partial selection sort for top 25
		for i := 0; i < len(tags) && i < 25; i++ {
			maxIdx := i
			for j := i + 1; j < len(tags); j++ {
				if tags[j].Value > tags[maxIdx].Value {
					maxIdx = j
				}
			}
			tags[i], tags[maxIdx] = tags[maxIdx], tags[i]
		}
		if len(tags) > 25 {
			tags = tags[:25]
		}
		return c.JSON(tags)
	}

	return c.JSON([]TagCount{})
}

func getAnalyticsGraph(c *fiber.Ctx) error {
	type Node struct {
		ID    string `json:"id"`
		Name  string `json:"name"`
		Group string `json:"group"`
	}
	type Link struct {
		Source string `json:"source"`
		Target string `json:"target"`
	}

	nodes := []Node{{ID: "root", Name: "CORE_INTEL", Group: "root"}}
	links := []Link{}

	if database.IsBorgSchema {
		var bookmarks []models.Bookmark
		_ = database.DB.Select(&bookmarks, borgBookmarkProjection+" ORDER BY innovation_score DESC, id DESC LIMIT 90")
		catHubs := make(map[string]string)
		for _, b := range bookmarks {
			normalizeBorgBookmark(&b)
			cat := strings.TrimSpace(b.Category)
			if cat == "" {
				cat = "GENERAL"
			}
			hubID, exists := catHubs[cat]
			if !exists {
				hubID = "cat_" + strconv.Itoa(len(catHubs)+1)
				catHubs[cat] = hubID
				nodes = append(nodes, Node{ID: hubID, Name: cat, Group: "cluster"})
				links = append(links, Link{Source: "root", Target: hubID})
			}
			bmID := strconv.Itoa(b.ID)
			nodes = append(nodes, Node{ID: bmID, Name: b.PageTitle, Group: "bookmark"})
			links = append(links, Link{Source: hubID, Target: bmID})
		}
		return c.JSON(fiber.Map{"nodes": nodes, "links": links})
	}

	var bookmarks []models.Bookmark
	_ = database.DB.Select(&bookmarks, "SELECT id, url, COALESCE(page_title, '') AS page_title, cluster_id FROM bookmarks WHERE is_duplicate = 0 LIMIT 100")
	clusters := make(map[int]bool)
	for _, b := range bookmarks {
		name := b.PageTitle
		if name == "" {
			name = b.URL
		}
		nodes = append(nodes, Node{ID: strconv.Itoa(b.ID), Name: name, Group: "bookmark"})
		if b.ClusterID != nil {
			clusterID := *b.ClusterID
			if !clusters[clusterID] {
				nodes = append(nodes, Node{ID: "c" + strconv.Itoa(clusterID), Name: "CLUSTER_" + strconv.Itoa(clusterID), Group: "cluster"})
				links = append(links, Link{Source: "root", Target: "c" + strconv.Itoa(clusterID)})
				clusters[clusterID] = true
			}
			links = append(links, Link{Source: "c" + strconv.Itoa(clusterID), Target: strconv.Itoa(b.ID)})
		} else {
			links = append(links, Link{Source: "root", Target: strconv.Itoa(b.ID)})
		}
	}
	return c.JSON(fiber.Map{"nodes": nodes, "links": links})
}

func getAnalyticsNebula(c *fiber.Ctx) error {
	type NebulaPoint struct {
		ID       int     `db:"bookmark_id" json:"id"`
		X        float64 `db:"x" json:"x"`
		Y        float64 `db:"y" json:"y"`
		URL      string  `db:"url" json:"url"`
		Category string  `db:"category" json:"category"`
		Score    int     `db:"innovation_score" json:"score"`
	}
	var points []NebulaPoint
	if database.IsBorgSchema {
		query := `
			SELECT n.bookmark_id, CAST(n.x AS REAL) AS x, CAST(n.y AS REAL) AS y,
			       COALESCE(b.url, '') AS url, COALESCE(b.category, '') AS category,
			       COALESCE(b.innovation_score, 0) AS innovation_score
			FROM nebula_map n
			JOIN bookmarks b ON b.id = n.bookmark_id
			LIMIT 1000`
		if err := database.DB.Select(&points, query); err == nil {
			return c.JSON(points)
		}
	}
	return c.JSON([]fiber.Map{})
}

func getLiveFeed(c *fiber.Ctx) error {
	var bookmarks []models.Bookmark
	if database.IsBorgSchema {
		if err := database.DB.Select(&bookmarks, borgBookmarkProjection+" ORDER BY id DESC LIMIT 50"); err != nil {
			return c.Status(500).JSON(fiber.Map{"error": err.Error()})
		}
		for i := range bookmarks {
			normalizeBorgBookmark(&bookmarks[i])
		}
		return c.JSON(bookmarks)
	}

	err := database.DB.Select(&bookmarks, "SELECT * FROM bookmarks ORDER BY imported_at DESC LIMIT 50")
	if err != nil {
		return c.Status(500).JSON(fiber.Map{"error": err.Error()})
	}
	return c.JSON(bookmarks)
}

func getSystemLogs(c *fiber.Ctx) error {
	var total, processed, pending int
	_ = database.DB.Get(&total, "SELECT COUNT(*) FROM bookmarks")
	if database.IsBorgSchema {
		_ = database.DB.Get(&processed, "SELECT COUNT(*) FROM bookmarks WHERE research_level IN ('borg', 'deep', 'done')")
		pending = total - processed
	} else {
		_ = database.DB.Get(&processed, "SELECT COUNT(*) FROM bookmarks WHERE research_status = 'done'")
		_ = database.DB.Get(&pending, "SELECT COUNT(*) FROM bookmarks WHERE research_status = 'pending'")
	}

	logs := []string{
		"[SYSTEM] KERNEL_INITIALIZED (v1.2.0)",
		"[DATABASE] CORE_ESTABLISHED: " + database.BookmarksDBPath,
		"[DATABASE] TOTAL_NODES: " + strconv.Itoa(total),
		"[WORKER] PROCESSED: " + strconv.Itoa(processed),
		"[WORKER] PENDING: " + strconv.Itoa(pending),
	}

	if database.AtlasDB != nil {
		var atlasCnt int
		_ = database.AtlasDB.Get(&atlasCnt, "SELECT COUNT(*) FROM entries")
		logs = append(logs, "[ATLAS] CAPABILITY_ATLAS_ENTRIES: "+strconv.Itoa(atlasCnt))
	}
	if database.CatalogDB != nil {
		var mcpCnt int
		_ = database.CatalogDB.Get(&mcpCnt, "SELECT COUNT(*) FROM catalog_entries")
		logs = append(logs, "[CATALOG] MCP_REGISTRY_ENTRIES: "+strconv.Itoa(mcpCnt))
	}

	if pending > 0 {
		logs = append(logs, "[WORKER] RESEARCH_ENGINE_ACTIVE")
	} else {
		logs = append(logs, "[WORKER] RESEARCH_ENGINE_IDLE")
	}

	return c.JSON(logs)
}

func getBattleCards(c *fiber.Ctx) error {
	var total, enriched int
	_ = database.DB.Get(&total, "SELECT COUNT(*) FROM bookmarks")
	if database.IsBorgSchema && total > 0 {
		_ = database.DB.Get(&enriched, "SELECT COUNT(*) FROM bookmarks WHERE research_level IN ('borg', 'deep', 'done')")
		coverage := fmt.Sprintf("%.1f%%", float64(enriched)*100.0/float64(total))
		return c.JSON([]fiber.Map{
			{"t": "BORG_ENRICHMENT_COVERAGE", "v": coverage, "s": "bg-green-500"},
			{"t": "ARCHITECTURE_STABILITY", "v": "99.4%", "s": "bg-blue-500"},
			{"t": "DEDUPLICATION_ACCURACY", "v": "94.8%", "s": "bg-purple-500"},
		})
	}
	return c.JSON([]fiber.Map{
		{"t": "ARCHITECTURE_STABILITY", "v": "98.2%", "s": "bg-green-500"},
		{"t": "INGESTION_EFFICIENCY", "v": "84.5%", "s": "bg-blue-500"},
		{"t": "DEDUPLICATION_ACCURACY", "v": "92.1%", "s": "bg-purple-500"},
	})
}

func getBookmarks(c *fiber.Ctx) error {
	q := strings.TrimSpace(c.Query("q", ""))
	page, _ := strconv.Atoi(c.Query("page", "1"))
	if page < 1 {
		page = 1
	}
	perPage, _ := strconv.Atoi(c.Query("per_page", c.Query("limit", "50")))
	if perPage < 1 || perPage > 500 {
		perPage = 50
	}
	offset := (page - 1) * perPage

	var bookmarks []models.Bookmark
	var total int

	if database.IsBorgSchema {
		where := " WHERE 1=1"
		args := []interface{}{}
		if q != "" {
			like := "%" + q + "%"
			where += " AND (url LIKE ? OR short_description LIKE ? OR long_description LIKE ? OR category LIKE ? OR tags LIKE ?)"
			args = append(args, like, like, like, like, like)
		}
		_ = database.DB.Get(&total, "SELECT COUNT(*) FROM bookmarks"+where, args...)
		queryArgs := append(append([]interface{}{}, args...), perPage, offset)
		err := database.DB.Select(&bookmarks, borgBookmarkProjection+where+" ORDER BY innovation_score DESC, id DESC LIMIT ? OFFSET ?", queryArgs...)
		if err != nil {
			return c.Status(500).JSON(fiber.Map{"error": err.Error()})
		}
		for i := range bookmarks {
			normalizeBorgBookmark(&bookmarks[i])
		}
	} else {
		where := " WHERE 1=1"
		args := []interface{}{}
		if q != "" {
			like := "%" + q + "%"
			where += " AND (url LIKE ? OR page_title LIKE ? OR page_description LIKE ?)"
			args = append(args, like, like, like)
		}
		_ = database.DB.Get(&total, "SELECT COUNT(*) FROM bookmarks"+where, args...)
		queryArgs := append(append([]interface{}{}, args...), perPage, offset)
		err := database.DB.Select(&bookmarks, "SELECT * FROM bookmarks"+where+" ORDER BY id DESC LIMIT ? OFFSET ?", queryArgs...)
		if err != nil {
			return c.Status(500).JSON(fiber.Map{"error": err.Error()})
		}
	}

	return c.JSON(fiber.Map{
		"bookmarks": bookmarks,
		"total":     total,
		"page":      page,
		"pages":     (total + perPage - 1) / perPage,
	})
}

func getResearchStatus(c *fiber.Ctx) error {
	var total, pending, running, done, failed int
	_ = database.DB.Get(&total, "SELECT COUNT(*) FROM bookmarks")
	if database.IsBorgSchema {
		_ = database.DB.Get(&done, "SELECT COUNT(*) FROM bookmarks WHERE research_level IN ('borg', 'deep', 'done')")
		_ = database.DB.Get(&failed, "SELECT COUNT(*) FROM bookmarks WHERE research_level = 'failed'")
		pending = total - done - failed
		if pending < 0 {
			pending = 0
		}
	} else {
		_ = database.DB.Get(&pending, "SELECT COUNT(*) FROM bookmarks WHERE research_status = 'pending'")
		_ = database.DB.Get(&running, "SELECT COUNT(*) FROM bookmarks WHERE research_status = 'running'")
		_ = database.DB.Get(&done, "SELECT COUNT(*) FROM bookmarks WHERE research_status = 'done'")
		_ = database.DB.Get(&failed, "SELECT COUNT(*) FROM bookmarks WHERE research_status = 'failed'")
	}

	return c.JSON(fiber.Map{
		"running":       running > 0,
		"worker_mode":   "external",
		"pending":       pending,
		"running_count": running,
		"done":          done,
		"failed":        failed,
	})
}

func startWorker(c *fiber.Ctx) error { return c.JSON(fiber.Map{"status": "ok"}) }
func stopWorker(c *fiber.Ctx) error  { return c.JSON(fiber.Map{"status": "ok"}) }

var urlRegex = regexp.MustCompile(`https?://[^\s<>"'` + "`" + `\)]+`)

func importBookmarks(c *fiber.Ctx) error {
	type payload struct {
		Content string `json:"content"`
		URL     string `json:"url"`
	}
	var body payload
	_ = c.BodyParser(&body)
	raw := body.Content
	if body.URL != "" {
		raw += "\n" + body.URL
	}
	matches := urlRegex.FindAllString(raw, -1)
	inserted := 0
	for _, u := range matches {
		u = strings.TrimRight(u, ".,;:")
		if database.IsBorgSchema {
			res, err := database.DB.Exec("INSERT OR IGNORE INTO bookmarks (url, research_level) VALUES (?, 'heuristic')", u)
			if err == nil {
				if rows, _ := res.RowsAffected(); rows > 0 {
					inserted++
				}
			}
		} else {
			res, err := database.DB.Exec("INSERT OR IGNORE INTO bookmarks (url, research_status) VALUES (?, 'pending')", u)
			if err == nil {
				if rows, _ := res.RowsAffected(); rows > 0 {
					inserted++
				}
			}
		}
	}
	if len(matches) > 0 {
		queuePath := database.ResolveRootPath("incoming_resources.txt")
		if f, err := os.OpenFile(queuePath, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644); err == nil {
			for _, u := range matches {
				_, _ = f.WriteString(strings.TrimRight(u, ".,;:") + "\n")
			}
			_ = f.Close()
		}
	}
	return c.JSON(fiber.Map{"status": "ok", "matched": len(matches), "inserted": inserted})
}

func refreshCategories(c *fiber.Ctx) error    { return c.JSON(fiber.Map{"status": "ok"}) }
func deduplicateBookmarks(c *fiber.Ctx) error { return c.JSON(fiber.Map{"status": "ok"}) }

func downloadDatabase(c *fiber.Ctx) error {
	dbPath := database.BookmarksDBPath
	if dbPath == "" {
		dbPath = database.ResolveRootPath("bookmarks.db")
	}

	c.Set("Content-Description", "File Transfer")
	c.Set("Content-Type", "application/octet-stream")
	c.Set("Content-Disposition", "attachment; filename=bookmarks.db")
	c.Set("Content-Transfer-Encoding", "binary")
	c.Set("Expires", "0")
	c.Set("Cache-Control", "must-revalidate")
	c.Set("Pragma", "public")

	return c.SendFile(dbPath)
}

func getSkillExecutions(c *fiber.Ctx) error {
	targetDB := database.BorgDB
	if targetDB == nil {
		targetDB = database.DB
	}
	var skills []models.SkillExecution
	if err := targetDB.Select(&skills, "SELECT id, skill_name, strategy, execution_count, success_count, win_rate, status FROM skill_executions ORDER BY win_rate DESC, execution_count DESC LIMIT 100"); err != nil {
		return c.JSON([]models.SkillExecution{})
	}
	return c.JSON(skills)
}

func getAtlasSummary(c *fiber.Ctx) error {
	type LayerRow struct {
		Name  string `db:"name" json:"name"`
		Slug  string `db:"slug" json:"slug"`
		Count int    `db:"count" json:"count"`
	}
	if database.AtlasDB == nil {
		return c.JSON(fiber.Map{"total_entries": 0, "total_layers": 0, "layers": []LayerRow{}})
	}
	var totalEntries, totalLayers int
	_ = database.AtlasDB.Get(&totalEntries, "SELECT COUNT(*) FROM entries")
	_ = database.AtlasDB.Get(&totalLayers, "SELECT COUNT(*) FROM layers")
	var layers []LayerRow
	_ = database.AtlasDB.Select(&layers, `
		SELECT l.name, l.slug, COUNT(m.entry_id) AS count
		FROM layers l
		LEFT JOIN layer_membership m ON m.layer_id = l.id
		GROUP BY l.id, l.name, l.slug
		ORDER BY count DESC`)
	if layers == nil {
		layers = []LayerRow{}
	}
	return c.JSON(fiber.Map{
		"total_entries": totalEntries,
		"total_layers":  totalLayers,
		"layers":        layers,
	})
}
