import os
from unittest.mock import MagicMock, patch

import pytest

from gemini_pool import GeminiModelPool, stringify_field


class TestStringifyField:
    def test_returns_empty_string_for_none(self):
        assert stringify_field(None) == ""

    def test_returns_string_as_is(self):
        assert stringify_field("hello") == "hello"

    def test_joins_list_values(self):
        assert stringify_field(["alpha", "beta", "gamma"]) == "alpha, beta, gamma"

    def test_coerces_other_values_to_string(self):
        assert stringify_field(42) == "42"


class TestGeminiModelPool:
    def test_extract_retry_seconds_from_retry_in_hint(self):
        pool = GeminiModelPool(logger=MagicMock(), sleep_seconds=30)
        err = Exception("Please retry in 45.2s.")
        assert pool._extract_retry_seconds(err) == 46

    def test_extract_retry_seconds_from_retry_delay_block(self):
        pool = GeminiModelPool(logger=MagicMock(), sleep_seconds=30)
        err = Exception("retry_delay { seconds: 59 }")
        assert pool._extract_retry_seconds(err) == 60

    def test_extract_retry_seconds_respects_minimum_sleep(self):
        pool = GeminiModelPool(logger=MagicMock(), sleep_seconds=30)
        err = Exception("Please retry in 5s.")
        assert pool._extract_retry_seconds(err) == 30

    def test_generate_content_falls_back_to_next_model_on_quota(self):
        logger = MagicMock()
        with patch.dict(os.environ, {"GEMINI_MODELS": "model-a,model-b"}, clear=False):
            pool = GeminiModelPool(logger=logger, sleep_seconds=30)

        first_model = MagicMock()
        second_model = MagicMock()
        second_response = MagicMock()
        second_response.text = "OK"

        first_model.generate_content.side_effect = Exception("429 quota exceeded")
        second_model.generate_content.return_value = second_response

        with patch.object(pool, "get_model", side_effect=[first_model, second_model]):
            response, model_name = pool.generate_content("prompt", "testing fallback")

        assert response is second_response
        assert model_name == "model-b"
        assert pool.active_model_index == 1
        logger.warning.assert_called_with("Quota hit on model-a while testing fallback. Trying next model.")
        logger.info.assert_called_with("Switching Gemini model to model-b")

    def test_generate_content_sleeps_when_all_models_exhausted(self):
        logger = MagicMock()
        with patch.dict(os.environ, {"GEMINI_MODELS": "model-a,model-b"}, clear=False):
            pool = GeminiModelPool(logger=logger, sleep_seconds=30)

        quota_error = Exception("Please retry in 45s.")
        exhausted_model = MagicMock()
        exhausted_model.generate_content.side_effect = quota_error

        with patch.object(pool, "get_model", side_effect=[exhausted_model, exhausted_model]), patch("gemini_pool.time.sleep") as sleep_mock:
            response, model_name = pool.generate_content("prompt", "testing exhaustion")

        assert response is None
        assert model_name is None
        sleep_mock.assert_called_once_with(46)
        logger.warning.assert_any_call("All Gemini models are currently unavailable while testing exhaustion. Sleeping 46s before retry.")

