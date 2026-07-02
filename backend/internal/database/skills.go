package database

import (
	"database/sql"
	"log"
)

// InitSkillEngine initializes the Phase 2 Skill Engine schemas
func InitSkillEngine(db *sql.DB) error {
	query := `
	CREATE TABLE IF NOT EXISTS skill_executions (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		skill_name TEXT NOT NULL,
		strategy TEXT NOT NULL,
		execution_count INTEGER DEFAULT 0,
		success_count INTEGER DEFAULT 0,
		win_rate REAL DEFAULT 0.0,
		status TEXT DEFAULT 'active'
	);
	`
	_, err := db.Exec(query)
	if err != nil {
		log.Printf("Error initializing skill_executions: %v", err)
		return err
	}
	return nil
}
