---
name: GitHub Repository Analysis
description: Analyzes a github repository to extract key features, innovation score, and categorization.
category: Code Analysis
tags:
  - github
  - code
  - repository
version: 1.0.0
---

# GitHub Repository Analysis Skill

## Objective
To extract high-quality, normalized information from a GitHub repository README and source structure to classify the tool effectively into the Borg Atlas.

## Triggers
This skill activates whenever a `github.com` URL is passed into the pipeline.

## Execution Strategy
1. **Fetch & Clean:** Retrieve the `README.md`. Strip out badges, contributor lists, and table of contents to focus on the core descriptions.
2. **Feature Extraction:** Do not just list "Open Source". Extract the *core architectural features* (e.g. "Uses AST parsing for deterministic type generation", "Implements zero-copy memory buffers").
3. **Innovation Scoring:**
   * Baseline = 5.
   * If it implements a completely novel algorithm not seen in other repos -> +2
   * If it is a wrapper around an existing tool without new features -> -2

## Prompt Modifiers for LLM
- Focus on: stars, language, last commit date, README quality
- Extract: primary use case, key dependencies, API surface
- Prioritize: how this differs from alternatives in the same space

## Output Schema
Ensure output complies with the standard atlas entry JSON structure.
