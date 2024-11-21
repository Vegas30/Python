# FactoryOfFactories
class Animal:
    """Базовый класс для животных."""
    def speak(self):
        raise NotImplementedError("Метод 'speak' должен быть переопределён")


class Dog(Animal):
    """Класс для собак."""
    def speak(self):
        return "Woof!"


class Cat(Animal):
    """Класс для кошек."""
    def speak(self):
        return "Meow!"


class AnimalFactory:
    """Базовый класс фабрики животных."""
    def create_animal(self):
        raise NotImplementedError("Метод 'create_animal' должен быть переопределён")


class DogFactory(AnimalFactory):
    """Фабрика для создания собак."""
    def create_animal(self):
        return Dog()


class CatFactory(AnimalFactory):
    """Фабрика для создания кошек."""
    def create_animal(self):
        return Cat()


class FactoryOfFactories:
    """Основная фабрика, которая создаёт другие фабрики."""
    def get_factory(self, animal_type):
        if animal_type == "dog":
            return DogFactory()
        elif animal_type == "cat":
            return CatFactory()
        else:
            raise ValueError(f"Неизвестный тип животного: {animal_type}")


# Использование
factory_of_factories = FactoryOfFactories()


# Создание фабрики для собак
dog_factory = factory_of_factories.get_factory("dog")
dog = dog_factory.create_animal()
print(dog.speak())  # Вывод: Woof!


# Создание фабрики для кошек
cat_factory = factory_of_factories.get_factory("cat")
cat = cat_factory.create_animal()
print(cat.speak())  # Вывод: Meow!