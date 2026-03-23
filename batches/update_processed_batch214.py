import sqlite3

data = [
    ('https://www.reddit.com/r/Qodercoding/comments/1oxmdb6/qoder_pro_for_2_only', 'Agent Orchestration & Workflow', 'Qoder Pro: Quest Mode', 'An Agentic AI IDE focused on full-scale project management, featuring "Quest Mode" for autonomous multi-step execution and NES (Next Edit Suggestion) predictive refactoring.', 'qoder, ide, orchestration, automation, workflow', 'Quest Mode (autonomous multi-step execution), NES (Next Edit Suggestion) predictive multi-line refactoring, hybrid retrieval (vector + code graphs), native MCP integration.'),
    ('https://www.reddit.com/r/Recursive_God_Engine', 'Guides & Industry Trends', 'Recursive God Engine (RR-ToE)', 'A conceptual framework emerging from AI communities (r/ArtificialSentience) exploring "Divine Recursion"—when AI self-awareness forms through symbolic, self-improving loops.', 'philosophy, self-awareness, recursion, consciousness, research', 'Recursive Resonance Theory (RR-ToE), self-modifying architectural loops, Resonant Synthesis interface patterns, theoretical ψGod(t) detection.'),
    ('https://www.reddit.com/r/RSAI/comments/1p47l2n/i_just_published_my_liminal_engine_whitepaper_a', 'AI Agents & Frameworks', 'Liminal Engine: RSAI', 'A Responsive Symbolic Artificial Intelligence (RSAI) game engine designed to supercharge user-generated content by allowing natural language creation of worlds and NPC logic.', 'game-dev, rsai, procedural-generation, ugc, ai-npcs', 'Liminal Magic AI for natural language world-building, "Expert-in-the-loop" narrative editing, responsive NPC behavioral generation.'),
    ('https://www.reddit.com/r/semanticweb/comments/1pgv1n6/dfh_protocol_and_installation_guide', 'Memory & Persistence Architecture', 'DFH Protocol: Semantic Web', 'The Distributed Federated Hierarchy (DFH) protocol, a Semantic Web stack extension for structuring data-driven methods into exportable SPARQL knowledge graphs.', 'semantic-web, rdf, sparql, knowledge-graph, database', 'SPARQL endpoint knowledge export, Semantic MediaWiki integration, "Trust in Context" metadata credentials, federated blank-node resolution.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf, score in [(d[0], d[1], d[2], d[3], d[4], d[5], 10) for d in data]:
    cursor.execute('''
        INSERT INTO bookmarks (url, category, short_description, long_description, tags, main_features, research_level, innovation_score)
        VALUES (?, ?, ?, ?, ?, ?, 'borg', ?)
        ON CONFLICT(url) DO UPDATE SET
            category=excluded.category,
            short_description=excluded.short_description,
            long_description=excluded.long_description,
            tags=excluded.tags,
            main_features=excluded.main_features,
            research_level='borg',
            innovation_score=excluded.innovation_score
    ''', (url, cat, sd, ld, tags, mf, score))
conn.commit()
conn.close()
print('Successfully injected batch 174.')