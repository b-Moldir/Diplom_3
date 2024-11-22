import requests
from data import BASE_URL, REGISTER_URL, USER_URL
from helpers import get_headers


class UsersMethods:
    def create_user(self, payload):
        response = requests.post(f'{BASE_URL}{REGISTER_URL}', json=payload)
        return response.status_code, response.json()

    def delete_user(self, token):
        headers = get_headers(token)
        response = requests.delete(f'{BASE_URL}{USER_URL}', headers=headers)
        return response.status_code, response.json()
