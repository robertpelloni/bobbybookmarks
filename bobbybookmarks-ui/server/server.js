const express = require('express');
const cors = require('cors');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const { GoogleGenerativeAI } = require("@google/generative-ai");

const app = express();
app.use(cors());

const DB_PATH = path.join(__dirname, '..', '..', 'bookmarks.db');
const db = new sqlite3.Database(DB_PATH);

// Initialize Gemini
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY || "AIzaSyB9juQ3l2gNtaFxAPkNuXlrV7Q99zL_yTo");
const embeddingModel = genAI.getGenerativeModel({ model: "text-embedding-004" }); 

function cosineSimilarity(vecA, vecB) {
    let dotProduct = 0;
    let normA = 0;
    let normB = 0;
    for (let i = 0; i < vecA.length; i++) {
        dotProduct += vecA[i] * vecB[i];
        normA += vecA[i] * vecA[i];
        normB += vecB[i] * vecB[i];
    }
    return dotProduct / (Math.sqrt(normA) * Math.sqrt(normB));
}

app.get('/api/bookmarks', (req, res) => {
    const q = req.query.q ? `%${req.query.q}%` : '%';
    const category = req.query.category || '%';
    const tag = req.query.tag ? `%${req.query.tag}%` : '%';
    const sortBy = req.query.sort || 'created_at';
    const order = req.query.order || 'DESC';

    const allowedSort = ['created_at', 'short_description', 'category', 'innovation_score'];
    const finalSort = allowedSort.includes(sortBy) ? sortBy : 'created_at';
    const finalOrder = order.toUpperCase() === 'ASC' ? 'ASC' : 'DESC';

    const sql = `
        SELECT * FROM bookmarks 
        WHERE (url LIKE ? OR short_description LIKE ? OR long_description LIKE ? OR tags LIKE ?)
        AND category LIKE ?
        AND tags LIKE ?
        ORDER BY ${finalSort} ${finalOrder}
        LIMIT 500
    `;

    db.all(sql, [q, q, q, q, category, tag], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(rows);
    });
});

app.get('/api/bookmarks/by-feature', (req, res) => {
    const feature = req.query.feature ? `%${req.query.feature}%` : '%';
    const sql = `
        SELECT * FROM bookmarks 
        WHERE main_features LIKE ?
        ORDER BY innovation_score DESC
    `;
    db.all(sql, [feature], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(rows);
    });
});

app.get('/api/categories', (req, res) => {
    db.all('SELECT DISTINCT category FROM bookmarks WHERE category IS NOT NULL AND category != "" ORDER BY category', [], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(rows.map(row => row.category));
    });
});

app.get('/api/random', (req, res) => {
    db.get('SELECT * FROM bookmarks ORDER BY RANDOM() LIMIT 1', [], (err, row) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(row);
    });
});

app.get('/api/stats', (req, res) => {
    const sql = `
        SELECT 
            COUNT(*) as count, 
            SUM(CASE WHEN research_level='deep' THEN 1 ELSE 0 END) as deep, 
            SUM(CASE WHEN research_level='borg' THEN 1 ELSE 0 END) as borg,
            SUM(CASE WHEN research_level='heuristic' THEN 1 ELSE 0 END) as heuristic
        FROM bookmarks
    `;
    db.get(sql, [], (err, row) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(row);
    });
});

app.get('/api/analytics/timeline', (req, res) => {
    const sql = `
        SELECT date(created_at) as day, COUNT(*) as count 
        FROM bookmarks 
        GROUP BY day 
        ORDER BY day ASC
    `;
    db.all(sql, [], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        let cumulative = 0;
        const result = rows.map(row => {
            cumulative += row.count;
            return { ...row, cumulative };
        });
        res.json(result);
    });
});

app.get('/api/analytics/categories', (req, res) => {
    const sql = `
        SELECT category as name, COUNT(*) as value 
        FROM bookmarks 
        WHERE category IS NOT NULL AND category != ""
        GROUP BY category 
        ORDER BY value DESC
    `;
    db.all(sql, [], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(rows);
    });
});

app.get('/api/analytics/tags', (req, res) => {
    db.all('SELECT tags FROM bookmarks WHERE tags IS NOT NULL AND tags != ""', [], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        const tagCounts = {};
        rows.forEach(row => {
            const tags = row.tags.split(',').map(t => t.trim().toLowerCase()).filter(t => t);
            tags.forEach(tag => {
                tagCounts[tag] = (tagCounts[tag] || 0) + 1;
            });
        });
        const sortedTags = Object.entries(tagCounts)
            .map(([name, value]) => ({ name, value }))
            .sort((a, b) => b.value - a.value)
            .slice(0, 20);
        res.json(sortedTags);
    });
});

app.get('/api/analytics/graph', (req, res) => {
    const sql = `
        SELECT id, url, short_description, category, tags, innovation_score 
        FROM bookmarks 
        WHERE research_level = 'borg'
        LIMIT 300
    `;
    db.all(sql, [], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        const nodes = [];
        const links = [];
        const categoryNodes = new Set();
        rows.forEach(row => {
            nodes.push({
                id: `bm-${row.id}`,
                name: row.short_description || row.url,
                type: 'bookmark',
                category: row.category,
                score: row.innovation_score
            });
            if (row.category) {
                if (!categoryNodes.has(row.category)) {
                    nodes.push({ id: row.category, name: row.category, type: 'category' });
                    categoryNodes.add(row.category);
                }
                links.push({ source: `bm-${row.id}`, target: row.category, value: 2 });
            }
            if (row.tags) {
                const tags = row.tags.split(',').map(t => t.trim().toLowerCase()).filter(t => t);
                tags.slice(0, 3).forEach(tag => {
                    const tagId = `tag-${tag}`;
                    if (!categoryNodes.has(tagId)) {
                        nodes.push({ id: tagId, name: `#${tag}`, type: 'tag' });
                        categoryNodes.add(tagId);
                    }
                    links.push({ source: `bm-${row.id}`, target: tagId, value: 1 });
                });
            }
        });
        res.json({ nodes, links });
    });
});

app.get('/api/analytics/nebula', (req, res) => {
    const sql = `
        SELECT b.id, b.url, b.short_description, b.category, b.innovation_score, n.x, n.y
        FROM bookmarks b
        JOIN nebula_map n ON b.id = n.bookmark_id
    `;
    db.all(sql, [], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(rows);
    });
});

app.get('/api/debates', (req, res) => {
    const sql = `
        SELECT d.*, b.short_description, b.url, b.category
        FROM debates d
        JOIN bookmarks b ON d.bookmark_id = b.id
        ORDER BY d.debated_at DESC
    `;
    db.all(sql, [], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(rows);
    });
});

app.get('/api/reports/latest', (req, res) => {
    const reportPath = path.join(__dirname, '..', '..', 'logs', 'reports', 'latest.md');
    const fs = require('fs');
    if (fs.existsSync(reportPath)) {
        res.setHeader('Content-Type', 'text/markdown');
        res.sendFile(reportPath);
    } else {
        res.json({ content: "The Borg Intelligence Officer is currently synthesizing the first briefing. Check back shortly!" });
    }
});

app.get('/api/network/health', (req, res) => {
    db.all('SELECT * FROM agent_heartbeats ORDER BY last_pulse DESC', [], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(rows.map(r => ({
            ...r,
            status_metadata: JSON.parse(r.status_metadata || '{}')
        })));
    });
});

app.get('/api/live-feed', (req, res) => {
    const feedPath = path.join(__dirname, '..', '..', 'logs', 'live_feed.json');
    const fs = require('fs');
    if (fs.existsSync(feedPath)) {
        fs.readFile(feedPath, 'utf8', (err, data) => {
            if (err) return res.status(500).json({ error: err.message });
            res.json(JSON.parse(data));
        });
    } else {
        res.json([]);
    }
});

app.get('/api/battle-cards', (req, res) => {
    const sql = `
        SELECT c.*, b.short_description, b.url, b.category, b.innovation_score
        FROM battle_cards c
        JOIN bookmarks b ON c.bookmark_id = b.id
        ORDER BY b.innovation_score DESC
    `;
    db.all(sql, [], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(rows);
    });
});

app.get('/api/skills', (req, res) => {
    const skillsDir = path.join(__dirname, '..', '..', 'skills', 'autonomous');
    const fs = require('fs');
    if (!fs.existsSync(skillsDir)) return res.json([]);
    
    fs.readdir(skillsDir, (err, files) => {
        if (err) return res.status(500).json({ error: err.message });
        const skills = files.filter(f => f.endsWith('.md')).map(f => {
            const content = fs.readFileSync(path.join(skillsDir, f), 'utf8');
            return { name: f.replace('.md', ''), content };
        });
        res.json(skills);
    });
});

app.get('/api/system/logs', (req, res) => {
    const logPath = path.join(__dirname, '..', '..', 'logs', 'self_healing.log');
    const fs = require('fs');
    if (fs.existsSync(logPath)) {
        const lines = fs.readFileSync(logPath, 'utf8').split('\n').filter(l => l.trim()).slice(-100);
        res.json(lines);
    } else {
        res.json(["System logs initialized. No self-healing pulse recorded yet."]);
    }
});

app.get('/api/clusters', (req, res) => {
    db.all('SELECT * FROM clusters ORDER BY bookmark_count DESC', [], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(rows.map(r => ({
            ...r,
            tags: JSON.parse(r.tags || '[]')
        })));
    });
});

app.get('/api/search/semantic', async (req, res) => {
    const query = req.query.q;
    if (!query) return res.status(400).json({ error: "Missing query" });
    
    try {
        // 1. Embed query
        const result = await embeddingModel.embedContent(query);
        const queryVector = result.embedding.values;

        // 2. Fetch all embeddings from DB
        db.all('SELECT bookmark_id, vector FROM embeddings', [], (err, embRows) => {
            if (err) return res.status(500).json({ error: err.message });
            
            if (embRows.length === 0) {
                return res.json({ message: "No vectors indexed yet", results: [] });
            }

            // 3. Rank by similarity
            const scored = embRows.map(row => {
                const vector = new Float32Array(row.vector.buffer, row.vector.byteOffset, row.vector.byteLength / 4);
                return {
                    id: row.bookmark_id,
                    score: cosineSimilarity(queryVector, vector)
                };
            }).sort((a, b) => b.score - a.score).slice(0, 20);

            // 4. Fetch bookmark details for top matches
            const ids = scored.map(s => s.id);
            const placeholders = ids.map(() => '?').join(',');
            const sql = `SELECT * FROM bookmarks WHERE id IN (${placeholders})`;
            
            db.all(sql, ids, (err, bookmarkRows) => {
                if (err) return res.status(500).json({ error: err.message });
                
                // Maintain ranked order
                const sortedResults = ids.map(id => bookmarkRows.find(b => b.id === id)).filter(b => b);
                res.json({ results: sortedResults });
            });
        });
    } catch (error) {
        console.error("Semantic search failed:", error);
        res.status(500).json({ error: error.message });
    }
});

const PORT = process.env.PORT || 3002;
app.listen(PORT, () => {
    console.log(`Express SQL Server running on port ${PORT}`);
});
