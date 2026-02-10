import allure
import pytest

from services.user.user_api import UserAPI
@allure.epic("Administration")
@allure.feature("Users")
class TestUsers:

    @pytest.mark.users
    @allure.title("Create new user")
    # test
    def test_create_user(self):
        self.user_ap = UserAPI()
        return_user = self.user_api.create_user()
        username = return_user[1]['username']
        self.user_api.get_user_by_username(username)
        self.user_api.delete_user(username)


