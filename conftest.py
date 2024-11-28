import pytest
from selenium import webdriver
from methods.users_methods import UsersMethods
from config import BASE_URL
from helpers import create_user_payload


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture()
def users_methods():
    return UsersMethods()


@pytest.fixture()
def user_data(users_methods):
    payload = create_user_payload()
    status_code, response_json = users_methods.create_user(payload)
    password = payload["password"]
    email = response_json["user"]["email"]
    token = response_json["accessToken"]
    yield email, password
    users_methods.delete_user(token)



