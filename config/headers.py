import os
from dotenv import load_dotenv

load_dotenv()

class Headers:
    API_KEY = os.getenv('GITHUB_API_KEY')

    def pet_store_headers(self):
        return {
            "api_key": self.API_KEY,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def api_key_headers(self):
        return {"api_key": self.API_KEY}