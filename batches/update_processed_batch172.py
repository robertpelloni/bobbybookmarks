import sqlite3

data = [
    ('https://en.wikipedia.org/wiki/Veilid', 'Connectivity & Interoperability (MCP/A2A)', 'Veilid: Private P2P', 'An open-source peer-to-peer framework developed by the Cult of the Dead Cow (cDc) for high-performance privacy-first application routing.', 'p2p, privacy, networking, protocol, decentralization', '256-bit public key identifiers, multi-protocol transport (UDP/TCP/WS), network-switching resilience, upgradable cryptography, no-token architecture.'),
    ('https://factory.ai/', 'AI Agents & Frameworks', 'Factory.ai: Industrial Agents', 'An industrial agentic AI platform that enables autonomous orchestration of production schedules and supplier contracts grounded in enterprise ontologies.', 'industrial-ai, manufacturing, orchestration, automation, ontology', 'Autonomous decision-execution, digital-twin ontology grounding, A2A/MCP integration, AIP Evals safety framework.'),
    ('https://fal.ai/', 'Infrastructure & Proxy Layers', 'Fal.ai: Media Inference', 'A high-speed, globally distributed serverless GPU engine optimized for "day zero" support of SOTA generative video, image, and 3D models.', 'gpu, inference, generative-media, serverless, infrastructure', '10x faster diffusion inference, 100M+ daily call scalability, multimodal workflow support, serverless zero-cold-start architecture.'),
    ('https://floooh.github.io/2018/06/17/handles-vs-pointers.html', 'Guides & Industry Trends', 'Handles: Memory Safety', 'A systems programming analysis advocating for opaque handles (index + counter) over direct pointers to achieve memory safety and defragmentation.', 'systems-programming, memory-safety, pointers, handles, architecture', 'Memory relocatability (defragmentation), UAF detection (generation counters), mandatory runtime bounds checking, high-integrity identifier resolution.')
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
print('Successfully injected batch 122.')