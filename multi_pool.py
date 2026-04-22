import os
import time
import json
import requests

class MultiProviderPool:
    def __init__(self, logger=None):
        self.providers = []
        self.cooldowns = {}
        self.error_counts = {}
        self.active_index = 0
        self.logger = logger
        self.last_provider = None
        self.last_provider_name = None
        self.total_calls = 0
        self.total_errors = 0
        self._init_providers()

    def _init_providers(self):
        # 1. LM Studio (Local First)
        lm_url = os.environ.get('LMSTUDIO_URL', 'http://localhost:1234/v1/chat/completions')
        self.providers.append({
            'name': 'lmstudio-local',
            'endpoint': lm_url,
            'key': 'not-needed',
            'model': 'local-model'
        })

        # 2. OpenRouter (Free/Preferred)
        or_key = os.environ.get('OPENROUTER_API_KEY')
        if or_key:
            # Try free/low-cost models first
            free_models = [
                'google/gemma-4-26b-a4b-it:free',
                'nvidia/nemotron-3-super-120b-a12b:free',
                'qwen/qwen3-coder:free',
                'liquid/lfm-2.5-1.2b-thinking:free',
                'qwen/qwen3-next-80b-a3b-instruct:free',
                'inclusionai/ling-2.6-flash:free',
                'nvidia/nemotron-3-nano-30b-a3b:free',
                'openai/gpt-oss-120b:free',
                'google/gemma-4-31b-it:free',
                'minimax/minimax-m2.5:free',
            ]
            for m in free_models:
                self.providers.append({
                    'name': f'openrouter-{m.split("/")[1].split(":")[0]}',
                    'endpoint': 'https://openrouter.ai/api/v1/chat/completions',
                    'key': or_key,
                    'model': m
                })

        # 3. Other potential free services (Placeholder for integration)
        # cline/free, zen/free, kilo/free etc usually require specific endpoints/keys
        # We can add them as environment-configurable OpenRouter custom models or direct endpoints

        # 4. Specialized Free Tiers
        groq_key = os.environ.get('GROQ_API_KEY')
        if groq_key:
            self.providers.append({
                'name': 'groq-llama3-8b',
                'endpoint': 'https://api.groq.com/openai/v1/chat/completions',
                'key': groq_key,
                'model': 'llama3-8b-8192'
            })

        # 5. Last Resort: Gemini Flash (paid/standard)
        if or_key:
            self.providers.append({
                'name': 'openrouter-gemini-flash',
                'endpoint': 'https://openrouter.ai/api/v1/chat/completions',
                'key': or_key,
                'model': 'google/gemini-2.0-flash-001'
            })

        self.logger.info(f"LLM providers (ordered by priority): {[p['name'] for p in self.providers]}")

    def generate(self, prompt, context=None):
        self.total_calls += 1
        for offset in range(len(self.providers)):
            idx = (self.active_index + offset) % len(self.providers)
            p = self.providers[idx]
            until = self.cooldowns.get(p['name'])
            if until and time.time() < until:
                continue
            self.cooldowns.pop(p['name'], None)
            try:
                resp = requests.post(
                    p['endpoint'],
                    headers={'Authorization': f"Bearer {p['key']}", 'Content-Type': 'application/json'},
                    json={'model': p['model'], 'messages': [{'role': 'user', 'content': prompt + (chr(10)+chr(10)+context if context else '')}], 'max_tokens': 800, 'temperature': 0.3},
                    timeout=30,
                )
                if resp.status_code == 200:
                    text = resp.json().get('choices', [{}])[0].get('message', {}).get('content', '')
                    if text:
                        self.error_counts.pop(p['name'], None)
                        self.active_index = idx
                        self.last_provider = p['name']
                        return text, p['name']
                elif resp.status_code == 429:
                    wait = min(60 * (2 ** self.error_counts.get(p['name'], 0)), 300)
                    self.error_counts[p['name']] = self.error_counts.get(p['name'], 0) + 1
                    self.cooldowns[p['name']] = time.time() + wait
                    self.logger.warning(f"Rate limited {p['name']}, cooldown {wait}s")
                elif resp.status_code == 402:
                    self.cooldowns[p['name']] = time.time() + 3600
                    self.logger.warning(f"Balance exhausted: {p['name']}")
                else:
                    self.logger.error(f"{p['name']}: {resp.status_code}")
            except Exception as e:
                self.logger.error(f"{p['name']} error: {e}")
        self.total_errors += 1
        return None, None



