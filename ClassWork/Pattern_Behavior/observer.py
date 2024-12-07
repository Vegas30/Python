# Интерфейс наблюдателя
class Observer:
    def update(self, message):
        raise NotImplementedError("Метод update должен быть переопределён")


# Интерфейс субъекта
class Subject:
    def __init__(self):
        self._observers = []


    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)


    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)


    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


# Конкретный субъект
class Blog(Subject):
    def __init__(self, name):
        super().__init__()
        self.name = name


    def publish_post(self, title):
        print(f"Новый пост на блоге '{self.name}': {title}")
        self.notify(f"Новый пост: {title}")


# Конкретные наблюдатели
class EmailSubscriber(Observer):
    def update(self, message):
        print(f"[Email] Уведомление: {message}")


class SMSNotifier(Observer):
    def update(self, message):
        print(f"[SMS] Уведомление: {message}")


class PushNotifier(Observer):
    def update(self, message):
        print(f"[Push] Уведомление: {message}")


# Клиентский код
if __name__ == "__main__":
    blog = Blog("Tech Insights")


    email_subscriber = EmailSubscriber()
    sms_notifier = SMSNotifier()
    push_notifier = PushNotifier()


    blog.attach(email_subscriber)
    blog.attach(sms_notifier)
    blog.attach(push_notifier)


    blog.publish_post("Как работает паттерн Observer в Python?")
    blog.detach(sms_notifier)
    blog.publish_post("10 советов для начинающих программистов")


# Результат выполнения:
# Новый пост на блоге 'Tech Insights': Как работает паттерн Observer в Python?
# [Email] Уведомление: Новый пост: Как работает паттерн Observer в Python?
# [SMS] Уведомление: Новый пост: Как работает паттерн Observer в Python?
# [Push] Уведомление: Новый пост: Как работает паттерн Observer в Python?
# Новый пост на блоге 'Tech Insights': 10 советов для начинающих программистов
# [Email] Уведомление: Новый пост: 10 советов для начинающих программистов
# [Push] Уведомление: Новый пост: 10 советов для начинающих программистов