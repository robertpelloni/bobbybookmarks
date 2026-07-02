---
name: Research Paper Analysis
description: Analyzes research papers (like arXiv) to extract methodology and benchmarks.
category: Research Reading
tags:
  - paper
  - research
  - arxiv
version: 1.0.0
---

# Research Paper Analysis Skill

## Objective
To distill academic and technical research papers into their core contributions, methodologies, and benchmark results for ingestion into the Atlas.

## Triggers
This skill activates for domains typically hosting papers, such as `arxiv.org`, `paperswithcode.com`, or URLs containing `/paper/`.

## Execution Strategy
1. **Focus Area:** Identify the "Abstract", "Methodology", and "Results/Conclusion" sections.
2. **Extraction:** Determine the specific novel technique being introduced. What existing method is it compared against, and by what margin does it improve?
3. **Limitation Check:** Extract any noted limitations or future work to ensure balanced representation.

## Prompt Modifiers for LLM
- Focus on: novel technique, benchmark results, key insight
- Extract: methodology, evaluation metrics, limitations
- Prioritize: what breakthrough or improvement this represents
