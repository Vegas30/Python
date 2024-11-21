# Abstract Factory
from abc import ABC, abstractmethod


# Абстрактный продукт: Button
class Button(ABC):
   @abstractmethod
   def render(self) -> str:
       pass


# Абстрактный продукт: Window
class Window(ABC):
   @abstractmethod
   def render(self) -> str:
       pass


# Конкретный продукт для Windows: Button
class WindowsButton(Button):
   def render(self) -> str:
       return "Rendering Windows Button"


# Конкретный продукт для Windows: Window
class WindowsWindow(Window):
   def render(self) -> str:
       return "Rendering Windows Window"


# Конкретный продукт для Mac: Button
class MacButton(Button):
   def render(self) -> str:
       return "Rendering Mac Button"


# Конкретный продукт для Mac: Window
class MacWindow(Window):
   def render(self) -> str:
       return "Rendering Mac Window"


# Абстрактная фабрика
class GUIFactory(ABC):
   @abstractmethod
   def create_button(self) -> Button:
       pass


   @abstractmethod
   def create_window(self) -> Window:
       pass


# Конкретная фабрика для Windows
class WindowsFactory(GUIFactory):
   def create_button(self) -> Button:
       return WindowsButton()


   def create_window(self) -> Window:
       return WindowsWindow()


# Конкретная фабрика для Mac
class MacFactory(GUIFactory):
   def create_button(self) -> Button:
       return MacButton()


   def create_window(self) -> Window:
       return MacWindow()


# Клиентский код
def client_code(factory: GUIFactory) -> None:
   button = factory.create_button()
   window = factory.create_window()
   print(button.render())
   print(window.render())


print("Windows GUI:")
windows_factory = WindowsFactory()
client_code(windows_factory)  # Output: Rendering Windows Button, Rendering Windows Window


print("\nMac GUI:")
mac_factory = MacFactory()
client_code(mac_factory)  # Output: Rendering Mac Button, Rendering Mac Window
