# Diplom_2

## Задание 2: API-автотесты для Stellar Burgers

Проект по API-автотестам для сервиса Stellar Burgers.

Тесты написаны с использованием `pytest`, `requests` и `allure-pytest`.


## Используется

* Python;
* Pytest;
* Requests;
* Allure.


## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск тестов

Для запуска всех тестов:

```bash
python -m pytest tests -v
```

## Запуск тестов с Allure

Для запуска тестов с сохранением результатов Allure:

```bash
python -m pytest tests --alluredir=allure_results
```

## Описание файлов

* `tests/test_create_user.py` — тесты создания пользователя;
* `tests/test_login_user.py` — тесты авторизации пользователя;
* `tests/test_create_order.py` — тесты создания заказа;
* `conftest.py` — фикстуры для тестов;
* `data.py` — тестовые данные и сообщения ответов API;
* `helpers.py` — вспомогательные функции;
* `urls.py` — URL и эндпоинты API;
* `requirements.txt` — список зависимостей проекта.
