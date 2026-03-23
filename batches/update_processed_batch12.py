
import os

links = [
    ('https://github.com/grapeot/devin.cursorrules', 'AI Agents & Frameworks', 'Devin Cursor Rules', 'A collection of instructions designed to transform AI editors like Cursor and Windsurf into autonomous, self-evolving agents like Devin.', 'cursor, devin, agent-instructions, scratchpad', 'Scratchpad Planning, Lessons Learned loop, Autonomous Tool-use, Self-evolution.'),
    ('https://github.com/grapeot/devin.cursorrules/blob/master/.github/copilot-instructions.md', 'Guides & Articles', 'Copilot Custom Instructions', 'Specific custom instructions for GitHub Copilot based on the Devin autonomous engineering philosophy, emphasizing planning and verification.', 'copilot, instructions, prompt-engineering, devin-style', 'Persistent Scratchpad, Progress Tracking, Engineers logic, Lesson recording.'),
    ('https://www.reddit.com/r/cursor/comments/1paezid/best_cursorrules_for_building_apps_with_devin/', 'Guides & Articles', 'Best CursorRules Discussion', 'Reddit community discussion on optimizing .cursorrules for autonomous app building, featuring the Devin-style philosophy and custom toolsets.', 'reddit, discussion, cursor, agentic-coding', 'Community Rules, Tool Integration, Workflow Hacks, Performance Tips.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
