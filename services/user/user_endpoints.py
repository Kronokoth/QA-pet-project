
HOST = 'https://petstore.swagger.io/v2'

class Endpoints:

    create_user_with_list = f"{HOST}/user/createWithList"
    get_user = lambda self, username: f"{HOST}/user/{username}"
    update_user = lambda self, username: f"{HOST}/user/{username}"
    delete_user = lambda self, username: f"{HOST}/user/{username}"
    logs_user = lambda self, username: f"{HOST}/user/login"
    logs_out_user = lambda self, username: f"{HOST}/user/logout"
    create_user_with_array = f"{HOST}/user/createWithArray"
    create_user = f"{HOST}/user"

