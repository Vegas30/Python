# Задача: Разработка системы уведомлений с использованием паттерна Factory Method
# Представьте, что вы разрабатываете систему уведомлений для приложения.
# Уведомления могут отправляться различными способами:
#
# По электронной почте (Email)
# Через SMS
# В виде push-уведомлений
# Каждый тип уведомления имеет свой уникальный способ доставки,
# но все они должны быть созданы и обработаны единообразно.
#
# Условия задачи:
# Реализуйте абстрактный класс Notification, который будет определять общий интерфейс для всех типов уведомлений.
# Например:
#
# Метод send(), который отвечает за отправку уведомления.
# Реализуйте конкретные классы уведомлений:
#
# EmailNotification: отправка уведомления по электронной почте.
# SMSNotification: отправка уведомления через SMS.
# PushNotification: отправка push-уведомления.
# Используйте паттерн Factory Method для создания уведомлений:
#
# Создайте абстрактный класс NotificationFactory, который определяет метод create_notification().
# Реализуйте конкретные фабрики для каждого типа уведомлений:
# EmailNotificationFactory
# SMSNotificationFactory
# PushNotificationFactory
# Напишите клиентский код, который использует фабрику для создания уведомлений, не зная их конкретных классов.
#
# Требования к коду:
# Классы и методы должны быть реализованы с использованием принципов ООП.
# Добавьте пример использования системы уведомлений: создайте уведомление с помощью фабрики и отправьте его.
# Пример:
# Код должен быть структурирован так, чтобы с помощью фабрики можно было легко заменить способ доставки уведомлений.
# Например:
#
# factory = EmailNotificationFactory()
# notification = factory.create_notification()
# notification.send()

from abc import ABC, abstractmethod


# Базовый интерфейс Report (Продукт)
class Notification(ABC):
    @abstractmethod
    def send(self, message, type_notification) -> str:
        pass


# Конкретные продукты
class EmailNotification(Notification):
    def send(self, message, type_notification) -> str:
        return f"На почту {type_notification} было отправлено сообщение: {message}"


class SMSNotification(Notification):
    def send(self, message, type_notification) -> str:
        return f"SMS на номер {type_notification} было отправлено сообщение: {message}"


class PushNotification(Notification):
    def send(self, message, type_notification) -> str:
        return f"Уведомление на {type_notification} было отправлено сообщение: {message}"


# Абстрактная фабрика (Creator)
class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass

    def send_notification(self, message, type_notification) -> str:
        notification = self.create_notification()
        return notification.send(message, type_notification)


# Конкретные фабрики (Concrete Creators)
class EmailNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return EmailNotification()


class PushNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return PushNotification()


class SMSNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return SMSNotification()


# Клиентский код
def client_code(factory: NotificationFactory, message, type_notification) -> None:
    print(factory.send_notification(message, type_notification))


pdf_factory = SMSNotificationFactory()
client_code(pdf_factory, "hello world", "8800553555")

html_factory = EmailNotificationFactory()
client_code(html_factory, "hello world!!!!", "maxim@yandex.ru")

excel_factory = PushNotificationFactory()
client_code(excel_factory, "hello world!!!!", "ANDROID")
