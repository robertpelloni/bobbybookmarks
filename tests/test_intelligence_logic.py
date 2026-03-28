import unittest
import sqlite3
import os
import sys

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from deduplicator import normalize_url, get_project_url
from unify_database import unify

class TestIntelligenceLogic(unittest.TestCase):
    def setUp(self):
        # We need to point unify_database.DB_PATH to our test DB for testing
        import unify_database
        self.old_db_path = unify_database.DB_PATH
        unify_database.DB_PATH = 'test_bookmarks.db'
        
        self.db_path = 'test_bookmarks.db'
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()
        self.cur.execute('''
            CREATE TABLE bookmarks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT UNIQUE,
                short_description TEXT,
                long_description TEXT,
                tags TEXT,
                category TEXT,
                research_level TEXT DEFAULT 'heuristic'
            )
        ''')
        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        # Restore the original DB path
        import unify_database
        unify_database.DB_PATH = self.old_db_path
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_url_normalization(self):
        # Basic normalization
        self.assertEqual(normalize_url("https://github.com/user/repo/"), "https://github.com/user/repo")
        self.assertEqual(normalize_url("http://GIT.COM/USER/REPO"), "http://git.com/user/repo")
        # Tracking param removal
        self.assertEqual(normalize_url("https://example.com/page?utm_source=test&q=search"), "https://example.com/page?q=search")

    def test_project_url_extraction(self):
        # GitHub sub-pages should point to the root
        self.assertEqual(get_project_url("https://github.com/robertpelloni/bobbybookmarks/blob/main/README.md"), "https://github.com/robertpelloni/bobbybookmarks")
        # Non-project URLs should remain unchanged
        self.assertEqual(get_project_url("https://news.ycombinator.com/item?id=123"), "https://news.ycombinator.com/item?id=123")

    def test_database_unification(self):
        # Add duplicate projects with different URLs
        self.cur.execute("INSERT INTO bookmarks (url, short_description, tags) VALUES (?, ?, ?)", 
                         ("https://github.com/org/tool", "Root Repo", "mcp, tool"))
        self.cur.execute("INSERT INTO bookmarks (url, short_description, tags) VALUES (?, ?, ?)", 
                         ("https://github.com/org/tool/blob/main/docs.md", "Sub Page", "agent, docs"))
        self.conn.commit()
        
        # Run the actual unification logic on the test DB
        unify()
        
        self.cur.execute("SELECT url, tags FROM bookmarks")
        rows = self.cur.fetchall()
        # Should be merged into 1 row
        self.assertEqual(len(rows), 1)
        # Should have merged tags
        self.assertIn("mcp", rows[0][1])
        self.assertIn("agent", rows[0][1])

if __name__ == '__main__':
    unittest.main()
