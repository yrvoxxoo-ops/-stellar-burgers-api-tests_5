import uuid


def generate_user_data():
    unique_part = uuid.uuid4().hex

    return {
        "email": f"test_user_{unique_part}@yandex.ru",
        "password": "password123",
        "name": f"User_{unique_part}"
    }


def remove_required_field(user_data, field_name):
    user_data_without_field = user_data.copy()
    user_data_without_field.pop(field_name)

    return user_data_without_field