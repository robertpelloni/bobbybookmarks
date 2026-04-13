package api

import (
	"bobbybookmarks/internal/database"
	"bobbybookmarks/internal/models"
	"github.com/gofiber/fiber/v2"
	"strconv"
)

func RegisterRoutes(app *fiber.App) {
	api := app.Group("/api")

	api.Get("/stats", getStats)
	api.Get("/bookmarks", getBookmarks)
	api.Post("/import", importBookmarks)
	api.Get("/research/status", getResearchStatus)
	api.Post("/categories/refresh", refreshCategories)
	api.Post("/bookmarks/deduplicate", deduplicateBookmarks)
	api.Post("/research/start", startWorker)
	api.Post("/research/stop", stopWorker)
}

func getStats(c *fiber.Ctx) error {
	var total, unique, clusters, duplicates, pending, running, done, failed int
	database.DB.Get(&total, "SELECT COUNT(*) FROM bookmarks")
	database.DB.Get(&unique, "SELECT COUNT(*) FROM bookmarks WHERE is_duplicate = 0")
	database.DB.Get(&clusters, "SELECT COUNT(*) FROM clusters")
	database.DB.Get(&duplicates, "SELECT COUNT(*) FROM bookmarks WHERE is_duplicate = 1")
	database.DB.Get(&pending, "SELECT COUNT(*) FROM bookmarks WHERE research_status = 'pending'")
	database.DB.Get(&running, "SELECT COUNT(*) FROM bookmarks WHERE research_status = 'running'")
	database.DB.Get(&done, "SELECT COUNT(*) FROM bookmarks WHERE research_status = 'done'")
	database.DB.Get(&failed, "SELECT COUNT(*) FROM bookmarks WHERE research_status = 'failed'")

	return c.JSON(fiber.Map{
		"total":      total,
		"unique":     unique,
		"clusters":   clusters,
		"duplicates": duplicates,
		"research": fiber.Map{
			"pending": pending,
			"running": running,
			"done":    done,
			"failed":  failed,
		},
	})
}

func getBookmarks(c *fiber.Ctx) error {
	q := c.Query("q", "")
	page, _ := strconv.Atoi(c.Query("page", "1"))
	perPage, _ := strconv.Atoi(c.Query("per_page", "50"))
	offset := (page - 1) * perPage

	var bookmarks []models.Bookmark
	query := "SELECT * FROM bookmarks WHERE 1=1"
	args := []interface{}{}

	if q != "" {
		query += " AND (url LIKE ? OR page_title LIKE ? OR page_description LIKE ?)"
		args = append(args, "%"+q+"%", "%"+q+"%", "%"+q+"%")
	}

	query += " ORDER BY id DESC LIMIT ? OFFSET ?"
	args = append(args, perPage, offset)

	err := database.DB.Select(&bookmarks, query, args...)
	if err != nil {
		return c.Status(500).JSON(fiber.Map{"error": err.Error()})
	}

	var total int
	database.DB.Get(&total, "SELECT COUNT(*) FROM bookmarks")

	return c.JSON(fiber.Map{
		"bookmarks": bookmarks,
		"total":     total,
		"page":      page,
		"pages":     (total + perPage - 1) / perPage,
	})
}

func getResearchStatus(c *fiber.Ctx) error {
	var pending, running, done, failed int
	database.DB.Get(&pending, "SELECT COUNT(*) FROM bookmarks WHERE research_status = 'pending'")
	database.DB.Get(&running, "SELECT COUNT(*) FROM bookmarks WHERE research_status = 'running'")
	database.DB.Get(&done, "SELECT COUNT(*) FROM bookmarks WHERE research_status = 'done'")
	database.DB.Get(&failed, "SELECT COUNT(*) FROM bookmarks WHERE research_status = 'failed'")

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
