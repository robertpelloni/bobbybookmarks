from unittest.mock import patch

from worker_status import build_status, clean_url, parse_log_lines


class TestWorkerStatusHelpers:
    def test_clean_url_strips_trailing_punctuation(self):
        assert clean_url("https://example.com/test).") == "https://example.com/test"

    def test_parse_log_lines_extracts_active_url_sleep_and_last_success(self):
        lines = [
            "2026-03-21 00:40:31,213 - INFO - Borg Intelligence Extracted: https://docs.anythingllm.com/agent/custom/plugin-json",
            "2026-03-21 00:48:00,465 - WARNING - All Gemini models are currently unavailable while researching https://gist.github.com/gc-victor/abc123. Sleeping 59s before retry.",
        ]

        state = parse_log_lines(lines)

        assert state["last_timestamp"] == "2026-03-21 00:48:00,465"
        assert state["active_url"] == "https://gist.github.com/gc-victor/abc123"
        assert state["last_extracted_url"] == "https://docs.anythingllm.com/agent/custom/plugin-json"
        assert state["sleep_seconds"] == 59


class TestBuildStatus:
    def test_build_status_marks_backing_off(self):
        log_state = {
            "last_timestamp": "2026-03-21 00:48:00,465",
            "last_message": "WARNING - All Gemini models are currently unavailable while researching https://example.com. Sleeping 59s before retry.",
            "active_url": "https://example.com",
            "last_extracted_url": None,
            "sleep_seconds": 59,
        }
        with patch("worker_status.get_worker_process", return_value={"pid": 123, "name": "python.exe", "command_line": "python .\\deep_research.py"}), patch("worker_status.get_progress", return_value={"borg_rows": 10, "total_urls": 20, "remaining_urls": 10}), patch("worker_status.get_recent_log_state", return_value=log_state), patch("worker_status.get_worker_heartbeat", return_value=None):
            status = build_status()

        assert status["worker_running"] is True
        assert status["state"] == "backing_off"

    def test_build_status_marks_stopped_without_process(self):
        with patch("worker_status.get_worker_process", return_value=None), patch("worker_status.get_progress", return_value={"borg_rows": 10, "total_urls": 20, "remaining_urls": 10}), patch("worker_status.get_recent_log_state", return_value=parse_log_lines([])), patch("worker_status.get_worker_heartbeat", return_value=None):
            status = build_status()

        assert status["worker_running"] is False
        assert status["state"] == "stopped"

    def test_build_status_prefers_heartbeat_fields(self):
        heartbeat = {
            "updated_at": "2026-03-21T05:00:00Z",
            "state": "backing_off",
            "active_url": "https://example.com/current",
            "last_extracted_url": "https://example.com/done",
            "sleep_seconds": 42,
        }
        with patch("worker_status.get_worker_process", return_value={"pid": 123, "name": "python.exe", "command_line": "python .\\deep_research.py"}), patch("worker_status.get_progress", return_value={"borg_rows": 10, "total_urls": 20, "remaining_urls": 10}), patch("worker_status.get_recent_log_state", return_value=parse_log_lines([])), patch("worker_status.get_worker_heartbeat", return_value=heartbeat):
            status = build_status()

        assert status["state"] == "backing_off"
        assert status["log_state"]["active_url"] == "https://example.com/current"
        assert status["log_state"]["last_extracted_url"] == "https://example.com/done"
        assert status["log_state"]["sleep_seconds"] == 42
