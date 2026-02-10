import allure
import requests
from services.user.user_endpoints import Endpoints
from services.user.user_payloads import Payloads
from config.headers import Headers

class UserAPI:
    def __init__(self):
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.pet_api_key = Headers().pet_store_api_key_headers()

    @allure.step("Create user")
    def create_user(self):
        url = self.endpoints.create_user
        json_data = self.payloads.base_user_payload
        response = requests.post(url=url, json=json_data, headers=self.pet_api_key)
        assert response.status_code == 200
        response_json = response.json()

        return response_json, json_data

    @allure.step("Get user by username")
    def get_user_by_username(self, username):
        response = requests.get(
            url=self.endpoints.get_user(username), headers=self.pet_api_key
        ).json()
        assert response['username'] == username
        return response

    @allure.step("Delete user")
    def delete_user(self, username):
        response = requests.delete(
            url=self.endpoints.delete_user(username), headers=self.pet_api_key
        )
        assert response.status_code == 200
        return response