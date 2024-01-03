"""
    conftest.py for infinity_elastic_logs.
"""

import pytest
from unittest import mock


@pytest.fixture(scope="session")
def elastic_logger():
    from src.infinity_elastic_logs.elastic_logger import ElasticLogger

    elastic_logger = ElasticLogger("test-service")
    yield elastic_logger

@pytest.fixture
def local_logs_writer():
    from src.infinity_elastic_logs.local_logs_writer import LocalLogsWriter

    local_logs_writer = LocalLogsWriter()
    yield local_logs_writer


@pytest.fixture
def elastic_search_sender():
    from src.infinity_elastic_logs.elasticsearch_sender import ElasticSearchSender

    elastic_search_sender = ElasticSearchSender()
    yield elastic_search_sender


@pytest.fixture
def log():
    from datetime import datetime

    log_json = {
        "timestamp": f"{datetime.now().isoformat()}",
        "message": "Test message",
        "level": "DEBUG",
        "service": "test-service",
    }
    return log_json


@pytest.fixture
def mock_es_instance():
    from unittest.mock import MagicMock

    return MagicMock()


@pytest.fixture
def sender(mock_es_instance):
    from src.infinity_elastic_logs.elasticsearch_connection import ElasticsearchConnection

    sender = ElasticsearchConnection()
    sender.elasticsearch = mock_es_instance
    yield sender


@pytest.fixture
def elasticsearch_connection():
    from src.infinity_elastic_logs.elasticsearch_connection import ElasticsearchConnection

    yield ElasticsearchConnection()


@pytest.fixture
def elasticsearch_local_logs_sender():
    from src.infinity_elastic_logs.elasticsearch_local_logs_sender import ElasticSearchLocalLogsSender

    yield ElasticSearchLocalLogsSender()


@pytest.fixture
def mock_elastic_search_connection():
    return mock.Mock()
