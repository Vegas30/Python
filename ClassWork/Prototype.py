# Prototype
import copy


class Prototype:
   def clone(self):
       return copy.deepcopy(self)


class ConcretePrototype(Prototype):
   def __init__(self, name, value):
       self.name = name
       self.value = value


   def __str__(self):
       return f"Prototype Name: {self.name}, Value: {self.value}"


# Создание исходного объекта
prototype1 = ConcretePrototype("Prototype1", 100)
print("Original: ", prototype1)


# Клонирование объекта
prototype2 = prototype1.clone()
prototype2.name = "Prototype2"  # Изменяем копию
prototype2.value = 200


print("Cloned: ", prototype2)