import sqlite3

data = [
    ('https://www.reddit.com/r/raindropio/comments/1r12c5k/mcp_support_added_to_raindrop/', 'Connectivity & Interoperability (MCP/A2A)', 'Raindrop.io MCP Support', 'Official Model Context Protocol (MCP) integration for Raindrop.io, enabling AI agents to search and organize personal bookmark libraries.', 'raindrop, mcp, bookmarks, second-brain, search', 'Native MCP server support, direct AI bookmark management, research workflow acceleration, second-brain automation.'),
    ('https://www.reddit.com/r/singularity/comments/1pwhgre/andrej_karpathy_powerful_alien_tech_is_heredo_not/', 'Guides & Industry Trends', 'Karpathy: Alien Tech Core', 'Andrej Karpathy\'s thesis on LLMs as "alien technology," emphasizing synthetic data and the potential for AGI reasoning in models under 1B parameters.', 'karpathy, philosophy, synthetic-data, small-models, agi', 'Synthetic data scaling thesis, 1B-parameter AGI reasoning potential, "Alien Technology" communication paradigm.'),
    ('https://www.reddit.com/r/saasbuild/comments/1r043b5/built_4_startups_only_succeeded_when_i_stopped/', 'Guides & Industry Trends', 'Boring Problem Validation', 'A founder\'s case study on finding SaaS success by pivoting from "revolutionary ideas" to solving mundane "boring problems" for established communities.', 'saas, validation, product-market-fit, entrepreneurship, strategy', 'Solving "Boring Problems," validation-first approach, distribution over product focus, specific community pain points.'),
    ('https://www.reddit.com/r/semanticweb/comments/1r0neth/created_an_owl_2_rl_reasoner/', 'AI Agents & Frameworks', 'Growl: OWL 2 RL Reasoner', 'A high-performance, Apache-licensed OWL 2 RL reasoner written in the Slop contract language and transpiled to C for commercial Rust environments.', 'semantic-web, owl2, reasoner, logic, performance', 'Slop-to-C transpilation, batch materializer performance, formal theorem prover verification, Apache-licensed open source.')
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
print('Successfully injected batch 96.')