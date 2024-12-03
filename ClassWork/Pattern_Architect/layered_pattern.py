
# Data Access Layer
class ProductDataAccess:
    def __init__(self):
        self.products = []


    def add_product(self, product):
        self.products.append(product)


    def get_all_products(self):
        return self.products


# Business Logic Layer
class ProductService:
    def __init__(self, data_access):
        self.data_access = data_access


    def create_product(self, name, price):
        if price <= 0:
            raise ValueError("Цена должна быть больше нуля")
        product = {"name": name, "price": price}
        self.data_access.add_product(product)


    def list_products(self):
        return self.data_access.get_all_products()


# Presentation Layer
class ProductView:
    def __init__(self, service):
        self.service = service


    def display_products(self):
        products = self.service.list_products()
        if not products:
            print("Нет доступных товаров")
        for product in products:
            print(f"Товар: {product['name']}, Цена: {product['price']}")


    def add_product(self, name, price):
        try:
            self.service.create_product(name, price)
            print(f"Товар '{name}' добавлен!")
        except ValueError as e:
            print(f"Ошибка: {e}")


# Использование
if __name__ == "__main__":
    data_access = ProductDataAccess()
    service = ProductService(data_access)
    view = ProductView(service)


    view.display_products()  # Нет доступных товаров
    view.add_product("Телефон", 20000)  # Товар 'Телефон' добавлен!
    view.add_product("Ноутбук", -5000)  # Ошибка: Цена должна быть больше нуля
    view.display_products()  # Товар: Телефон, Цена: 20000

