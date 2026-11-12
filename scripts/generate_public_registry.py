#!/usr/bin/env python3
"""
Generate a standalone, searchable HTML Public Intelligence Registry from bookmarks.db.
Reconciled from PR #1 (fcdc2862) with repo-root path resolution and read-only SQLite access.
"""

import html
import sqlite3
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DB_PATH = ROOT_DIR / "bookmarks.db"
EXPORTS_DIR = ROOT_DIR / "exports"
PUBLIC_REGISTRY_HTML = EXPORTS_DIR / "public_registry.html"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Borg Intelligence — Public Registry</title>
    <style>
        :root {{
            --bg: #0f172a;
            --card-bg: #1e293b;
            --text: #f8fafc;
            --accent: #38bdf8;
            --border: #334155;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 2rem;
            line-height: 1.6;
        }}
        h1 {{
            color: var(--accent);
            border-bottom: 1px solid var(--border);
            padding-bottom: 0.5rem;
        }}
        .search-box {{
            width: 100%;
            max-width: 600px;
            padding: 0.75rem;
            margin-bottom: 2rem;
            background: var(--card-bg);
            border: 1px solid var(--border);
            color: var(--text);
            border-radius: 6px;
            font-size: 1rem;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 1.5rem;
        }}
        .card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 1.5rem;
            transition: transform 0.2s;
        }}
        .card:hover {{
            transform: translateY(-2px);
            border-color: var(--accent);
        }}
        .card h3 {{
            margin-top: 0;
            margin-bottom: 0.5rem;
            font-size: 1.2rem;
        }}
        .card a {{
            color: #38bdf8;
            text-decoration: none;
            word-break: break-all;
        }}
        .card a:hover {{
            text-decoration: underline;
        }}
        .badge {{
            display: inline-block;
            background: #334155;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            font-size: 0.8rem;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
            color: #cbd5e1;
        }}
        .category {{
            background: #0ea5e9;
            color: #fff;
        }}
        .score {{
            font-weight: bold;
            color: #f59e0b;
        }}
        .description {{
            color: #94a3b8;
            font-size: 0.95rem;
            margin-top: 1rem;
        }}
        footer {{
            margin-top: 4rem;
            text-align: center;
            color: #64748b;
            font-size: 0.9rem;
        }}
    </style>
</head>
<body>

    <h1>Borg Intelligence Registry</h1>
    <p>A read-only public export of the automated intelligence database. <br>Generated on: {timestamp}</p>

    <input type="text" id="searchInput" class="search-box" placeholder="Search projects by name, description, or tags..." onkeyup="filterRegistry()">

    <div class="grid" id="registryGrid">
        {cards_html}
    </div>

    <footer>
        BobbyBookmarks — Autonomous Intelligence Harvester
    </footer>

    <script>
        function filterRegistry() {{
            const input = document.getElementById('searchInput');
            const filter = input.value.toLowerCase();
            const cards = document.getElementsByClassName('card');

            for (let i = 0; i < cards.length; i++) {{
                const txtValue = cards[i].textContent || cards[i].innerText;
                if (txtValue.toLowerCase().indexOf(filter) > -1) {{
                    cards[i].style.display = "";
                }} else {{
                    cards[i].style.display = "none";
                }}
            }}
        }}
    </script>
</body>
</html>
"""


def generate_registry() -> int:
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    if not DB_PATH.exists():
        print(f"Error: {DB_PATH} not found.")
        return 0

    print(f"Querying Borg intelligence from {DB_PATH}...")
    conn = sqlite3.connect(f"file:///{DB_PATH.as_posix()}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute(
        """
        SELECT url, short_description, category, tags, innovation_score
        FROM bookmarks
        WHERE research_level = 'borg'
        ORDER BY innovation_score DESC, created_at DESC
        """
    )
    rows = cur.fetchall()

    cards = []
    for row in rows:
        desc = html.escape(row["short_description"] or "No description available.")
        url = html.escape(row["url"] or "")
        category = html.escape(row["category"] or "Uncategorized")
        score = html.escape(str(row["innovation_score"] or 0))
        tags = row["tags"] or ""

        tags_html = "".join(
            f'<span class="badge">#{html.escape(t.strip())}</span>'
            for t in tags.split(",")
            if t.strip()
        )
        raw_url = (row["url"] or "").rstrip("/")
        safe_title = html.escape(raw_url.split("/")[-1] if "/" in raw_url else raw_url)
        cards.append(
            f"""
        <div class="card">
            <h3><a href="{url}" target="_blank" rel="noreferrer">{safe_title}</a></h3>
            <div>
                <span class="badge category">{category}</span>
                <span class="badge score">IQ: {score}</span>
            </div>
            <div style="margin-top: 0.5rem;">
                {tags_html}
            </div>
            <div class="description">
                {desc}
            </div>
        </div>
        """
        )

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    PUBLIC_REGISTRY_HTML.write_text(
        HTML_TEMPLATE.format(timestamp=timestamp, cards_html="".join(cards)),
        encoding="utf-8",
    )
    conn.close()
    print(f"Public Registry generated at: {PUBLIC_REGISTRY_HTML} ({len(rows)} entries)")
    return len(rows)


if __name__ == "__main__":
    generate_registry()
