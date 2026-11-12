package models

import (
	"time"
)

type Bookmark struct {
	ID               int        `db:"id" json:"id"`
	URL              string     `db:"url" json:"url"`
	Title            string     `db:"title" json:"title"`
	Description      string     `db:"description" json:"description"`
	PageTitle        string     `db:"page_title" json:"page_title"`
	PageDescription  string     `db:"page_description" json:"page_description"`
	Status           string     `db:"research_status" json:"research_status"`
	ImportedAt       string     `db:"imported_at" json:"imported_at"`
	ResearchedAt     *time.Time `db:"researched_at" json:"researched_at,omitempty"`
	ClusterID        *int       `db:"cluster_id" json:"cluster_id,omitempty"`
	Source           string     `db:"source" json:"source"`
	IsDuplicate      bool       `db:"is_duplicate" json:"is_duplicate"`
	OriginalID       *int       `db:"original_id" json:"original_id,omitempty"`
	Category         string     `db:"category" json:"category,omitempty"`
	ShortDescription string     `db:"short_description" json:"short_description,omitempty"`
	LongDescription  string     `db:"long_description" json:"long_description,omitempty"`
	Tags             string     `db:"tags" json:"tags,omitempty"`
	MainFeatures     string     `db:"main_features" json:"main_features,omitempty"`
	ResearchLevel    string     `db:"research_level" json:"research_level,omitempty"`
	InnovationScore  int        `db:"innovation_score" json:"innovation_score"`
}

type Tag struct {
	ID   int    `db:"id" json:"id"`
	Name string `db:"name" json:"name"`
}

type Cluster struct {
	ID            int      `db:"id" json:"id"`
	Name          string   `db:"name" json:"name"`
	BookmarkCount int      `json:"bookmark_count"`
	Tags          []string `json:"tags"`
}

type ImportSession struct {
	ID             int       `db:"id" json:"id"`
	SourceType     string    `db:"source_type" json:"source_type"`
	SourceName     string    `db:"source_name" json:"source_name"`
	TotalCount     int       `db:"total_count" json:"total_count"`
	ImportedCount  int       `db:"imported_count" json:"imported_count"`
	DuplicateCount int       `db:"duplicate_count" json:"duplicate_count"`
	CreatedAt      time.Time `db:"created_at" json:"created_at"`
}

type SkillExecution struct {
	ID             int     `db:"id" json:"id"`
	SkillName      string  `db:"skill_name" json:"skill_name"`
	Strategy       string  `db:"strategy" json:"strategy"`
	ExecutionCount int     `db:"execution_count" json:"execution_count"`
	SuccessCount   int     `db:"success_count" json:"success_count"`
	WinRate        float64 `db:"win_rate" json:"win_rate"`
	Status         string  `db:"status" json:"status"`
}
