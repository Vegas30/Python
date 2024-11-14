from dataclasses import dataclass, field
from typing import List, Dict


# Класс для описания товара
@dataclass
class Product:
    id: int
    name: str
    price: float
    category: str = "General"


# Класс для описания единицы заказа
@dataclass
class OrderItem:
    product: Product
    quantity: int = 1

    @property
    def total_price(self) -> float:
        """Вычисляет стоимость конкретной позиции в заказе"""
        return self.product.price * self.quantity


# Класс для управления заказами
@dataclass
class Order:
    items: List[OrderItem] = field(default_factory=list)
    tax_rate: float = 0.07  # Налог по умолчанию (7%)
    metadata: Dict[str, str] = field(default_factory=dict, repr=False)

    def add_item(self, product: Product, quantity: int = 1) -> None:
        """Добавляет товар в заказ"""
        self.items.append(OrderItem(product, quantity))

    def total_price(self) -> float:
        """Вычисляет общую стоимость заказа, включая налог"""
        subtotal = sum(item.total_price for item in self.items)
        return subtotal * (1 + self.tax_rate)

    def summary(self) -> str:
        """Возвращает сводку заказа"""
        item_summaries = [
            f"{item.product.name} x {item.quantity}: ${item.total_price:.2f}"
            for item in self.items
        ]
        return "\n".join(item_summaries) + f"\nTotal with tax: ${self.total_price():.2f}"


if __name__ == "__main__":
    product1 = Product(id=1, name="Laptop", price=999.99, category="Electronics")
    product2 = Product(id=2, name="Mouse", price=49.99, category="Electronics")
    product3 = Product(id=3, name="Book", price=19.99, category="Books")

    order = Order(tax_rate=0.1)  # Налог 10%

    order.add_item(product1, quantity=1)
    order.add_item(product2, quantity=2)
    order.add_item(product3, quantity=3)

    print(order.summary())
