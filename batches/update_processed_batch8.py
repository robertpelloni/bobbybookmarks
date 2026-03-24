
import os

links = [
    ('https://github.com/omdivyatej/Self-Learning-Agents', 'AI Agents & Frameworks', 'Self-Learning Agents (dead-simple)', 'A lightweight Python library enabling LLM agents to improve through a feedback-in-prompt loop, using task embeddings to retrieve and inject relevant past corrections.', 'self-learning, feedback-loop, rag-memory, python', 'Task Embeddings, Local JSON Storage, Prompt Injection, Judge-based Filtering.'),
    ('https://www.reddit.com/r/ClaudeAI/comments/1pcu6wy/i_built_a_self_learning_agent_that_updates_its/', 'Guides & Articles', 'Self-Learning Agent Discussion', 'Reddit community discussion on the practical implementation of feedback-driven agentic memory to prevent regression and repeated mistakes.', 'reddit, discussion, agent-memory, self-learning', 'Error Analysis, Feedback Loops, Regressive Mistake prevention.'),
    ('https://github.com/anthropics/claude-agent-sdk-typescript/tree/main/packages/sdk/src/hooks', 'AI Agents & Frameworks', 'Claude Agent SDK Hook System (TS)', 'The core interceptor system for the TypeScript SDK, allowing developers to programmatically approve, deny, or modify agent actions before and after tool use.', 'anthropic, hooks, security, guardrails', 'PreToolUse, PostToolUse, OnEvent, OnError, Async Execution.'),
    ('https://github.com/anthropics/claude-agent-sdk-python/tree/main/src/claude_agent_sdk/hooks', 'AI Agents & Frameworks', 'Claude Agent SDK Hook System (Py)', 'The Python implementation of the hook system, providing lifecycle triggers for monitoring and controlling autonomous agent behaviors.', 'anthropic, python, hooks, guardrails', 'PreToolUse implementation, Event Auditing, Error Interception, Tool Authorization.')
]

with open('processed.txt', 'a', encoding='utf-8') as f:
    for link in links:
        f.write(f'{link[0]}, {link[1]}, {link[2]}, {link[3]}, {link[4]}, {link[5]}\n')
