import sqlite3
import os
import html
from datetime import datetime

DB_PATH = 'bookmarks.db'
EXPORTS_DIR = 'exports'
PUBLIC_REGISTRY_HTML = os.path.join(EXPORTS_DIR, 'public_registry.html')

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Borg Public Registry</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #0f172a;
            color: #f8fafc;
            margin: 0;
            padding: 2rem;
            line-height: 1.6;
        }}
        h1 {{
            color: #38bdf8;
            border-bottom: 2px solid #334155;
            padding-bottom: 0.5rem;
            margin-bottom: 2rem;
        }}
        .search-box {{
            width: 100%;
            padding: 1rem;
            margin-bottom: 2rem;
            background: #1e293b;
            border: 1px solid #334155;
            color: #f8fafc;
            border-radius: 8px;
            font-size: 1rem;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }}
        .card {{
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 8px;
            padding: 1.5rem;
            transition: transform 0.2s;
        }}
        .card:hover {{
            transform: translateY(-2px);
            border-color: #475569;
        }}
        .card h3 {{
            margin-top: 0;
            color: #e2e8f0;
            font-size: 1.1rem;
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
        BobbyBookmarks - Autonomous Intelligence Harvester
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

def generate_registry():
    if not os.path.exists(EXPORTS_DIR):
        os.makedirs(EXPORTS_DIR)

    if not os.path.exists(DB_PATH):
        print(f"Error: {DB_PATH} not found.")
        return

    print("Querying Borg intelligence...")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute('''
        SELECT url, short_description, category, tags, innovation_score
        FROM bookmarks
        WHERE research_level = 'borg'
        ORDER BY innovation_score DESC, created_at DESC
    ''')
    rows = cur.fetchall()

    cards_html = ""
    for row in rows:
        desc = html.escape(row['short_description'] or "No description available.")
        url = html.escape(row['url'])
        category = html.escape(row['category'] or "Uncategorized")
        score = html.escape(str(row['innovation_score'] or 0))
        tags = html.escape(row['tags'] or "")

        # Parse tags
        tags_html = ""
        if tags:
            tag_list = [t.strip() for t in tags.split(',') if t.strip()]
            for tag in tag_list:
                tags_html += f'<span class="badge">#{tag}</span>'

        # Card HTML
        safe_title = html.escape(url.split('/')[-1] if '/' in url else url)
        card = f"""
        <div class="card">
            <h3><a href="{url}" target="_blank">{safe_title}</a></h3>
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
        cards_html += card

    print("Generating HTML report...")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    final_html = HTML_TEMPLATE.format(timestamp=timestamp, cards_html=cards_html)

    with open(PUBLIC_REGISTRY_HTML, 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"Public Registry generated successfully at: {PUBLIC_REGISTRY_HTML}")
    print(f"Total projects exported: {len(rows)}")

    conn.close()

if __name__ == "__main__":
    generate_registry()
