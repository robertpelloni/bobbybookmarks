
import os

links = [
    ('https://github.com/OthersideAI/self-operating-computer', 'AI Agents & Frameworks', 'Self-Operating Computer', 'A framework enabling multimodal AI to operate computers via screen vision and mouse/keyboard emulation.', 'vision-agent, autonomous, computer-control, multimodal', 'OCR Navigation, YOLOv8 visual grounding, Voice Mode, Cross-platform.'),
    ('https://github.com/KillianLucas/open-interpreter', 'AI Agents & Frameworks', 'Open Interpreter', 'A natural language interface for LLMs to run code locally with full access to internet, files, and libraries.', 'code-interpreter, local-llm, automation, sandbox', 'Terminal Interface, Local Model support (Ollama), Browser automation, Data Analysis.'),
    ('https://github.com/Skyvern-AI/skyvern', 'AI Agents & Frameworks', 'Skyvern Browser Agent', 'An open-source browser automation platform using Vision LLMs to execute workflows without brittle scripts.', 'browser-automation, computer-vision, workflow, ai-rpa', 'Vision-based navigation, 2FA support, Playwright SDK, No-code builder.'),
    ('https://github.com/vanna-ai/vanna', 'AI Agents & Frameworks', 'Vanna Text-to-SQL', 'An open-source Python framework for high-accuracy natural language interaction with SQL databases.', 'text-to-sql, data-analysis, enterprise-ai, database', 'Plotly Chart generation, RAG-enhanced SQL, Web Chat component, Multi-database support.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
