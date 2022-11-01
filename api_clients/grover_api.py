import requests
from utils.queries import *


class GroverAPIClient:

    GROVER_API = "https://grover-staging.graphcdn.app/"

    def get_store_collection(self):
        return requests.get(self.GROVER_API, params={"query": get_store_collection})

    def get_store_by_id(self, _id: int):
        return requests.get(self.GROVER_API, params={"query": get_by_id.format(_id)})

    def bad_query(self):
        return requests.get(self.GROVER_API, params={"query": invalid_query})

    def crash_server(self):
        return requests.get(self.GROVER_API, params={"query": crash_srv})
