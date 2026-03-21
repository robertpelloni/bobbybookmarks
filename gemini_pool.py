import os
import re
import time

import google.generativeai as genai


DEFAULT_GEMINI_MODELS = [
    "models/gemini-flash-latest",
    "models/gemini-flash-lite-latest",
    "models/gemini-3-flash-preview",
]


def stringify_field(value):
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, (list, tuple, set)):
        parts = [str(item).strip() for item in value if str(item).strip()]
        return ", ".join(parts)
    return str(value)


class GeminiModelPool:
    def __init__(self, logger=None, default_models=None, sleep_seconds=30):
        self.logger = logger
        self.sleep_seconds = sleep_seconds
        self.models = self._load_models(default_models or DEFAULT_GEMINI_MODELS)
        self.model_cache = {}
        self.active_model_index = 0

        api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        genai.configure(api_key=api_key)

    def _log(self, level, message):
        if self.logger and hasattr(self.logger, level):
            getattr(self.logger, level)(message)

    def _summarize_error(self, error):
        message = " ".join(str(error).split())
        return message[:240]

    def _extract_retry_seconds(self, error):
        message = str(error)
        for pattern in (
            r"retry in ([0-9]+(?:\.[0-9]+)?)s",
            r"retry_delay\s*\{\s*seconds:\s*([0-9]+)",
        ):
            match = re.search(pattern, message, flags=re.IGNORECASE | re.DOTALL)
            if match:
                return max(self.sleep_seconds, int(float(match.group(1))) + 1)
        return self.sleep_seconds

    def _load_models(self, default_models):
        configured = []
        preferred = os.environ.get("GEMINI_MODEL")
        if preferred:
            configured.append(preferred.strip())

        raw_models = os.environ.get("GEMINI_MODELS")
        if raw_models:
            configured.extend(model.strip() for model in raw_models.split(",") if model.strip())

        if not configured:
            configured = list(default_models)

        deduped = []
        for model_name in configured:
            if model_name not in deduped:
                deduped.append(model_name)
        return deduped

    def get_model(self, model_name):
        if model_name not in self.model_cache:
            self.model_cache[model_name] = genai.GenerativeModel(model_name)
        return self.model_cache[model_name]

    def generate_content(self, prompt, context_label):
        last_error = None
        for offset in range(len(self.models)):
            model_index = (self.active_model_index + offset) % len(self.models)
            model_name = self.models[model_index]
            try:
                response = self.get_model(model_name).generate_content(prompt)
                if model_index != self.active_model_index:
                    self._log("info", f"Switching Gemini model to {model_name}")
                self.active_model_index = model_index
                return response, model_name
            except Exception as e:
                last_error = e
                message = self._summarize_error(e)
                lowered = message.lower()
                if "429" in message or "quota" in lowered or "resourceexhausted" in lowered:
                    self._log("warning", f"Quota hit on {model_name} while {context_label}. Trying next model.")
                    continue
                if "not found" in lowered or "not supported" in lowered:
                    self._log("error", f"Gemini model {model_name} is unavailable while {context_label}: {e}")
                    continue
                self._log("error", f"Gemini request failed while {context_label} using {model_name}: {e}")
                continue

        if last_error:
            self._log("warning", f"Last Gemini failure while {context_label}: {self._summarize_error(last_error)}")
        sleep_seconds = self._extract_retry_seconds(last_error) if last_error else self.sleep_seconds
        self._log("warning", f"All Gemini models are currently unavailable while {context_label}. Sleeping {sleep_seconds}s before retry.")
        time.sleep(sleep_seconds)
        return None, None
