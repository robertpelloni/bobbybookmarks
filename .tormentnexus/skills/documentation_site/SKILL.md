---
name: Documentation/API Site Analysis
description: Analyzes technical documentation to extract the value proposition and core primitives.
category: Technical Reading
tags:
  - docs
  - api
  - reference
version: 1.0.0
---

# Documentation Site Analysis Skill

## Objective
To understand the core primitives, API surface, and use cases of a tool based on its published documentation.

## Triggers
This skill activates for URLs containing `docs.`, `/docs/`, `/api/`, or `/guide/`.

## Execution Strategy
1. **Targeting:** Focus on the "Getting Started", "Concepts", or "Architecture" pages rather than deep endpoint references.
2. **Extraction:** Identify the core problem the API solves. What are the key objects/nouns in the system?
3. **Differentiation:** How does this API differ from standard REST/GraphQL paradigms in its space?

## Prompt Modifiers for LLM
- Focus on: API endpoints, authentication model, rate limits
- Extract: key abstractions, data models, extension points
- Prioritize: what makes this API/service unique

## Verification
Ensure the extracted `SHORT_DESCRIPTION` clearly states *what* the developer can do with the API, not just *that* it's an API.
