package database

import (
	"log"
	"os"
	"path/filepath"

	"github.com/jmoiron/sqlx"
	_ "modernc.org/sqlite"
)

var (
	DB              *sqlx.DB
	ArchiveDB       *sqlx.DB
	BorgDB          *sqlx.DB
	AtlasDB         *sqlx.DB
	CatalogDB       *sqlx.DB
	BookmarksDBPath string
	IsBorgSchema    bool
)

// ResolveRootPath locates an existing file/directory across the workspace root
// (., .., ../.., ../../..) first, falling back to container volume (/data).
func ResolveRootPath(rel string) string {
	candidates := []string{
		rel,
		filepath.Join("..", rel),
		filepath.Join("..", "..", rel),
		filepath.Join("..", "..", "..", rel),
		filepath.Join("/data", rel),
	}
	for _, c := range candidates {
		if info, err := os.Stat(c); err == nil {
			if info.IsDir() || info.Size() > 0 {
				return c
			}
		}
	}
	for _, c := range candidates[:4] {
		if _, err := os.Stat(c); err == nil {
			return c
		}
	}
	return rel
}

func connectOptionalDB(rel string) *sqlx.DB {
	p := ResolveRootPath(rel)
	if info, err := os.Stat(p); err != nil || info.Size() == 0 {
		return nil
	}
	db, err := sqlx.Connect("sqlite", p)
	if err != nil {
		log.Printf("Optional DB %s not connected: %v", p, err)
		return nil
	}
	return db
}

func DetectSchema(db *sqlx.DB) bool {
	type colInfo struct {
		Cid        int     `db:"cid"`
		Name       string  `db:"name"`
		Type       string  `db:"type"`
		NotNull    int     `db:"notnull"`
		DfltValue  *string `db:"dflt_value"`
		PrimaryKey int     `db:"pk"`
	}
	var cols []colInfo
	if err := db.Select(&cols, "PRAGMA table_info(bookmarks)"); err != nil {
		return false
	}
	hasShortDesc := false
	hasResearchStatus := false
	for _, c := range cols {
		if c.Name == "short_description" || c.Name == "research_level" {
			hasShortDesc = true
		}
		if c.Name == "research_status" {
			hasResearchStatus = true
		}
	}
	return hasShortDesc && !hasResearchStatus
}

func InitDB() {
	var err error
	BookmarksDBPath = ResolveRootPath("bookmarks.db")
	log.Printf("Connecting to main database at %s...", BookmarksDBPath)
	DB, err = sqlx.Connect("sqlite", BookmarksDBPath)
	if err != nil {
		log.Fatalf("CRITICAL: Failed to connect to database %s: %v", BookmarksDBPath, err)
	}
	IsBorgSchema = DetectSchema(DB)
	log.Printf("Main database connected (BorgSchema=%v).", IsBorgSchema)

	ArchiveDB = connectOptionalDB("bookmarks_archive.db")
	BorgDB = connectOptionalDB("borg.db")
	AtlasDB = connectOptionalDB("atlas.db")
	CatalogDB = connectOptionalDB("catalog.db")

	if BorgDB != nil {
		_ = InitSkillEngine(BorgDB.DB)
	} else {
		_ = InitSkillEngine(DB.DB)
	}
	log.Println("Database initialization complete.")
}

func EnsureSchema() {
	var tableCount int
	_ = DB.Get(&tableCount, "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='bookmarks'")
	if tableCount == 0 {
		schema := `
		CREATE TABLE IF NOT EXISTS bookmarks (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			url TEXT UNIQUE,
			category TEXT,
			short_description TEXT,
			long_description TEXT,
			tags TEXT,
			main_features TEXT,
			created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
			research_level TEXT DEFAULT 'heuristic',
			innovation_score INTEGER DEFAULT 0
		);`
		DB.MustExec(schema)
		IsBorgSchema = true
	}

	auxSchema := `
	CREATE TABLE IF NOT EXISTS clusters (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT UNIQUE
	);
	CREATE TABLE IF NOT EXISTS tags (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT UNIQUE
	);`
	DB.MustExec(auxSchema)
}
