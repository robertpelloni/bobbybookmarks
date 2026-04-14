package database

import (
	"github.com/jmoiron/sqlx"
	_ "github.com/mattn/go-sqlite3"
)

var DB *sqlx.DB
var ArchiveDB *sqlx.DB

func InitDB() {
	var err error
	DB, err = sqlx.Connect("sqlite3", "/data/bookmarks.db")
	if err != nil {
		DB, err = sqlx.Connect("sqlite3", "bookmarks.db") // fallback to local
		if err != nil {
			panic("Failed to connect to database: " + err.Error())
		}
	}

	ArchiveDB, err = sqlx.Connect("sqlite3", "/data/bookmarks_archive.db")
	if err != nil {
		ArchiveDB, _ = sqlx.Connect("sqlite3", "bookmarks_archive.db") // fallback to local
	}
}

func EnsureSchema() {
	schema := `
	CREATE TABLE IF NOT EXISTS bookmarks (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		url TEXT NOT NULL UNIQUE,
		title TEXT,
		description TEXT,
		page_title TEXT,
		page_description TEXT,
		research_status TEXT DEFAULT 'pending',
		imported_at DATETIME DEFAULT CURRENT_TIMESTAMP,
		researched_at DATETIME,
		cluster_id INTEGER,
		source TEXT,
		is_duplicate BOOLEAN DEFAULT 0,
		original_id INTEGER
	);
	CREATE TABLE IF NOT EXISTS clusters (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT UNIQUE
	);
	CREATE TABLE IF NOT EXISTS tags (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT UNIQUE
	);
	`
	DB.MustExec(schema)
}
