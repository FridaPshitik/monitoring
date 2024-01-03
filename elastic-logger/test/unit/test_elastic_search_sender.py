from unittest.mock import MagicMock, patch
from src.infinity_elastic_logs.elasticsearch_sender import ElasticSearchSender


def test_send_log_to_elastic_success(
    elastic_search_sender: ElasticSearchSender, log: dict[str, str]
):
    elastic_search_sender.elasticsearch = MagicMock()
    elastic_search_sender.write_local_log = MagicMock()

    elastic_search_sender._ElasticSearchSender__send_log(log)
    elastic_search_sender.elasticsearch.send_log_to_elastic.assert_called_once_with(log)


def test_send_log_to_elastic_failure(
    elastic_search_sender: ElasticSearchSender, log: dict[str, str]
):
    elastic_search_sender.elasticsearch = MagicMock()
    elastic_search_sender.elasticsearch.send_log_to_elastic.side_effect = Exception(
        "Connection error"
    )

    elastic_search_sender.write_local_log = MagicMock()
    elastic_search_sender._ElasticSearchSender__send_log(log)
    elastic_search_sender.write_local_log.write_log_to_local.assert_called_once_with(
        log
    )


def test_send_local_to_elastic(elastic_search_sender: ElasticSearchSender):
    elastic_search_sender.local_to_elastic.send_local_logs_to_elastic = MagicMock()
    elastic_search_sender.elasticsearch = MagicMock()
    elastic_search_sender._ElasticSearchSender__send_local_to_elastic()
    elastic_search_sender.local_to_elastic.send_local_logs_to_elastic.assert_called_once_with(
        elastic_search_sender.elasticsearch.get_elasticsearch_instance()
    )
