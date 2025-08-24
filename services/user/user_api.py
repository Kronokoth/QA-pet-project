import allure
import requests
from services.user.user_endpoints import Endpoints
from services.user.user_payloads import Payloads

class UserAPI:
    def __init__(self):
        self.payloads = Payloads()
        self.endpoints = Endpoints()

    @allure.step("Create user")
    def create_user(self):
        url = self.endpoints.create_user
        json_data = self.payloads.base_user_payload
        response = requests.post(url=url, json=json_data)
        assert response.status_code == 200
        response_json = response.json()

        return response_json, json_data

    @allure.step("Get user by username")
    def get_user_by_username(self, username):
        response = requests.get(
            url=self.endpoints.get_user(username),
        ).json()
        assert response['username'] == username
        return response

    @allure.step("Delete user")
    def delete_user(self, username):
        response = requests.delete(
            url=self.endpoints.delete_user(username),
        )
        assert response.status_code == 200
        return response