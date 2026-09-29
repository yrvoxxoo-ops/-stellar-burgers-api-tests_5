import allure
import requests

from data import INVALID_INGREDIENT_HASH, ResponseMessages
from urls import BASE_URL, ORDERS_ENDPOINT


@allure.feature("Создание заказа")
class TestCreateOrder:



    @allure.title("Создание заказа с авторизацией")
    @allure.story("Успешное создание заказа")
    def test_create_order_with_authorization_success(self, registered_user, ingredients):
        order_data = {"ingredients": ingredients}

        headers = {"Authorization": registered_user["accessToken"]}

        with allure.step("Отправляем запрос на создание заказа с авторизацией"):
            response = requests.post(f"{BASE_URL}{ORDERS_ENDPOINT}",json=order_data, headers=headers)

        with allure.step("Получаем тело ответа"):
            response_json = response.json()

        with allure.step("Проверяем успешное создание заказа"):
            assert response.status_code == 200
            assert response_json["success"] is True
            assert "order" in response_json



    @allure.title("Создание заказа без авторизации")
    @allure.story("Успешное создание заказа")
    def test_create_order_without_authorization_success(self, ingredients):
        order_data = {"ingredients": ingredients}

        with allure.step("Отправляем запрос на создание заказа без авторизации"):
            response = requests.post(f"{BASE_URL}{ORDERS_ENDPOINT}",json=order_data)

        with allure.step("Получаем тело ответа"):
            response_json = response.json()

        with allure.step("Проверяем успешное создание заказа без авторизации"):
            assert response.status_code == 200
            assert response_json["success"] is True
            assert "order" in response_json



    @allure.title("Создание заказа с ингредиентами")
    @allure.story("Успешное создание заказа")
    def test_create_order_with_ingredients_success(self, ingredients):
        order_data = {"ingredients": ingredients}

        with allure.step("Отправляем запрос на создание заказа с ингредиентами"):
            response = requests.post(f"{BASE_URL}{ORDERS_ENDPOINT}",json=order_data)

        with allure.step("Получаем тело ответа"):
            response_json = response.json()

        with allure.step("Проверяем успешное создание заказа с ингредиентами"):
            assert response.status_code == 200
            assert response_json["success"] is True
            assert "order" in response_json



    @allure.title("Создание заказа без ингредиентов")
    @allure.story("Ошибка при создании заказа")
    def test_create_order_without_ingredients_returns_error(self):
        order_data = {"ingredients": []}

        with allure.step("Отправляем запрос на создание заказа без ингредиентов"):
            response = requests.post(f"{BASE_URL}{ORDERS_ENDPOINT}",json=order_data)

        with allure.step("Получаем тело ответа"):
            response_json = response.json()

        with allure.step("Проверяем ошибку при создании заказа без ингредиентов"):
            assert response.status_code == 400
            assert response_json["success"] is False
            assert response_json["message"] == ResponseMessages.INGREDIENT_IDS_MUST_BE_PROVIDED



    @allure.title("Создание заказа с неверным хешем ингредиентов")
    @allure.story("Ошибка при создании заказа")
    def test_create_order_with_invalid_ingredient_hash_returns_error(self):
        order_data = {"ingredients": [INVALID_INGREDIENT_HASH]}
        with allure.step("Отправляем запрос на создание заказа с неверным хешем ингредиента"):
            response = requests.post(f"{BASE_URL}{ORDERS_ENDPOINT}",json=order_data)
        with allure.step("Проверяем ошибку сервера при неверном хеше ингредиента"):
            assert response.status_code == 500