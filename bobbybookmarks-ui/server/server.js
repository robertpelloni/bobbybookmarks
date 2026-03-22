const express = require('express');
const cors = require('cors');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const app = express();
app.use(cors());

const DB_PATH = path.join(__dirname, '..', '..', 'bookmarks.db');
const db = new sqlite3.Database(DB_PATH);

app.get('/api/bookmarks', (req, res) => {
    const q = req.query.q ? `%${req.query.q}%` : '%';
    const category = req.query.category || '%';
    const tag = req.query.tag ? `%${req.query.tag}%` : '%';
    const sortBy = req.query.sort || 'created_at';
    const order = req.query.order || 'DESC';

    // Validate sort column to prevent injection
    const allowedSort = ['created_at', 'short_description', 'category'];
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
        if (err) {
            console.error(err);
            return res.status(500).json({ error: err.message });
        }
        res.json(rows);
    });
});

app.get('/api/categories', (req, res) => {
    db.all('SELECT DISTINCT category FROM bookmarks ORDER BY category', [], (err, rows) => {
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
    db.get('SELECT COUNT(*) as count, SUM(CASE WHEN research_level=\"deep\" THEN 1 ELSE 0 END) as deep, SUM(CASE WHEN research_level=\"borg\" THEN 1 ELSE 0 END) as borg FROM bookmarks', [], (err, row) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(row);
    });
});

const PORT = process.env.PORT || 3002;
app.listen(PORT, () => {
    console.log(`Express SQL Server running on port ${PORT}`);
});
