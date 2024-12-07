class Event:
    """Абстракция для событий"""
    pass




class OrderCreatedEvent(Event):
    """Событие о создании заказа"""
    def __init__(self, order_id):
        self.order_id = order_id




class EventManager:
    """Менеджер событий, который управляет подписками на события"""
    def __init__(self):
        self.handlers = {}


    def subscribe(self, event_type, handler):
        if event_type not in self.handlers:
            self.handlers[event_type] = []
        self.handlers[event_type].append(handler)


    def publish(self, event):
        event_type = type(event)
        if event_type in self.handlers:
            for handler in self.handlers[event_type]:
                handler(event)




class OrderService:
    """Сервис для обработки заказов"""
    def __init__(self, event_manager):
        self.event_manager = event_manager


    def create_order(self, order_id):
        # Логика создания заказа
        print(f"Заказ {order_id} создан.")
        # Генерация события
        event = OrderCreatedEvent(order_id)
        self.event_manager.publish(event)




# Обработчики событий
def send_notification(event):
    print(f"Отправлено уведомление о создании заказа: {event.order_id}")




def update_order_status(event):
    print(f"Статус заказа {event.order_id} обновлен на 'В обработке'.")




# Клиентский код
if __name__ == "__main__":
    event_manager = EventManager()


    # Подписываем обработчики на событие
    event_manager.subscribe(OrderCreatedEvent, send_notification)
    event_manager.subscribe(OrderCreatedEvent, update_order_status)


    order_service = OrderService(event_manager)


    # Создание заказа
    order_service.create_order(101)