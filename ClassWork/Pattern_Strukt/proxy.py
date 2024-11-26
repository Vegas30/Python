# Интерфейс для реального субъекта
class Subject:
    def request(self):
        pass

    # Реальный субъект


class RealSubject(Subject):
    def request(self):
        print("Выполнение запроса в реальном субъекте.")

    # Заместитель


class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        print("Прокси: Проверка прав доступа перед выполнением запроса.")
        self._real_subject.request()

    # Пример использования


real_subject = RealSubject()
proxy = Proxy(real_subject)

proxy.request()