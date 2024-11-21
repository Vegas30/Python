Builder
# Продукт
class House:
    def __init__(self):
        self.parts = []


    def add_part(self, part):
        self.parts.append(part)


    def __str__(self):
        return f"House parts: {', '.join(self.parts)}"


# Абстрактный строитель
class HouseBuilder:
    def build_walls(self):
        pass


    def build_roof(self):
        pass


    def build_garden(self):
        pass


    def get_result(self):
        pass


# Конкретный строитель
class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()


    def build_walls(self):
        self.house.add_part("Walls")


    def build_roof(self):
        self.house.add_part("Roof")


    def build_garden(self):
        self.house.add_part("Garden")


    def get_result(self):
        return self.house


# Директор
class Director:
    def __init__(self, builder):
        self.builder = builder


    def construct(self):
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.build_garden()


# Клиентский код
builder = ConcreteHouseBuilder()
director = Director(builder)


# Создаем объект
director.construct()
house = builder.get_result()


print(house)
