import sqlite3

data = [
    ('https://github.com/alphavantage/alpha_vantage_mcp', 'Guides & Industry Trends', 'Alpha Vantage Market Intelligence', 'The official MCP server for real-time and historical market data, providing agents with access to stocks, options, forex, and technical indicators.', 'finance, real-time-data, mcp, indicator, technical-analysis', 'Live stock/options quotes, 50+ technical indicators (RSI/MACD), progressive tool discovery, multi-asset support (Forex/Crypto).'),
    ('https://github.com/financial-datasets/mcp-server', 'Guides & Industry Trends', 'Institutional Financial Datasets', 'A professional bridge to institutional-quality financial data, focusing on fundamental analysis, SEC filings, and multi-year historical metrics.', 'fundamental-analysis, sec-filings, due-diligence, finance, deep-research', 'Income Statement/Balance Sheet retrieval, 5-year comparative analysis, direct SEC filing access, historical growth tracking.'),
    ('https://github.com/coingecko/coingecko-typescript/tree/main/packages/mcp-server', 'Guides & Industry Trends', 'Official CoinGecko MCP', 'The primary crypto-native research tool, providing aggregated data for 15,000+ coins and GeckoTerminal on-chain analytics.', 'crypto, web3, coingecko, market-data, on-chain', '15,000+ Coin price/volume, GeckoTerminal network analytics (200+ nets), trending/market psychological tools, rich metadata extraction.'),
    ('https://octagonai.co/', 'Guides & Industry Trends', 'Octagon Institutional Intelligence', 'A suite of specialized analysts for high-stakes research, providing citation-backed data from SEC filings and earnings call transcripts.', 'institutional-intelligence, sec, compliance, research, orchestration', 'Form 10-K/Q/8-K analysis, 13F ownership tracking (since 2018), timestamped transcript citations, intelligent sub-agent routing.'),
    ('https://github.com/ethancod1ng/binance-mcp-server', 'Connectivity & Interoperability (MCP/A2A)', 'Binance Actionable Trading', 'A TypeScript-based implementation for direct interaction with the Binance exchange, enabling both market data retrieval and automated trading.', 'binance, crypto-trading, exchange, mcp, execution', 'Automated order placement/cancel, real-time order book depth, account balance/history management, Testnet support for safety.'),
    ('https://github.com/solangii/upbit-mcp-server', 'Connectivity & Interoperability (MCP/A2A)', 'Upbit Exchange Integration', 'A Python-based MCP server bridging the Upbit exchange API for market data, technical analysis, and automated cryptocurrency trading.', 'upbit, exchange, crypto, technical-analysis, automation', 'Real-time ticker/orderbook reading, automated buy/sell execution, deposit/withdrawal logistics, built-in TA toolset.'),
    ('https://dappier.com/', 'Infrastructure & Proxy Layers', 'Dappier AI Monetization', 'A monetization and data delivery layer for the AI internet that provides rights-cleared, real-time data from premium publishers.', 'monetization, premium-data, infrastructure, rag, marketplace', 'Rights-cleared publisher feeds (News/Sports/Finance), sub-300ms RAG latency, price-per-query marketplace, model-agnostic recommendations.'),
    ('https://github.com/kukapay/crypto-sentiment-mcp', 'Guides & Industry Trends', 'Market Mood Intelligence', 'A market psychology server that queries the Santiment API to provide agents with real-time sentiment and social dominance data.', 'market-sentiment, social-volume, santiment, psychology, whale-tracking', 'Positive/Negative mention ratios, social volume shift detection, trending narrative identification, whale movement alerts.')
]

conn = sqlite3.connect('bookmarks.db')
cursor = conn.cursor()
for url, cat, sd, ld, tags, mf, score in [(d[0], d[1], d[2], d[3], d[4], d[5], 9) for d in data]:
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
print('Successfully injected batch 27.')
