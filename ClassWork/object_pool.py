# Object pool
class ObjectPool:
    def __init__(self, create_object, max_size=5):
        self._create_object = create_object  # Функция для создания объектов
        self._pool = []  # Пул объектов
        self._max_size = max_size


    def acquire(self):
        """Получить объект из пула."""
        if self._pool:
            return self._pool.pop()
        elif len(self._pool) < self._max_size:
            return self._create_object()
        else:
            raise Exception("No available objects in the pool.")


    def release(self, obj):
        """Вернуть объект в пул."""
        if len(self._pool) < self._max_size:
            self._pool.append(obj)


# Пример объекта, который будет управляться пулом
class DatabaseConnection:
    def __init__(self):
        print("Создание нового подключения к базе данных")


# Использование Object Pool
def create_db_connection():
    return DatabaseConnection()


pool = ObjectPool(create_db_connection, max_size=3)


# Запрос объектов
conn1 = pool.acquire()
conn2 = pool.acquire()


# Возвращение объекта в пул
pool.release(conn1)


# Получение объекта повторно
conn3 = pool.acquire()  # conn1 будет повторно использован