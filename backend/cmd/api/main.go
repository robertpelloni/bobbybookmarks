package main

import (
	"bobbybookmarks/internal/api"
	"bobbybookmarks/internal/database"
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/cors"
	"log"
	"os"
)

func main() {
	database.InitDB()
	app := fiber.New()
	app.Use(cors.New())

	api.RegisterRoutes(app)

	port := os.Getenv("PORT")
	if port == "" {
		port = "5000"
	}

	log.Fatal(app.Listen(":" + port))
}
