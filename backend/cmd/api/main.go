package main

import (
	"bobbybookmarks/internal/api"
	"bobbybookmarks/internal/database"
	"log"
	"os"
	"path/filepath"
	"strings"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/cors"
)

func main() {
	database.InitDB()
	database.EnsureSchema()
	app := fiber.New()
	app.Use(cors.New())

	api.RegisterRoutes(app)

	atlasPath := database.ResolveRootPath("atlas.html")
	app.Get("/atlas", func(c *fiber.Ctx) error {
		return c.SendFile(atlasPath)
	})
	app.Get("/atlas.html", func(c *fiber.Ctx) error {
		return c.SendFile(atlasPath)
	})

	distDir := database.ResolveRootPath("dist")
	indexFile := filepath.Join(distDir, "index.html")
	app.Static("/", distDir)

	app.Get("/*", func(c *fiber.Ctx) error {
		if strings.HasPrefix(c.Path(), "/api/") {
			return c.Status(404).JSON(fiber.Map{"error": "endpoint not found"})
		}
		return c.SendFile(indexFile)
	})

	port := strings.TrimSpace(os.Getenv("PORT"))
	if port == "" {
		port = "5000"
	}

	log.Printf("BobbyIntel v1.2.0 unified server starting on port %s (dist=%s)...", port, distDir)
	log.Fatal(app.Listen(":" + port))
}
