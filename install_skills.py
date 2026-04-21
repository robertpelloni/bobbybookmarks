import os
import shutil

SKILLS_TO_INSTALL = [
    # ... existing skills ...
    {
        'name': 'gh-address-comments',
        'src': 'submodules/bkircher-skills/gh-address-comments',
        'files': ['SKILL.md']
    },
    {
        'name': 'gh-code-review',
        'src': 'submodules/bkircher-skills/gh-code-review',
        'files': ['SKILL.md']
    },
    {
        'name': 'gh-run-failure',
        'src': 'submodules/bkircher-skills/gh-run-failure',
        'files': ['SKILL.md']
    },
    {
        'name': 'git-commit-message',
        'src': 'submodules/bkircher-skills/git-commit-message',
        'files': ['SKILL.md']
    },
    {
        'name': 'postgresql-table-design',
        'src': 'submodules/bkircher-skills/postgresql-table-design',
        'files': ['SKILL.md']
    },
    {
        'name': 'unit-testing-bkircher',
        'src': 'submodules/bkircher-skills/unit-testing',
        'files': ['SKILL.md']
    },
    {
        'name': 'notion-meeting-intelligence',
        'src': 'submodules/openai-skills/skills/.curated/notion-meeting-intelligence',
        'files': ['SKILL.md']
    },
    {
        'name': 'notion-spec-to-implementation',
        'src': 'submodules/openai-skills/skills/.curated/notion-spec-to-implementation',
        'files': ['SKILL.md']
    },
    {
        'name': 'playwright-interactive',
        'src': 'submodules/openai-skills/skills/.curated/playwright-interactive',
        'files': ['SKILL.md']
    },
    {
        'name': 'skill-creator',
        'src': 'submodules/anthropics-skills/skills/skill-creator',
        'files': ['SKILL.md']
    },
    {
        'name': 'mcp-builder',
        'src': 'submodules/anthropics-skills/skills/mcp-builder',
        'files': ['SKILL.md']
    },
    {
        'name': 'webapp-testing-v2',
        'src': 'submodules/anthropics-skills/skills/webapp-testing',
        'files': ['SKILL.md']
    },
    {
        'name': 'security-threat-model',
        'src': 'submodules/openai-skills/skills/.curated/security-threat-model',
        'files': ['SKILL.md']
    },
    {
        'name': 'security-best-practices',
        'src': 'submodules/openai-skills/skills/.curated/security-best-practices',
        'files': ['SKILL.md']
    },
    # New ykdojo skills
    {
        'name': 'yk-clone',
        'src': 'submodules/ykdojo-claude-code-tips/skills/clone',
        'files': ['SKILL.md']
    },
    {
        'name': 'yk-half-clone',
        'src': 'submodules/ykdojo-claude-code-tips/skills/half-clone',
        'files': ['SKILL.md']
    },
    {
        'name': 'yk-handoff',
        'src': 'submodules/ykdojo-claude-code-tips/skills/handoff',
        'files': ['SKILL.md']
    },
    {
        'name': 'yk-reddit-fetch',
        'src': 'submodules/ykdojo-claude-code-tips/skills/reddit-fetch',
        'files': ['SKILL.md']
    },
    {
        'name': 'yk-gha',
        'src': 'submodules/ykdojo-claude-code-tips/skills/gha',
        'files': ['SKILL.md']
    },
    {
        'name': 'yk-review-claudemd',
        'src': 'submodules/ykdojo-claude-code-tips/skills/review-claudemd',
        'files': ['SKILL.md']
    }
]

def handle_conversions():
    skills_dir = 'skills'
    
    # A2A Protocol
    a2a_target = os.path.join(skills_dir, 'a2a-protocol')
    if not os.path.exists(a2a_target): os.makedirs(a2a_target)
    a2a_src = 'submodules/a2aproject-A2A/docs/specification.md'
    if os.path.exists(a2a_src):
        with open(a2a_src, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(os.path.join(a2a_target, 'SKILL.md'), 'w', encoding='utf-8') as f:
            f.write("# A2A Protocol Expert\n\nExpert in Agent-to-Agent (A2A) communication protocol and standards.\n\n" + content)
        print("Converted A2A specification to skill.")

    # TaskSync
    ts_target = os.path.join(skills_dir, 'tasksync')
    if not os.path.exists(ts_target): os.makedirs(ts_target)
    ts_src = 'submodules/4regab-TaskSync/Prompt/tasksync-v5.2.md'
    if os.path.exists(ts_src):
        with open(ts_src, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(os.path.join(ts_target, 'SKILL.md'), 'w', encoding='utf-8') as f:
            f.write("# TaskSync Protocol\n\nProtocol for cross-agent task synchronization and state management.\n\n" + content)
        print("Converted TaskSync prompt to skill.")

def install():
    skills_dir = 'skills'
    if not os.path.exists(skills_dir):
        os.makedirs(skills_dir)
        
    for skill in SKILLS_TO_INSTALL:
        target_dir = os.path.join(skills_dir, skill['name'])
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            
        for f in skill['files']:
            src_file = os.path.join(skill['src'], f)
            if os.path.exists(src_file):
                shutil.copy(src_file, target_dir)
                print(f"Installed {skill['name']}/{f}")
            else:
                print(f"Source file not found: {src_file}")
    
    handle_conversions()

if __name__ == "__main__":
    install()
