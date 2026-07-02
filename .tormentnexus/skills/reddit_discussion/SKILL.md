---
name: Reddit/Forum Discussion Analysis
description: Analyzes forum threads to extract community consensus and tool recommendations.
category: Community Intelligence
tags:
  - forum
  - reddit
  - hackernews
  - discussion
version: 1.0.0
---

# Reddit/Forum Discussion Analysis Skill

## Objective
To synthesize community discussions into consensus views, extracting real-world experiences and tool recommendations.

## Triggers
Activates on domains like `reddit.com`, `news.ycombinator.com`, and forum software (`discourse`).

## Execution Strategy
1. **Identify Consensus:** Look for highly upvoted comments or repeated sentiments across multiple users.
2. **Extract Warnings/Gotchas:** Highlight specific edge cases or problems users experienced in production.
3. **Collate Recommendations:** List alternative tools suggested by the community compared to the original topic.

## Prompt Modifiers for LLM
- Focus on: consensus opinions, novel approaches mentioned, real-world experiences
- Extract: tools recommended, patterns discussed, warnings given
- Prioritize: community-validated insights over individual claims
