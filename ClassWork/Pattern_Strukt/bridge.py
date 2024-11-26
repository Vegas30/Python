# Задача: Управление устройствами с использованием паттерна Bridge
# Представьте, что вы разрабатываете приложение для управления различными устройствами, такими как:
#
# Телевизор (TV)
# Радио (Radio)
# Каждое устройство поддерживает базовые операции:
#
# Включение/выключение
# Изменение громкости
# Переключение каналов или радиочастот
# Для управления устройствами используются различные типы пультов:
#
# Обычный пульт (BasicRemote)
# Улучшенный пульт (AdvancedRemote), который добавляет, например, функцию "Mute" (выключение звука).
# Условия задачи:
# Реализуйте базовый интерфейс Device, который определяет функции управления устройством:
#
# Включение/выключение.
# Настройка громкости.
# Переключение каналов/частот.
# Реализуйте конкретные устройства TV и Radio, которые реализуют интерфейс Device.
#
# Создайте базовый интерфейс Remote, представляющий пульт.
# В нем должны быть методы для управления устройством через интерфейс Device.
#
# Используйте паттерн Bridge, чтобы разделить управление устройством (Device) и реализацию пульта (Remote).
#
# Реализуйте два типа пультов:
#
# BasicRemote — с базовыми функциями.
# AdvancedRemote — с функцией отключения звука (mute).
# Напишите пример, где создается телевизор и радио, которые управляются разными пультами.

# Реализация: интерфейс "Реализация" (Component)

class DrawingAPI:
    def draw_circle(self, x, y, radius):
        pass

    # Конкретная реализация 1


class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"Рисуем круг в API1 на ({x}, {y}) с радиусом {radius}")

    # Конкретная реализация 2


class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"Рисуем круг в API2 на ({x}, {y}) с радиусом {radius}")

    # Абстракция: базовый класс


class Shape:
    def __init__(self, drawing_api):
        self.drawing_api = drawing_api

    def draw(self):
        pass

    def resize(self, factor):
        pass

    # Конкретная абстракция: круг


class Circle(Shape):
    def __init__(self, x, y, radius, drawing_api):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

    def resize(self, factor):
        self.radius *= factor

    # Использование паттерна Bridge


api1 = DrawingAPI1()
circle1 = Circle(5, 5, 10, api1)
circle1.draw()

api2 = DrawingAPI2()
circle2 = Circle(10, 10, 20, api2)
circle2.draw()

circle1.resize(2)
circle1.draw()