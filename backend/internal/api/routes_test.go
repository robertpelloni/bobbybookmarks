package api

import (
	"bobbybookmarks/internal/database"
	"encoding/json"
	"net/http/httptest"
	"testing"

	"github.com/gofiber/fiber/v2"
	"github.com/jmoiron/sqlx"
	_ "modernc.org/sqlite"
)

func TestBorgSchemaEndpointsAndSkillEngine(t *testing.T) {
	db, err := sqlx.Connect("sqlite", ":memory:")
	if err != nil {
		t.Fatalf("failed opening in-memory sqlite: %v", err)
	}
	defer db.Close()

	database.DB = db
	database.BorgDB = db
	database.AtlasDB = nil
	database.CatalogDB = nil

	database.EnsureSchema()
	if !database.IsBorgSchema {
		t.Fatalf("expected IsBorgSchema=true after EnsureSchema on fresh DB")
	}
	if err := database.InitSkillEngine(db.DB); err != nil {
		t.Fatalf("InitSkillEngine failed: %v", err)
	}

	_, err = db.Exec(`
		INSERT INTO bookmarks (url, category, short_description, tags, research_level, innovation_score)
		VALUES ('https://github.com/example/agent-tool', 'AI Agents', 'Autonomous test harness', 'agents,mcp,go', 'borg', 92)
	`)
	if err != nil {
		t.Fatalf("insert bookmark failed: %v", err)
	}

	_, err = db.Exec(`
		INSERT INTO skill_executions (skill_name, strategy, execution_count, success_count, win_rate, status)
		VALUES ('github_repo', 'ast_readme_extract', 10, 9, 0.9, 'active')
	`)
	if err != nil {
		t.Fatalf("insert skill_execution failed: %v", err)
	}

	app := fiber.New()
	RegisterRoutes(app)

	for _, path := range []string{
		"/api/analytics/summary",
		"/api/analytics/categories",
		"/api/analytics/tags",
		"/api/analytics/graph",
		"/api/bookmarks?q=agent",
		"/api/live-feed",
		"/api/skills",
	} {
		req := httptest.NewRequest("GET", path, nil)
		resp, err := app.Test(req, -1)
		if err != nil {
			t.Fatalf("GET %s error: %v", path, err)
		}
		if resp.StatusCode != 200 {
			t.Fatalf("GET %s expected 200, got %d", path, resp.StatusCode)
		}
	}

	req := httptest.NewRequest("GET", "/api/analytics/summary", nil)
	resp, _ := app.Test(req, -1)
	var summary map[string]interface{}
	if err := json.NewDecoder(resp.Body).Decode(&summary); err != nil {
		t.Fatalf("decode summary failed: %v", err)
	}
	if int(summary["total"].(float64)) != 1 {
		t.Fatalf("expected total=1, got %v", summary["total"])
	}
}

func TestLiveRealDatabasesIntegration(t *testing.T) {
	database.InitDB()
	database.EnsureSchema()

	app := fiber.New()
	RegisterRoutes(app)

	for _, path := range []string{
		"/api/analytics/summary",
		"/api/analytics/timeline",
		"/api/analytics/categories",
		"/api/analytics/tags",
		"/api/analytics/graph",
		"/api/analytics/nebula",
		"/api/live-feed",
		"/api/system/logs",
		"/api/battle-cards",
		"/api/bookmarks?limit=5&q=mcp",
		"/api/research/status",
		"/api/skills",
		"/api/atlas/summary",
	} {
		req := httptest.NewRequest("GET", path, nil)
		resp, err := app.Test(req, -1)
		if err != nil {
			t.Fatalf("GET %s error: %v", path, err)
		}
		if resp.StatusCode != 200 {
			t.Fatalf("GET %s expected 200, got %d", path, resp.StatusCode)
		}
	}

	req := httptest.NewRequest("GET", "/api/analytics/summary", nil)
	resp, _ := app.Test(req, -1)
	var summary map[string]interface{}
	_ = json.NewDecoder(resp.Body).Decode(&summary)
	t.Logf("Live DB summary: total=%v, clusters=%v, atlas_entries=%v, mcp_catalog_entries=%v",
		summary["total"], summary["clusters"], summary["atlas_entries"], summary["mcp_catalog_entries"])
}

