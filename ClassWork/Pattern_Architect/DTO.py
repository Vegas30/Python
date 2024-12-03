# DTO для представления данных пользователя
class UserDTO:
    def __init__(self, user_id: int, username: str, email: str):
        self.user_id = user_id
        self.username = username
        self.email = email


    def __repr__(self):
        return f"UserDTO(user_id={self.user_id}, username='{self.username}', email='{self.email}')"




# Слой базы данных
class UserRepository:
    def get_user_by_id(self, user_id: int):
        # Имитируем данные из базы данных
        database_record = {
            "user_id": user_id,
            "username": "john_doe",
            "email": "john.doe@example.com",
            "password_hash": "hashed_password_12345",  # Приватные данные
            "last_login": "2024-12-01 15:45:00"
        }
        return database_record




# Слой сервиса
class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository


    def get_user_dto(self, user_id: int) -> UserDTO:
        user_data = self.repository.get_user_by_id(user_id)
        # Создание DTO, передаём только нужные данные
        return UserDTO(
            user_id=user_data["user_id"],
            username=user_data["username"],
            email=user_data["email"]
        )




# Слой контроллера
class UserController:
    def __init__(self, service: UserService):
        self.service = service


    def get_user_profile(self, user_id: int):
        user_dto = self.service.get_user_dto(user_id)
        return f"User Profile: {user_dto}"




# Пример использования
if __name__ == "__main__":
    repository = UserRepository()
    service = UserService(repository)
    controller = UserController(service)


    print(controller.get_user_profile(1))

