import pytest
from src.infinity_elastic_logs.local_logs_writer import LocalLogsWriter, DEFAULT_PATH
from unittest import mock
from unittest.mock import MagicMock
import json
import os
from dotenv import load_dotenv

load_dotenv()
FAILED_LOGS_FILE_PATH = os.getenv("FAILED_LOGS_FILE_PATH")


def test_write_log_to_local(local_logs_writer: LocalLogsWriter, log: dict[str, str]):
    mock_file = mock.mock_open()
    with mock.patch("builtins.open", mock_file):
        local_logs_writer.write_log_to_local(log)
    mock_file.assert_called_once_with(local_logs_writer.path, "a")
    mock_file().write.assert_called_once_with(f"{json.dumps(log)}\n")


@pytest.mark.parametrize(
    "is_path_exists, expected_result",
    [(True, FAILED_LOGS_FILE_PATH), (False, DEFAULT_PATH)],
)
def test_get_failed_log_path(
    local_logs_writer: LocalLogsWriter,
    is_path_exists: bool,
    expected_result,
):
    local_logs_writer._LocalLogsWriter__is_exists_failed_log_path = MagicMock(
        return_value=is_path_exists
    )
    result = local_logs_writer._LocalLogsWriter__get_failed_log_path()
    assert result == expected_result


def test_load_path_from_env(local_logs_writer: LocalLogsWriter):
    os.getenv = MagicMock(return_value="/path/to/failed_logs.log")
    path = local_logs_writer._LocalLogsWriter__load_path_from_env()
    assert path == "/path/to/failed_logs.log"
