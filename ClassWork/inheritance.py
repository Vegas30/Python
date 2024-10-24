# 1. Создайте класс Animal, который содержит имя и возраст животного. Создайте
# наследственный класс Bird, который добавляет способность летать или не летать.
# Реализуйте метод speak, который выводит звук, издаваемый животным.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} издает звук"

    def __str__(self):
        return f"{self.name} и {self.age}"


class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(name, age)
        self.can_fly = can_fly

    def speak(self):
        print(super().speak())
        print(f"Но она еще и {self.can_fly}")

    def __str__(self):
        return f"{self.name} и {self.age}, {self.can_fly}"


def main():
    dog = Animal("Бобик", 5)
    print(dog)
    print(dog.speak())

    bird = Bird("Тузик", 100, "не летает")
    print(bird)
    bird.speak()


main()


# Создайте класс Transport, описывающий транспортное средство (например, скорость
# и мощность двигателя). Создавайте классы наследники Car и Plane, которые добавляют
# свои специфические свойста.

class Transport:
    def __init__(self, speed, power):
        self.speed = speed
        self.power = power

    def info(self):
        print(f"{self.speed} {self.power}")


class Car(Transport):
    def __init__(self, speed, power, color):
        super().__init__(speed, power)
        self.color = color


class Plane(Transport):
    def __init__(self, speed, power, fuselage):
        super().__init__(speed, power)
        self.fuselage = fuselage


transport = Transport(2, 3)
car = Car(200, 10, "red")
plane = Plane(800, 100, "monoplan")
transport.info()
car.info()
plane.info()

