from abc import ABC, abstractmethod




# Интерфейс для отправки сообщений
class MessageSender(ABC):
    @abstractmethod
    def send_message(self, recipient: str, message: str) -> None:
        pass




# Реализация интерфейса: Отправка сообщений по электронной почте
class EmailSender(MessageSender):
    def send_message(self, recipient: str, message: str) -> None:
        print(f"Email to {recipient}: {message}")




# Реализация интерфейса: Отправка сообщений через SMS
class SmsSender(MessageSender):
    def send_message(self, recipient: str, message: str) -> None:
        print(f"SMS to {recipient}: {message}")




# Класс, зависящий от MessageSender
class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender


    def notify(self, recipient: str, message: str) -> None:
        self.sender.send_message(recipient, message)




# Пример использования
if __name__ == "__main__":
    # Внедрение зависимости через конструктор
    email_service = NotificationService(EmailSender())
    sms_service = NotificationService(SmsSender())


    # Отправка уведомлений
    email_service.notify("john.doe@example.com", "Hello, John!")
    sms_service.notify("+1234567890", "Hello, John!")
