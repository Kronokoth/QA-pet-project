from faker import Faker

fake = Faker()

class Payloads:

    base_user_payload = {
      "id": 0,
      "username": fake.user_name(),
      "firstName": fake.first_name(),
      "lastName": fake.last_name(),
      "email": fake.email(),
      "password": fake.password(),
      "phone": fake.phone_number(),
      "userStatus": 0
    }

    create_with_list_or_array = [
      {
        "id": 0,
        "username": fake.user_name(),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.phone_number(),
        "userStatus": 0
      }
    ]