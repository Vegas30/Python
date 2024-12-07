from typing import List, Optional


# Модель данных
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email


    def __str__(self):
        return f"User(id={self.user_id}, name={self.name}, email={self.email})"


# Интерфейс репозитория
class UserRepository:
    def add(self, user: User) -> None:
        raise NotImplementedError


    def get_by_id(self, user_id: int) -> Optional[User]:
        raise NotImplementedError


    def get_all(self) -> List[User]:
        raise NotImplementedError


    def update(self, user: User) -> None:
        raise NotImplementedError


    def delete(self, user_id: int) -> None:
        raise NotImplementedError


# Реализация репозитория (в памяти)
class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._users = {}


    def add(self, user: User) -> None:
        if user.user_id in self._users:
            raise ValueError(f"User with id {user.user_id} already exists.")
        self._users[user.user_id] = user


    def get_by_id(self, user_id: int) -> Optional[User]:
        return self._users.get(user_id)


    def get_all(self) -> List[User]:
        return list(self._users.values())


    def update(self, user: User) -> None:
        if user.user_id not in self._users:
            raise ValueError(f"User with id {user.user_id} does not exist.")
        self._users[user.user_id] = user


    def delete(self, user_id: int) -> None:
        if user_id not in self._users:
            raise ValueError(f"User with id {user_id} does not exist.")
        del self._users[user_id]


# Пример использования
if __name__ == "__main__":
    # Создаем репозиторий
    repository = InMemoryUserRepository()


    # Добавляем пользователей
    user1 = User(1, "Alice", "alice@example.com")
    user2 = User(2, "Bob", "bob@example.com")
    repository.add(user1)
    repository.add(user2)


    # Получаем пользователей
    print("Все пользователи:")
    for user in repository.get_all():
        print(user)


    # Обновляем пользователя
    user1.name = "Alice Smith"
    repository.update(user1)
    print(f"\nОбновленный пользователь: {repository.get_by_id(1)}")


    # Удаляем пользователя
    repository.delete(2)
    print("\nПользователи после удаления:")
    for user in repository.get_all():
        print(user)
