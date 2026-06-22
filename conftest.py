import allure
import pytest
import requests

from helpers import generate_user_data
from urls import (BASE_URL, REGISTER_USER_ENDPOINT, USER_ENDPOINT, INGREDIENTS_ENDPOINT)


@pytest.fixture
def user_data():
    return generate_user_data()


@pytest.fixture
def delete_user():
    access_tokens = []
    yield access_tokens
    for token in access_tokens:
        if token:
            with allure.step("Удаляем тестового пользователя после теста"):
                requests.delete(f"{BASE_URL}{USER_ENDPOINT}", headers={"Authorization": token})


@pytest.fixture
def registered_user(user_data):
    with allure.step("Создаём пользователя для теста"):
        response = requests.post(f"{BASE_URL}{REGISTER_USER_ENDPOINT}",json=user_data)

    with allure.step("Получаем токен созданного пользователя"):
        response_json = response.json()
        access_token = response_json.get("accessToken")
    user_data["accessToken"] = access_token
    yield user_data
    if access_token:
        with allure.step("Удаляем пользователя после теста"):
            requests.delete(f"{BASE_URL}{USER_ENDPOINT}", headers={"Authorization": access_token})


@pytest.fixture
def ingredients():
    with allure.step("Получаем список ингредиентов"):
        response = requests.get(f"{BASE_URL}{INGREDIENTS_ENDPOINT}")

    with allure.step("Берём хеши двух ингредиентов"):
        ingredients_data = response.json()["data"]
        return [ingredients_data[0]["_id"], ingredients_data[1]["_id"]]