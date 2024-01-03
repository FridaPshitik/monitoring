from unittest.mock import MagicMock, patch, mock_open
from src.infinity_elastic_logs.elasticsearch_local_logs_sender import ElasticSearchLocalLogsSender, INDEX
from elasticsearch.helpers import bulk
import os
import pytest


@pytest.mark.parametrize(
    "file_exists, file_size, expected_result",
    [(True, 100, True), (False, 0, False), (True, 0, False)],
)
def test_is_failed_log_file_contain_logs(
    elasticsearch_local_logs_sender: ElasticSearchLocalLogsSender,
    file_exists,
    file_size,
    expected_result,
):
    os_mock = MagicMock()
    os_mock.path.exists.return_value = file_exists
    os_mock.stat.return_value.st_size = file_size

    with patch("os.path", os_mock.path):
        with patch("os.stat", os_mock.stat):
            assert (
                elasticsearch_local_logs_sender._ElasticSearchLocalLogsSender__is_failed_log_file_contain_logs()
                == expected_result
            )


def test_clean_failed_log_file(
    elasticsearch_local_logs_sender: ElasticSearchLocalLogsSender,
):
    elasticsearch_local_logs_sender.path = "test_log.txt"
    with open("test_log.txt", "w") as f:
        f.write("some")

    elasticsearch_local_logs_sender._ElasticSearchLocalLogsSender__clean_failed_log_file()

    with open("test_log.txt", "r") as f:
        content = f.read()

    assert content == ""
    os.remove("test_log.txt")


def test_write_local_logs_to_elastic(
    elasticsearch_local_logs_sender: ElasticSearchLocalLogsSender,
):
    mock_elastic_search_connection = MagicMock()
    with patch("builtins.open", mock_open(read_data="log1\nlog2\nlog3\n")) as mock_file:
        with patch("src.infinity_elastic_logs.elasticsearch_local_logs_sender.bulk", wraps=bulk) as mock_bulk:
            elasticsearch_local_logs_sender._ElasticSearchLocalLogsSender__write_local_logs_to_elastic(
                mock_elastic_search_connection
            )
            mock_bulk.assert_called_once_with(
                mock_elastic_search_connection,
                [
                    {"_index": INDEX, "_source": "log1"},
                    {"_index": INDEX, "_source": "log2"},
                    {"_index": INDEX, "_source": "log3"},
                ],
            )
        mock_file.assert_called_once_with(elasticsearch_local_logs_sender.path)
