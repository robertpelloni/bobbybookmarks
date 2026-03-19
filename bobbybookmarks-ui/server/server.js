const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
app.use(cors());

const PROCESSED_FILE_PATH = path.join(__dirname, '..', '..', 'processed.txt');

function parseLine(line) {
    // The format is: URL, CATEGORY, SHORT_DESCRIPTION, LONG_DESCRIPTION, TAGS, MAIN_FEATURES
    // Since commas might be inside the fields, a simple split might fail. 
    // We'll use a regex or heuristic if possible, but for a prototype, let's do a basic split 
    // and attempt to reconstruct it if there are more than 6 parts.
    
    // As a simple heuristic, split by ', '
    let parts = line.split(', ');
    if (parts.length < 6) return null;
    
    let url = parts[0];
    let category = parts[1];
    let short_desc = parts[2];
    
    // We don't know exactly where long_desc ends and tags begin, 
    // but typically MAIN_FEATURES is the last part, and TAGS is the second to last.
    // However, tags and main_features might also contain ', '.
    // Let's just bundle the rest for now in a safe way.
    
    return {
        id: url,
        url: url,
        category: category,
        short_description: short_desc,
        raw_content: line // Send raw line to frontend just in case
    };
}

app.get('/api/bookmarks', (req, res) => {
    try {
        const data = fs.readFileSync(PROCESSED_FILE_PATH, 'utf8');
        const lines = data.split('\n').filter(l => l.trim().length > 0);
        
        let bookmarks = lines.map(parseLine).filter(b => b !== null);
        
        // Simple search query
        const q = req.query.q ? req.query.q.toLowerCase() : null;
        if (q) {
            bookmarks = bookmarks.filter(b => b.raw_content.toLowerCase().includes(q));
        }
        
        // Simple category filter
        const category = req.query.category;
        if (category) {
            bookmarks = bookmarks.filter(b => b.category === category);
        }

        res.json(bookmarks);
    } catch (error) {
        console.error("Error reading bookmarks:", error);
        res.status(500).json({ error: "Failed to read bookmarks data" });
    }
});

app.get('/api/categories', (req, res) => {
    try {
        const data = fs.readFileSync(PROCESSED_FILE_PATH, 'utf8');
        const lines = data.split('\n').filter(l => l.trim().length > 0);
        
        let categories = new Set();
        lines.forEach(line => {
            let parts = line.split(', ');
            if (parts.length >= 2) {
                categories.add(parts[1]);
            }
        });
        
        res.json(Array.from(categories));
    } catch (error) {
        res.status(500).json({ error: "Failed to read categories" });
    }
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
