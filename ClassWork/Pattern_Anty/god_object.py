# Пример анти-паттерна: Бог-объект
class GodObject:
    def __init__(self):
        self.users = []
        self.orders = []
        self.notifications = []

    # Управление пользователями
    def add_user(self, user):
        self.users.append(user)
        print(f"Пользователь {user} добавлен.")

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"Пользователь {user} удалён.")

    # Управление заказами
    def add_order(self, order):
        self.orders.append(order)
        print(f"Заказ {order} добавлен.")

    def cancel_order(self, order):
        if order in self.orders:
            self.orders.remove(order)
            print(f"Заказ {order} отменён.")

    # Управление уведомлениями
    def send_notification(self, user, message):
        if user in self.users:
            self.notifications.append((user, message))
            print(f"Уведомление для {user}: {message}")
        else:
            print(f"Ошибка: пользователь {user} не найден.")


# Использование God Object
god = GodObject()

# Пользователи
god.add_user("Иван")
god.add_user("Мария")

# Заказы
god.add_order("Заказ #1")
god.cancel_order("Заказ #1")

# Уведомления
god.send_notification("Иван", "Ваш заказ готов.")
