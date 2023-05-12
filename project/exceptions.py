class BaseServiceError(Exception):
    code = 500


class ItemNotFound(BaseServiceError):
    code = 404
    message = "Не найдено"

class UserAlreadyExists(BaseServiceError):
    code = 400
    message = "Такой пользователь уже существует"