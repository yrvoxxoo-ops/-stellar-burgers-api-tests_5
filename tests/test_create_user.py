import allure
import pytest
import requests

from data import REQUIRED_FIELDS_FOR_CREATE_USER, ResponseMessages
from helpers import remove_required_field
from urls import BASE_URL, REGISTER_USER_ENDPOINT


@allure.feature("Создание пользователя")
class TestCreateUser:



    @allure.title("Создание уникального пользователя")
    @allure.story("Успешная регистрация")
    def test_create_unique_user_success(self, user_data, delete_user):
        with allure.step("Отправляем запрос на создание уникального пользователя"):
            response = requests.post(f"{BASE_URL}{REGISTER_USER_ENDPOINT}", json=user_data)

        with allure.step("Получаем тело ответа"):
            response_json = response.json()

        with allure.step("Сохраняем токен для удаления пользователя после теста"):
            if response.status_code == 200 and "accessToken" in response_json:
                delete_user.append(response_json["accessToken"])

        with allure.step("Проверяем статус-код и тело успешного ответа"):
            assert response.status_code == 200
            assert response_json["success"] is True
            assert "accessToken" in response_json
            assert "refreshToken" in response_json
            assert response_json["user"]["email"] == user_data["email"]
            assert response_json["user"]["name"] == user_data["name"]



    @allure.title("Создание пользователя, который уже зарегистрирован")
    @allure.story("Ошибка при повторной регистрации")
    def test_create_existing_user_returns_error(self, user_data, delete_user):
        with allure.step("Создаём нового пользователя"):
            response_create_user = requests.post(f"{BASE_URL}{REGISTER_USER_ENDPOINT}",json=user_data)

        with allure.step("Получаем тело ответа после создания пользователя"):
            response_create_user_json = response_create_user.json()

        with allure.step("Сохраняем токен для удаления пользователя после теста"):
            if response_create_user.status_code == 200 and "accessToken" in response_create_user_json:
                delete_user.append(response_create_user_json["accessToken"])

        with allure.step("Повторно отправляем запрос с теми же данными"):
            response_existing_user = requests.post(f"{BASE_URL}{REGISTER_USER_ENDPOINT}", json=user_data)

        with allure.step("Получаем тело ответа при повторной регистрации"):
            response_existing_user_json = response_existing_user.json()

        with allure.step("Проверяем, что нельзя создать уже зарегистрированного пользователя"):
            assert response_existing_user.status_code == 403
            assert response_existing_user_json["success"] is False
            assert response_existing_user_json["message"] == ResponseMessages.USER_ALREADY_EXISTS

    @allure.title("Создание пользователя без обязательного поля")
    @allure.story("Ошибка при отсутствии обязательного поля")
    @pytest.mark.parametrize("field_name", REQUIRED_FIELDS_FOR_CREATE_USER)

    def test_create_user_without_required_field_returns_error(self, user_data, field_name):
        allure.dynamic.title(f"Создание пользователя без поля {field_name}")

        with allure.step(f"Удаляем обязательное поле {field_name} из тела запроса"):
            user_data_without_required_field = remove_required_field(user_data, field_name)

        with allure.step("Отправляем запрос на создание пользователя с неполными данными"):
            response = requests.post(f"{BASE_URL}{REGISTER_USER_ENDPOINT}",json=user_data_without_required_field)

        with allure.step("Получаем тело ответа"):
            response_json = response.json()

        with allure.step("Проверяем ошибку при отсутствии обязательного поля"):
            assert response.status_code == 403
            assert response_json["success"] is False
            assert response_json["message"] == ResponseMessages.REQUIRED_FIELDS