from abc import ABC, abstractmethod


# Интерфейс логгера
class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass


# Реализация реального логгера
class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f"[LOG]: {message}")


# Реализация Null Object
class NullLogger(Logger):
    def log(self, message: str):
        pass  # Ничего не делает


# Класс, использующий логгер
class Application:
    def __init__(self, logger: Logger):
        self.logger = logger

    def perform_action(self):
        self.logger.log("Действие выполнено.")
        print("Выполнение основного функционала.")


# Клиентский код
if __name__ == "__main__":
    # Пример с реальным логгером
    real_logger = ConsoleLogger()
    app_with_logger = Application(real_logger)
    app_with_logger.perform_action()

    print("\nПример с Null Logger:")
    # Пример с Null Object
    null_logger = NullLogger()
    app_with_logger_null = Application(null_logger)
    app_with_logger_null.perform_action()
