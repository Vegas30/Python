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
    def __init__(self, hotel_name):
        self.hotel_name = hotel_name
        self.amenities = []
        self.price_per_night = 0

    @abstractmethod
    def configure_room(self):
        """Абстрактный метод для настройки номера"""
        pass

    def __str__(self):
        return (f"Отель: {self.hotel_name}\n"
                f"Тип номера: {self.room_type}\n"
                f"Удобства: {', '.join(self.amenities)}\n"
                f"Стоимость за ночь: {self.price_per_night} рублей\n")


class StandardRoom(HotelRoom):
    def configure_room(self):
        self.room_type = "Стандартный номер"
        self.amenities = ["Wi-Fi", "Телевизор"]
        self.price_per_night = 3000


class LuxuryRoom(HotelRoom):
    def configure_room(self):
        self.room_type = "Люкс"
        self.amenities = ["Wi-Fi", "Мини-бар", "Телевизор", "Сейф"]
        self.price_per_night = 8000


class ApartmentRoom(HotelRoom):
    def configure_room(self):
        self.room_type = "Апартаменты"
        self.amenities = ["Wi-Fi", "Мини-бар", "Телевизор", "Кухня", "Джакузи"]
        self.price_per_night = 15000


class RoomFactory:
    @staticmethod
    def create_room(room_type, hotel_name):
        if room_type == "standard":
            room = StandardRoom(hotel_name)
        elif room_type == "luxury":
            room = LuxuryRoom(hotel_name)
        elif room_type == "apartment":
            room = ApartmentRoom(hotel_name)
        else:
            raise ValueError("Неизвестный тип номера")
        room.configure_room()
        return room


if __name__ == '__main__':
    room1 = RoomFactory.create_room("standard", "Grand Hotel")
    room2 = RoomFactory.create_room("luxury", "Grand Hotel")
    room3 = RoomFactory.create_room("apartment", "Elite Stay")

    print(room1)
    print(room2)
    print(room3)