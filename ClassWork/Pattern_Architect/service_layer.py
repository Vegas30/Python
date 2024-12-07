# Доменные объекты
class Customer:
    def __init__(self, customer_id: int, name: str):
        self.customer_id = customer_id
        self.name = name


    def __str__(self):
        return f"Customer(id={self.customer_id}, name={self.name})"




class Order:
    def __init__(self, order_id: int, customer_id: int, amount: float):
        self.order_id = order_id
        self.customer_id = customer_id
        self.amount = amount


    def __str__(self):
        return f"Order(id={self.order_id}, customer_id={self.customer_id}, amount={self.amount})"




# Репозитории
class CustomerRepository:
    def __init__(self):
        self.customers = {}


    def add(self, customer: Customer):
        self.customers[customer.customer_id] = customer


    def get_by_id(self, customer_id: int):
        return self.customers.get(customer_id)




class OrderRepository:
    def __init__(self):
        self.orders = {}


    def add(self, order: Order):
        self.orders[order.order_id] = order


    def get_by_customer_id(self, customer_id: int):
        return [order for order in self.orders.values() if order.customer_id == customer_id]


# Сервисный слой
class CustomerService:
    def __init__(self, customer_repo: CustomerRepository, order_repo: OrderRepository):
        self.customer_repo = customer_repo
        self.order_repo = order_repo


    def create_customer(self, customer_id: int, name: str):
        customer = Customer(customer_id, name)
        self.customer_repo.add(customer)
        return customer


    def get_customer_with_orders(self, customer_id: int):
        customer = self.customer_repo.get_by_id(customer_id)
        if not customer:
            raise ValueError(f"Customer with ID {customer_id} not found.")
        orders = self.order_repo.get_by_customer_id(customer_id)
        return customer, orders


    def create_order(self, customer_id: int, amount: float):
        customer = self.customer_repo.get_by_id(customer_id)
        if not customer:
            raise ValueError(f"Customer with ID {customer_id} not found.")
        order_id = len(self.order_repo.orders) + 1
        order = Order(order_id, customer_id, amount)
        self.order_repo.add(order)
        return order




# Пример использования
if __name__ == "__main__":
    # Инициализация репозиториев и сервиса
    customer_repo = CustomerRepository()
    order_repo = OrderRepository()
    customer_service = CustomerService(customer_repo, order_repo)


    # Создание клиентов
    customer_service.create_customer(1, "Alice")
    customer_service.create_customer(2, "Bob")


    # Создание заказов
    customer_service.create_order(1, 250.0)
    customer_service.create_order(1, 500.0)
    customer_service.create_order(2, 300.0)


    # Получение информации о клиенте и его заказах
    customer, orders = customer_service.get_customer_with_orders(1)
    print(f"Customer: {customer}")
    print("Orders:")
    for order in orders:
        print(order)
