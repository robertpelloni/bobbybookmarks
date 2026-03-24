import os
import shutil

SKILLS_TO_INSTALL = [
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
    }
]

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

if __name__ == "__main__":
    install()
