---
name: Technical Blog Analysis
description: Analyzes technical blog posts and articles for actionable developer insights.
category: Technical Reading
tags:
  - blog
  - article
  - tutorial
version: 1.0.0
---

# Technical Blog Analysis Skill

## Objective
To extract practical, actionable insights, tools, and architecture decisions from technical blog posts and articles.

## Triggers
Activates on common blogging platforms (`medium.com`, `dev.to`, `hashnode`, `substack.com`) and paths (`/blog/`).

## Execution Strategy
1. **Filter Fluff:** Ignore introductory anecdotes or marketing speak. Zero in on the technical implementation details.
2. **Identify Tooling:** List all specific libraries, frameworks, or tools explicitly mentioned as part of the solution.
3. **Extract Decisions:** Why did the author choose approach A over approach B?

## Prompt Modifiers for LLM
- Focus on: key takeaways, practical code examples, architecture decisions
- Extract: techniques described, tools mentioned, lessons learned
- Prioritize: actionable insights a developer can apply today
