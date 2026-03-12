import json
import re
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class LLMTagger:
    def __init__(self, config):
        self.backend = getattr(config, "LLM_BACKEND", "mock")
        self.openai_api_key = getattr(config, "OPENAI_API_KEY", "")
        self.openai_model = getattr(config, "OPENAI_MODEL", "gpt-4o-mini")
        self.anthropic_api_key = getattr(config, "ANTHROPIC_API_KEY", "")
        self.anthropic_model = getattr(config, "ANTHROPIC_MODEL", "claude-3-haiku-20240307")
        self.ollama_base_url = getattr(config, "OLLAMA_BASE_URL", "http://localhost:11434")
        self.ollama_model = getattr(config, "OLLAMA_MODEL", "llama3")

    def _build_prompt(self, title: str, description: str, url: str) -> str:
        return (
            "Given this webpage, return a JSON array of 5-10 relevant tags "
            "(lowercase, single words or short phrases). "
            f"Title: {title}. Description: {description}. URL: {url}. "
            "Return only valid JSON array."
        )

    def _parse_response(self, text: str) -> list[str]:
        """Extract a JSON array of strings from LLM response text."""
        if not text:
            return []
        # Try direct parse first
        try:
            result = json.loads(text.strip())
            if isinstance(result, list):
                return [str(t).strip().lower() for t in result if t]
        except json.JSONDecodeError:
            pass
        # Try to find a JSON array in the text
        match = re.search(r"\[.*?\]", text, re.DOTALL)
        if match:
            try:
                result = json.loads(match.group())
                if isinstance(result, list):
                    return [str(t).strip().lower() for t in result if t]
            except json.JSONDecodeError:
                pass
        return []

    def _mock_tags(self, title: str, description: str, url: str) -> list[str]:
        """Generate tags from URL/title keywords without calling any external API."""
        tags = set()
        combined = f"{url} {title} {description}".lower()

        keyword_map = {
            "github": "github", "git": "version-control", "code": "programming",
            "python": "python", "javascript": "javascript", "js": "javascript",
            "typescript": "typescript", "react": "react", "vue": "vue",
            "flask": "flask", "django": "django", "node": "nodejs",
            "css": "css", "html": "html", "sql": "database",
            "news": "news", "blog": "blog", "article": "article",
            "video": "video", "youtube": "video", "tutorial": "tutorial",
            "docs": "documentation", "documentation": "documentation",
            "api": "api", "rest": "api", "graphql": "api",
            "machine learning": "machine-learning", "ml": "machine-learning",
            "ai": "artificial-intelligence", "data": "data",
            "cloud": "cloud", "aws": "aws", "azure": "azure", "gcp": "gcp",
            "linux": "linux", "docker": "docker", "kubernetes": "kubernetes",
            "security": "security", "crypto": "cryptography",
            "finance": "finance", "stock": "finance", "invest": "finance",
            "health": "health", "science": "science", "research": "research",
            "design": "design", "ux": "ux", "ui": "design",
            "tool": "tools", "productivity": "productivity",
            "open source": "open-source", "opensource": "open-source",
        }
        for keyword, tag in keyword_map.items():
            if keyword in combined:
                tags.add(tag)

        # Extract domain as a tag
        domain_match = re.search(r"https?://(?:www\.)?([^/]+)", url)
        if domain_match:
            domain = domain_match.group(1).split(".")[0]
            if len(domain) > 2:
                tags.add(domain)

        result = sorted(tags)[:8] if tags else ["bookmark", "web"]
        return result

    def get_tags(self, title: str, description: str, url: str) -> list[str]:
        """Return a list of tag strings for the given page info."""
        try:
            if self.backend == "mock":
                return self._mock_tags(title, description, url)
            elif self.backend == "openai":
                return self._openai_tags(title, description, url)
            elif self.backend == "anthropic":
                return self._anthropic_tags(title, description, url)
            elif self.backend == "ollama":
                return self._ollama_tags(title, description, url)
            else:
                logger.warning("Unknown LLM backend '%s', using mock", self.backend)
                return self._mock_tags(title, description, url)
        except Exception as exc:
            logger.error("LLM tagging failed: %s", exc)
            return []

    def _openai_tags(self, title: str, description: str, url: str) -> list[str]:
        from openai import OpenAI
        client = OpenAI(api_key=self.openai_api_key)
        prompt = self._build_prompt(title, description, url)
        response = client.chat.completions.create(
            model=self.openai_model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.3,
        )
        text = response.choices[0].message.content or ""
        return self._parse_response(text)

    def _anthropic_tags(self, title: str, description: str, url: str) -> list[str]:
        import anthropic
        client = anthropic.Anthropic(api_key=self.anthropic_api_key)
        prompt = self._build_prompt(title, description, url)
        message = client.messages.create(
            model=self.anthropic_model,
            max_tokens=200,
            messages=[{"role": "user", "content": prompt}],
        )
        text = message.content[0].text if message.content else ""
        return self._parse_response(text)

    def _ollama_tags(self, title: str, description: str, url: str) -> list[str]:
        import requests
        prompt = self._build_prompt(title, description, url)
        payload = {"model": self.ollama_model, "prompt": prompt, "stream": False}
        resp = requests.post(
            f"{self.ollama_base_url}/api/generate",
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        text = resp.json().get("response", "")
        return self._parse_response(text)
