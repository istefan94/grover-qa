import requests


class ChuckAPIClient:

    _CN_API = "https://api.chucknorris.io/jokes"
    CN_RANDOM_ENDPOINT = f"{_CN_API}/random"
    METHODS = ["get", "post", "put", "patch", "delete"]

    def get_random_joke(self):
        return requests.get(self.CN_RANDOM_ENDPOINT)

    def get_joke_by_id(self, joke_id: str):
        return requests.get(f"{self._CN_API}/{joke_id}")
