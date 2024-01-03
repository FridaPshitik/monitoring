import threading
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv()
CLOUD_ID = os.environ["CLOUD_ID"]
NAME = os.environ["NAME"]
PASSWORD = os.environ["PASSWORD"]
INDEX = os.environ["INDEX"]

lock = threading.Lock()


class ElasticsearchConnection:
    def __init__(self) -> None:
        self.connect_elasticsearch()

    def connect_elasticsearch(self) -> bool:
        try:
            self.elasticsearch = self.init_elasticsearch()
            self.is_connected = self.__check_connection()
        except Exception as err:
            self.is_connected = False
            print(f"Exception: {err}")
        return self.is_connected

    def init_elasticsearch(self) -> Elasticsearch:
        try:
            elasticsearch = Elasticsearch(
                cloud_id=CLOUD_ID,
                basic_auth=(NAME, PASSWORD),
            )
        except:
            raise Exception(
                "Elasticsearch Connection authentication failed. Check the cloud ID, name and password"
            )
        return elasticsearch

    def __check_connection(self) -> bool:
        return self.elasticsearch.ping()

    def send_log_to_elastic(self, log):
        if self.is_active_connection() == False:
            raise Exception("Elasticsearch is not connected")
        res = self.elasticsearch.index(index=INDEX, document=log)
        if res["result"] != "created":
            raise Exception(f'Log was not sent. res = {res["result"]}')

    def is_active_connection(self) -> bool:
        if self.is_connected == False:
            self.connect_elasticsearch()
        return self.is_connected

    def get_elasticsearch_instance(self) -> Elasticsearch:
        return self.elasticsearch
