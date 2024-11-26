# Интерфейс, ожидаемый клиентом
class Target:
    def request(self):
        pass

    # Существующий класс с несовместимым интерфейсом


class Adaptee:
    def specific_request(self):
        return "Привет из Adaptee!"

    # Адаптер, который приводит Adaptee к интерфейсу Target


class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        # Преобразует вызов specific_request в request
        return f"Адаптировано: {self.adaptee.specific_request()}"

    # Клиентский код


def client_code(target):
    print(target.request())


# Пример использования
adaptee = Adaptee()
adapter = Adapter(adaptee)

client_code(adapter)