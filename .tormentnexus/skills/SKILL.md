---
name: "Template Extraction Skill"
description: "Base template for all extraction and task resolution strategies."
category: "extraction"
tags: ["template", "base"]
version: "1.0.0"
---

# Execution Strategy
Describe the exact prompt layout and logic required to execute this skill.

# Success Signals
- Identify the explicit signals that confirm this skill operated correctly.

# Failure Signals
- Identify output strings or patterns that indicate failure.

# Auto-Retirement Criteria
- If win-rate < 0.3 over 50 executions, mark as `retired`.
