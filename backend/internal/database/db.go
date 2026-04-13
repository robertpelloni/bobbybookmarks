package database

import (
	"log"
	"github.com/jmoiron/sqlx"
	_ "github.com/mattn/go-sqlite3"
)

var DB *sqlx.DB
var ArchiveDB *sqlx.DB

func InitDB() {
	var err error
	DB, err = sqlx.Connect("sqlite3", "/data/bookmarks.db")
	if err != nil {
		DB, err = sqlx.Connect("sqlite3", "../bookmarks.db") // fallback
	}

	ArchiveDB, err = sqlx.Connect("sqlite3", "/data/bookmarks_archive.db")
	if err != nil {
		ArchiveDB, err = sqlx.Connect("sqlite3", "../bookmarks_archive.db") // fallback
	}
}
