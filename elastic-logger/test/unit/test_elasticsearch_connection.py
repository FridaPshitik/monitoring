from unittest.mock import MagicMock
from src.infinity_elastic_logs.elasticsearch_connection import ElasticsearchConnection, INDEX
import pytest


def test_connect_elasticsearch(elasticsearch_connection: ElasticsearchConnection):
    elasticsearch_connection.connect_elasticsearch = MagicMock(return_value=True)
    result = elasticsearch_connection.connect_elasticsearch()
    assert result == True
    
def test_connect_elasticsearch_false(elasticsearch_connection: ElasticsearchConnection):
    elasticsearch_connection._ElasticsearchConnection__check_connection = MagicMock(return_value=False)
    result = elasticsearch_connection.connect_elasticsearch()
    assert result == False


def test_is_active_connection_success(
    elasticsearch_connection: ElasticsearchConnection,
):
    elasticsearch_connection.connect_elasticsearch = MagicMock(return_value=True)
    elasticsearch_connection.is_connected = True
    assert elasticsearch_connection.is_active_connection() == True


def test__check_connection_success(
    sender: ElasticsearchConnection, mock_es_instance: MagicMock
):
    mock_es_instance.ping.return_value = True

    assert sender._ElasticsearchConnection__check_connection() == True


def test__check_connection_not_sucess(
    sender: ElasticsearchConnection, mock_es_instance: MagicMock
):
    mock_es_instance.ping.return_value = False
    assert sender._ElasticsearchConnection__check_connection() == False


def test_send_log_to_elastic_success(
    elasticsearch_connection: ElasticsearchConnection, log: dict[str, str]
):
    elasticsearch_connection.elasticsearch = MagicMock()
    elasticsearch_connection.is_active_connection = MagicMock(return_value=True)
    elasticsearch_connection.elasticsearch.index.return_value = {"result": "created"}

    elasticsearch_connection.send_log_to_elastic(log)
    elasticsearch_connection.elasticsearch.index.assert_called_once_with(
        index=INDEX, document=log
    )


def test_send_log_to_elastic_not_success(
    sender: ElasticsearchConnection, mock_es_instance: MagicMock
):
    mock_es_instance.ping.return_value = True
    with pytest.raises(Exception) as excexption:
        sender.send_log_to_elastic("not send")
        assert str(excexption.value) == "Exception: The log was not sent"


def test_get_elasticsearch_instance(sender: ElasticsearchConnection):
    elasticsearch = sender.get_elasticsearch_instance()
    assert elasticsearch == sender.elasticsearch
