import os
from dotenv import load_dotenv

load_dotenv()

class Headers:
    PET_STORE_API_KEY = os.getenv('PET_STORE_API_KEY')

    def pet_store_api_key_headers(self):
        return {"api_key": self.PET_STORE_API_KEY}