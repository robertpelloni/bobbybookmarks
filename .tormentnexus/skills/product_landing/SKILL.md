---
name: Product/Tool Landing Page
description: Default fallback to extract value propositions from product landing pages.
category: Product Analysis
tags:
  - product
  - landing-page
  - marketing
version: 1.0.0
---

# Product/Tool Landing Page Skill

## Objective
To parse marketing and landing pages to determine the actual technical capabilities and target audience of a product.

## Triggers
This is the default fallback skill when no other specific domain matches.

## Execution Strategy
1. **De-jargonize:** Translate marketing buzzwords (e.g., "synergistic AI copilot") into technical realities (e.g., "LLM wrapper with vector search").
2. **Identify Integrations:** What ecosystems does this tool natively plug into?
3. **Core Value Prop:** What is the primary problem this product claims to solve?

## Prompt Modifiers for LLM
- Focus on: core value proposition, pricing model, integrations
- Extract: key features, target audience, competitive advantages
- Prioritize: what specific problem this solves and how
