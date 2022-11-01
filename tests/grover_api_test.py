from api_clients.grover_api import *
import pycountry
from utils import currency


class TestGroverAPI:

    client = GroverAPIClient()

    def test_get_store_success(self):
        response = self.client.get_store_by_id(1)
        response_json = response.json()

        assert response.status_code == 200
        assert isinstance(response_json["data"], dict)
        assert isinstance(response_json["data"]["store"], dict)
        assert isinstance(response_json["data"]["store"]["alternativeLocales"], list)
        assert response_json["data"]["store"]["defaultCurrency"] != ""
        assert response_json["data"]["store"]["code"] != ""
        assert response_json["data"]["store"]["defaultLocale"] != ""

    def test_store_currency_is_correct(self):
        response = self.client.get_store_collection()
        response_json = response.json()

        assert response.status_code == 200

        stores = response_json["data"]["storeCollection"]["nodes"]

        for store in stores:
            country = pycountry.countries.get(alpha_2=store["code"])
            assert country is not None, f"Invalid country code for store with id {store['id']}"
            assert currency.codes[country.alpha_2.lower()] == store["defaultCurrency"].lower(), \
                f"Invalid currency for store with id {store['id']}"

    def test_invalid_query(self):
        response = self.client.bad_query()

        assert response.status_code == 400

    def test_crash(self):
        response = self.client.crash_server()

        assert response.status_code == 200
        assert response.json()["errors"][0]["message"] == "500: Internal Server Error"
