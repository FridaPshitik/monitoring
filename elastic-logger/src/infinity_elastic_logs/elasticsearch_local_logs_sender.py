from .local_logs_writer import LocalLogsWriter
import os
from dotenv import load_dotenv
from elasticsearch.helpers import bulk

load_dotenv()
INDEX = os.environ["INDEX"]


class ElasticSearchLocalLogsSender:
    def __init__(self) -> None:
        self.path = LocalLogsWriter().path

    def send_local_logs_to_elastic(self, elastic_search_connection):
        if self.__is_failed_log_file_contain_logs():
            self.__write_local_logs_to_elastic(elastic_search_connection)
            self.__clean_failed_log_file()

    def __is_failed_log_file_contain_logs(self):
        return os.path.exists(self.path) and os.stat(self.path).st_size > 0

    def __write_local_logs_to_elastic(self, elastic_search_connection):
        bulk_data = []
        with open(self.path) as log_file:
            for row in log_file:
                bulk_data.append({"_index": INDEX, "_source": row.strip()})
        bulk(elastic_search_connection, bulk_data)

    def __clean_failed_log_file(self):
        open(self.path, "w").close()
