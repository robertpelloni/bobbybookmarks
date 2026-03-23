import sqlite3

data = [
    ('https://github.com/bmad-code-org/BMAD-METHOD', 'AI Agents & Frameworks', 'BMAD Method Core', 'The primary framework for the Breakthrough Method for Agile AI-Driven Development, treating AI agents as versionable code artifacts.', 'bmad, agent-as-code, agile, framework, multi-agent', '12+ Specialized Personas (Architect/PM/Dev), Agent-as-Code markdown definitions, atomic Story File sharding, scale-adaptive planning flows.'),
    ('https://github.com/24601/BMAD-AT-CLAUDE', 'AI Agents & Frameworks', 'BMAD for Claude Code', "A specialized implementation of the BMAD Method optimized for Anthropic's Claude Code CLI and agentic workflows.", 'bmad, claude-code, optimization, automation, workflow', 'Native Claude Code integration, optimized instruction sets, automated PR sharding, CLI-first CDD support.'),
    ('https://docs.bmad.club', 'Guides & Articles', 'Official BMAD Documentation', 'Comprehensive technical guides and methodology specifications for building autonomous software engineering teams using BMAD.', 'bmad, documentation, guide, software-engineering, autonomous', 'Methodology whitepapers, persona configuration guides, document sharding tutorials, enterprise case studies.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf in data:
    cursor.execute('''
        INSERT INTO bookmarks (url, category, short_description, long_description, tags, main_features, research_level)
        VALUES (?, ?, ?, ?, ?, ?, 'deep')
        ON CONFLICT(url) DO UPDATE SET
            category=excluded.category,
            short_description=excluded.short_description,
            long_description=excluded.long_description,
            tags=excluded.tags,
            main_features=excluded.main_features,
            research_level='deep'
    ''', (url, cat, sd, ld, tags, mf))
conn.commit()
conn.close()

with open('bookmarks.txt', 'a') as f:
    f.write('\nhttps://github.com/EvolutionAPI/BMAD-METHOD-BY-EVOLUTION')

print('Successfully injected BMAD ecosystem.')
