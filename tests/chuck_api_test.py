from api_clients.chuck_norris_api import *
import random
import string


class TestChuckNorrisAPI:

    client = ChuckAPIClient()

    def test_get_random_joke_success(self):
        response = self.client.get_random_joke()
        response_body = response.json()

        assert response.status_code == 200

        assert isinstance(response_body["categories"], list)
        assert response_body["created_at"] != ""
        assert response_body["icon_url"] != ""
        assert response_body["id"] != ""
        assert response_body["updated_at"] != ""
        assert response_body["url"] != ""
        assert response_body["value"] != ""

    def test_get_joke_by_id_success(self):
        joke_id = "XMbEIozoTbCR6kwz_uJWeQ"  # randomly selected from multiple calls
        response = self.client.get_joke_by_id(joke_id)
        response_body = response.json()

        assert response.status_code == 200

        assert isinstance(response_body["categories"], list)
        assert response_body["created_at"] != ""
        assert response_body["icon_url"] != ""
        assert response_body["id"] != ""
        assert response_body["updated_at"] != ""
        assert response_body["url"] != ""
        assert response_body["value"] != ""

    def test_method_not_allowed(self):
        for method in self.client.METHODS:
            if method != "get":
                response = requests.request(method, self.client.CN_RANDOM_ENDPOINT)
                assert response.status_code == 405

    def test_get_joke_by_invalid_id(self):
        joke_id = "".join(random.choices(string.ascii_letters + string.digits, k=20)) + "GRV"
        response = self.client.get_joke_by_id(joke_id)
        response_body = response.json()

        assert response.status_code == 404

        assert response_body["timestamp"] != ""
        assert response_body["status"] == 404
        assert response_body["error"] == "Not Found"
        assert response_body["message"] == f"Joke with id \"{joke_id}\" not found."
        assert response_body["path"] == f"/jokes/{joke_id}"
