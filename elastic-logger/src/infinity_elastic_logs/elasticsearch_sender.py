import threading
from .elasticsearch_connection import ElasticsearchConnection
from .local_logs_writer import LocalLogsWriter
from .elasticsearch_local_logs_sender import ElasticSearchLocalLogsSender

lock = threading.Lock()


class ElasticSearchSender:
    def __init__(self) -> None:
        self.elasticsearch = ElasticsearchConnection()
        self.write_local_log = LocalLogsWriter()
        self.local_to_elastic = ElasticSearchLocalLogsSender()

    def send_log(self, log):
        thread = threading.Thread(target=self.__send_log(log))
        thread.start()

    def __send_log(self, log):
        with lock:
            try:
                self.elasticsearch.send_log_to_elastic(log)
                self.send_local_to_elastic()
            except:
                self.write_local_log.write_log_to_local(log)

    def send_local_to_elastic(self):
        thread = threading.Thread(target=self.__send_local_to_elastic)
        thread.start()

    def __send_local_to_elastic(self):
        with lock:
            try:
                self.local_to_elastic.send_local_logs_to_elastic(
                    self.elasticsearch.get_elasticsearch_instance()
                )
            except:
                print("send local logs to elastic failed")
