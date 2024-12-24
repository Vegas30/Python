# Задача: Система бронирования отелей (Паттерн "Фабричный метод")
#
# Условие задачи:
# Вы разрабатываете систему бронирования номеров в отелях. В системе есть несколько типов номеров:
#
# Стандартный номер
# Люкс
# Апартаменты
# Каждый номер имеет:
#
# Имя отеля (строка)
# Тип номера (строка)
# Список удобств (например, "Wi-Fi", "Мини-бар", "Телевизор")
# Стоимость за ночь (число)
# В зависимости от типа номера, удобства и стоимость отличаются. В системе используется паттерн "Фабричный метод" для создания объектов разных типов номеров.
#
# Ваша задача:
#
# Реализовать базовый класс HotelRoom (номер отеля).
# Создать подклассы StandardRoom, LuxuryRoom и ApartmentRoom, которые наследуются от HotelRoom и задают уникальные параметры для каждого типа номера.
# Реализовать фабрику RoomFactory, которая создает объекты номеров в зависимости от их типа.
# Написать код, который демонстрирует добавление нескольких номеров в систему и вывод информации о них.
#
# Пример вывода:
# Отель: Grand Hotel
# Тип номера: Стандартный номер
# Удобства: Wi-Fi, Телевизор
# Стоимость за ночь: 3000 рублей
#
# Отель: Grand Hotel
# Тип номера: Люкс
# Удобства: Wi-Fi, Мини-бар, Телевизор, Сейф
# Стоимость за ночь: 8000 рублей
#
# Отель: Elite Stay
# Тип номера: Апартаменты
# Удобства: Wi-Fi, Мини-бар, Телевизор, Кухня, Джакузи
# Стоимость за ночь: 15000 рублей
from abc import ABC, abstractmethod

class HotelRoom(ABC):
    def __init__(self, hotel_name, room_type, amenities, price_per_night):
        self.hotel_name = hotel_name
        self.room_type = room_type
        self.amenities = amenities
        self.price_per_night = price_per_night

    def __str__(self):
        return f"Отель: {self.hotel_name}nТип номера: {self.room_type}nУдобства: {', '.join(self.amenities)}nСтоимость за ночь: {self.price_per_night} рублей"

class StandardRoom(HotelRoom):
    def __init__(self, hotel_name):
        super().__init__(hotel_name, "Стандартный номер", ["Wi-Fi", "Телевизор"], 3000)

class LuxuryRoom(HotelRoom):
    def __init__(self, hotel_name):
        super().__init__(hotel_name, "Люкс", ["Wi-Fi", "Мини-бар", "Телевизор", "Сейф"], 8000)

class ApartmentRoom(HotelRoom):
    def __init__(self, hotel_name):
        super().__init__(hotel_name, "Апартаменты", ["Wi-Fi", "Мини-бар", "Телевизор", "Кухня", "Джакузи"], 15000)

class RoomFactory:
    def create_room(self, room_type, hotel_name):
        if room_type == "Стандартный номер":
            return StandardRoom(hotel_name)
        elif room_type == "Люкс":
            return LuxuryRoom(hotel_name)
        elif room_type == "Апартаменты":
            return ApartmentRoom(hotel_name)
        else:
            raise ValueError("Неверный тип номера")

# Демонстрация использования
room_factory = RoomFactory()

room1 = room_factory.create_room("Стандартный номер", "Grand Hotel")
print(room1)
print()

room2 = room_factory.create_room("Люкс", "Grand Hotel")
print(room2)
print()

room3 = room_factory.create_room("Апартаменты", "Elite Stay")
print(room3)
