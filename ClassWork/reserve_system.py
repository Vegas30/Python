# Необходимо создать систему бронирования номеров в отеле. Система должна отслеживать
# информацию о номерах, клиентах, и бронированиях.
# Hotel - содержит информацию о номерах и бронированиях
# Room - представляет номер в отеле
# Booking - представляет бронирование
# Customer - представляет клиента, который делает бронирование

# Используйте:
# Статический метод: для проверки доступности номера на заданные даты.
# Классовый метод: в классе Customer для генерации уникальных идентификаторов клиентов.
# Магические методы: __str__, __repr__, __len__, __getitem__

class Hotel:
    rooms = []

    def __init__(self, name):
        self.name = name

    @classmethod
    def count_room_hotel(cls):
        return len(cls.rooms)

    def __str__(self):
        return f"В {self.name} имеется {Hotel.count_room_hotel()}"

    @staticmethod
    def is_room_available(room):
        return room.is_available


class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = True
        Hotel.rooms.append(self)


class Booking:
    def __init__(self, customer, room, start_date, end_date):
        self.customer = customer
        self.room = room
        self.start_date = start_date
        self.end_date = end_date


class Customer:
    id_counter = 0

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.id = Customer.generate_id()

    @classmethod
    def generate_id(cls):
        cls.id_counter += 1
        return cls.id_counter

    def book_room(self, customer, room, start_date, end_date):
        if room.is_available:
            room.is_available = False
            return Booking(customer, room, start_date, end_date)
        else:
            return f"Данный номер недоступен"


def main():
    hotel1 = Hotel("Виктория Паласи")
    room1 = Room(101, "стандартный", 10000)
    room2 = Room(989, "премиум", 100000)

    customer1 = Customer(101, "стандартаный", "Максим", "Макаров", 14).book_room()
    print(hotel1)


main()


