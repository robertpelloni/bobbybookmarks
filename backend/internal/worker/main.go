package main

import (
	"bobbybookmarks/internal/database"
	"bobbybookmarks/internal/models"
	"log"
	"time"
)

func main() {
	database.InitDB()
	log.Println("BobbyBookmarks Research Worker Active...")

	for {
		processNext()
		time.Sleep(5 * time.Second)
	}
}

func processNext() {
	var bm models.Bookmark
	if database.IsBorgSchema {
		err := database.DB.Get(&bm, "SELECT id, COALESCE(url, '') AS url FROM bookmarks WHERE research_level = 'heuristic' LIMIT 1")
		if err != nil {
			return
		}
		log.Printf("Queued heuristic node awaiting Python deep_research worker: %s\n", bm.URL)
		return
	}

	err := database.DB.Get(&bm, "SELECT id, COALESCE(url, '') AS url FROM bookmarks WHERE research_status = 'pending' LIMIT 1")
	if err != nil {
		return
	}

	log.Printf("Researching: %s\n", bm.URL)
	database.DB.Exec("UPDATE bookmarks SET research_status = 'running' WHERE id = ?", bm.ID)
	time.Sleep(2 * time.Second)
	database.DB.Exec("UPDATE bookmarks SET research_status = 'done', researched_at = ? WHERE id = ?", time.Now(), bm.ID)
	log.Printf("Completed: %s\n", bm.URL)
}
