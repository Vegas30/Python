from abc import ABC, abstractmethod

# Интерфейс команды
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


    @abstractmethod
    def undo(self):
        pass


# Конкретная команда
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light


    def execute(self):
        self.light.turn_on()


    def undo(self):
        self.light.turn_off()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light


    def execute(self):
        self.light.turn_off()


    def undo(self):
        self.light.turn_on()


# Получатель
class Light:
    def turn_on(self):
        print("Light is ON")


    def turn_off(self):
        print("Light is OFF")


# Отправитель
class RemoteControl:
    def __init__(self):
        self.command = None


    def set_command(self, command):
        self.command = command


    def press_button(self):
        if self.command:
            self.command.execute()


    def press_undo(self):
        if self.command:
            self.command.undo()


# Клиентский код
light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)


remote = RemoteControl()


# Включение света
remote.set_command(light_on)
remote.press_button()


# Выключение света
remote.set_command(light_off)
remote.press_button()


# Отмена действия
remote.press_undo()
