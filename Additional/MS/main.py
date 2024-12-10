# /project_order_management/main.py
from CSV.file_operation import load_from_file, save_to_file
from CSV.orders_management import add_order, remove_order
from CSV.validation import validate_order_data, ValidationError



ORDERS_FILE = 'data/orders.json'

"""Глобальная переменная"""

def load_orders():
    """Загружает список заказаов из файла JSON"""

    return load_from_file(ORDERS_FILE) or []

def save_orders(orders):
    """Сохраняет список заказов в файл JSON"""

    save_to_file(ORDERS_FILE, orders)


def main():
    """Консольное приложение для управления заказами в интернет-магазине """

    orders = load_orders()
    print(orders)

    while True:
        print("\nПриложение для управления интернет-магазином")
        print("-"*40)
        print("Выберете действие")
        print("1. Добавьте заказ")

        choice = input("Введите номер действия: ")
        if choice == "1":
            try:
                order_data = {
                    'order_id': input("Введите уникальный идентификатор ID заказа: "),
                    'customer_name': input("Введите имя клиента: "),
                    'order_date': input("ВВедите дату заказа 'YYYY-MM-DD': "),
                    'status': input("Введите статус заказа: "),
                    'address': input("Введите адрес доставки: "),
                    'items': {
                        'item_name': input("Введите название товара: "),
                        'quantity': input("Введите количество: "),
                        'price': float(input("Введите цену за единицу: "))

                    }
                }


                validate_order_data(order_data, orders)
                add_order(orders, order_data)
                save_orders(orders)
                print("Заказ добавлен")
            except ValidationError as e:
                print(f"Ошибка добавления сотрудника: {e}")

        elif choice == "2":
            order_id = input("Введите ID заказа для удаления: ")
            if remove_order(orders, order_id):
                save_orders(orders)
                print(f"заказ с ID {order_id} удален!")
            else:
                print(f"заказ с ID {order_id} не найден!")

        # elif choice == "3":
        #     order_id = input("Введите ID заказа для обновления статуса: ")





if __name__ == "__main__":
    main()

