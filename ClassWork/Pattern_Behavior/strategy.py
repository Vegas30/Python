from abc import ABC, abstractmethod


# Интерфейс стратегии
class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, weight: float) -> float:
        pass


# Конкретные стратегии
class GroundDelivery(DeliveryStrategy):
    def calculate_cost(self, weight: float) -> float:
        return weight * 1.2  # Стоимость доставки за кг по земле


class AirDelivery(DeliveryStrategy):
    def calculate_cost(self, weight: float) -> float:
        return weight * 3.5  # Стоимость доставки за кг по воздуху


class SeaDelivery(DeliveryStrategy):
    def calculate_cost(self, weight: float) -> float:
        return weight * 0.8  # Стоимость доставки за кг морем


# Контекст
class DeliveryContext:
    def __init__(self, strategy: DeliveryStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: DeliveryStrategy):
        self._strategy = strategy

    def calculate_cost(self, weight: float) -> float:
        return self._strategy.calculate_cost(weight)

# Клиентский код
if __name__ == "__main__":
    # Задаём вес посылки
    package_weight = 10.0  # кг

    # Используем наземную доставку
    ground_delivery = GroundDelivery()
    context = DeliveryContext(ground_delivery)
    print(f"Наземная доставка: {context.calculate_cost(package_weight)} USD")

    # Переключаемся на воздушную доставку
    air_delivery = AirDelivery()
    context.set_strategy(air_delivery)
    print(f"Воздушная доставка: {context.calculate_cost(package_weight)} USD")

    # Переключаемся на морскую доставку
    sea_delivery = SeaDelivery()
    context.set_strategy(sea_delivery)
    print(f"Морская доставка: {context.calculate_cost(package_weight)} USD")
