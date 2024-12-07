# Пример реализации паттерна Domain Model


class Customer:
    def __init__(self, customer_id: int, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.orders = []


    def add_order(self, order):
        self.orders.append(order)


    def get_total_spent(self):
        return sum(order.amount for order in self.orders)


    def __str__(self):
        return f"Customer(id={self.customer_id}, name={self.name}, email={self.email}, total_spent={self.get_total_spent()})"




class Order:
    def __init__(self, order_id: int, customer_id: int, amount: float):
        self.order_id = order_id
        self.customer_id = customer_id
        self.amount = amount
        self.status = "pending"  # статусы могут быть: pending, shipped, delivered, canceled


    def set_status(self, status: str):
        self.status = status


    def __str__(self):
        return f"Order(id={self.order_id}, customer_id={self.customer_id}, amount={self.amount}, status={self.status})"




# Репозиторий для работы с моделями
class CustomerRepository:
    def __init__(self):
        self.customers = {}


    def add(self, customer: Customer):
        self.customers[customer.customer_id] = customer


    def get_by_id(self, customer_id: int):
        return self.customers.get(customer_id)


    def get_all(self):
        return list(self.customers.values())




class OrderRepository:
    def __init__(self):
        self.orders = {}


    def add(self, order: Order):
        self.orders[order.order_id] = order


    def get_by_customer_id(self, customer_id: int):
        return [order for order in self.orders.values() if order.customer_id == customer_id]




# Пример использования
if __name__ == "__main__":
    # Создаем репозитории
    customer_repository = CustomerRepository()
    order_repository = OrderRepository()


    # Создаем клиентов и заказы
    customer1 = Customer(1, "Alice", "alice@example.com")
    customer2 = Customer(2, "Bob", "bob@example.com")


    order1 = Order(1, 1, 250.0)
    order2 = Order(2, 1, 500.0)
    order3 = Order(3, 2, 300.0)


    # Добавляем клиентов и заказы в репозитории
    customer_repository.add(customer1)
    customer_repository.add(customer2)


    order_repository.add(order1)
    order_repository.add(order2)
    order_repository.add(order3)


    # Связываем заказы с клиентами
    customer1.add_order(order1)
    customer1.add_order(order2)
    customer2.add_order(order3)


    # Печатаем информацию о клиентах и их заказах
    for customer in customer_repository.get_all():
        print(customer)
        for order in order_repository.get_by_customer_id(customer.customer_id):
            print(order)
