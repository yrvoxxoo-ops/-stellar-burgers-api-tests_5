class ResponseMessages:
    USER_ALREADY_EXISTS = "User already exists"
    REQUIRED_FIELDS = "Email, password and name are required fields"
    EMAIL_PASSWORD_INCORRECT = "email or password are incorrect"
    INGREDIENT_IDS_MUST_BE_PROVIDED = "Ingredient ids must be provided"


class RequiredFields:
    EMAIL = "email"
    PASSWORD = "password"
    NAME = "name"


REQUIRED_FIELDS_FOR_CREATE_USER = [
    RequiredFields.EMAIL,
    RequiredFields.PASSWORD,
    RequiredFields.NAME]


INVALID_INGREDIENT_HASH = "invalid_ingredient_hash"