class ServiceLocator:
    _services = {}


    @staticmethod
    def register_service(name: str, service):
        """Регистрирует сервис в локаторе."""
        ServiceLocator._services[name] = service


    @staticmethod
    def get_service(name: str):
        """Возвращает зарегистрированный сервис."""
        service = ServiceLocator._services.get(name)
        if service is None:
            raise ValueError(f"Service '{name}' not found.")
        return service




# Пример сервисов
class EmailService:
    def send_email(self, recipient: str, message: str) -> None:
        print(f"Sending email to {recipient}: {message}")




class SmsService:
    def send_sms(self, recipient: str, message: str) -> None:
        print(f"Sending SMS to {recipient}: {message}")




# Клиентский код
class NotificationSender:
    def __init__(self):
        # Получение сервисов через локатор
        self.email_service = ServiceLocator.get_service("email")
        self.sms_service = ServiceLocator.get_service("sms")


    def send_notification(self, recipient: str, message: str, method: str) -> None:
        if method == "email":
            self.email_service.send_email(recipient, message)
        elif method == "sms":
            self.sms_service.send_sms(recipient, message)
        else:
            print("Invalid notification method.")




if __name__ == "__main__":
    # Регистрация сервисов
    ServiceLocator.register_service("email", EmailService())
    ServiceLocator.register_service("sms", SmsService())


    # Использование клиентского кода
    sender = NotificationSender()
    sender.send_notification("john.doe@example.com", "Hello, John!", "email")
    sender.send_notification("+1234567890", "Hello, John!", "sms")

