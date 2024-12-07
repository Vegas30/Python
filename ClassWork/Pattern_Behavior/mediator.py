from abc import ABC, abstractmethod
class Mediator(ABC):
    @abstractmethod
    def send(self, message, colleague):
        pass


# Конкретный посредник
class ChatMediator(Mediator):
    def __init__(self):
        self._users = []


    def add_user(self, user):
        self._users.append(user)


    def send(self, message, sender):
        for user in self._users:
            if user != sender:
                user.receive(message)


# Базовый класс участников
class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator


    def send(self, message):
        print(f"{self.name} отправляет сообщение: {message}")
        self.mediator.send(message, self)


    def receive(self, message):
        print(f"{self.name} получил сообщение: {message}")


# Клиентский код
mediator = ChatMediator()


user1 = User("Alice", mediator)
user2 = User("Bob", mediator)
user3 = User("Charlie", mediator)


mediator.add_user(user1)
mediator.add_user(user2)
mediator.add_user(user3)


user1.send("Привет всем!")
user2.send("Привет, Alice!")


# Результат выполнения:
# Alice отправляет сообщение: Привет всем!
# Bob получил сообщение: Привет всем!
# Charlie получил сообщение: Привет всем!
# Bob отправляет сообщение: Привет, Alice!
# Alice получил сообщение: Привет, Alice!
# Charlie получил сообщение: Привет, Alice!