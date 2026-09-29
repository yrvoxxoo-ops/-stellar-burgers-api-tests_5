import allure
import requests

from data import ResponseMessages
from urls import BASE_URL, LOGIN_USER_ENDPOINT


@allure.feature("Логин пользователя")
class TestLoginUser:

    @allure.title("Вход под существующим пользователем")
    @allure.story("Успешная авторизация")
    def test_login_existing_user_success(self, registered_user):
        login_data = {"email": registered_user["email"], "password": registered_user["password"]}

        with allure.step("Отправляем запрос на логин существующего пользователя"):
            response = requests.post(f"{BASE_URL}{LOGIN_USER_ENDPOINT}",json=login_data)

        with allure.step("Получаем тело ответа"):
            response_json = response.json()

        with allure.step("Проверяем успешный логин пользователя"):
            assert response.status_code == 200
            assert response_json["success"] is True
            assert "accessToken" in response_json
            assert "refreshToken" in response_json
            assert response_json["user"]["email"] == registered_user["email"]
            assert response_json["user"]["name"] == registered_user["name"]

    @allure.title("Вход с неверным логином и паролем")
    @allure.story("Ошибка авторизации")
    def test_login_with_invalid_login_and_password_returns_error(self, user_data):
        invalid_login_data = {"email": user_data["email"],"password": "wrong_password"}

        with allure.step("Отправляем запрос на логин с неверными данными"):
            response = requests.post(f"{BASE_URL}{LOGIN_USER_ENDPOINT}", json=invalid_login_data)

        with allure.step("Получаем тело ответа"):
            response_json = response.json()

        with allure.step("Проверяем ошибку при неверном логине и пароле"):
            assert response.status_code == 401
            assert response_json["success"] is False
            assert response_json["message"] == ResponseMessages.EMAIL_PASSWORD_INCORRECT