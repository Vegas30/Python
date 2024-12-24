class HashTableOpenAddressing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Изначально таблица пустая


    def _hash(self, key):
        """Вычисляем базовый индекс"""
        return hash(key) % self.size


    def insert(self, key, value):
        """Добавляем элемент в таблицу с линейным пробированием"""
        index = self._hash(key)
        original_index = index
        i = 0  # Номер попытки пробирования
        while self.table[index] is not None and self.table[index][0] != key:
            i += 1
            index = (original_index + i) % self.size  # Линейное пробирование
        self.table[index] = (key, value)


    def get(self, key):
        """Получаем значение по ключу"""
        index = self._hash(key)
        original_index = index
        i = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]  # Возвращаем значение
            i += 1
            index = (original_index + i) % self.size
        return None  # Ключ не найден


    def remove(self, key):
        """Удаляем элемент по ключу"""
        index = self._hash(key)
        original_index = index
        i = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None  # Удаляем элемент
                return
            i += 1
            index = (original_index + i) % self.size


    def display(self):
        """Отображаем таблицу"""
        for i, item in enumerate(self.table):
            print(f"Index {i}: {item}")




# Пример использования
hash_table = HashTableOpenAddressing(5)


# Добавляем элементы
hash_table.insert("apple", 100)
hash_table.insert("banana", 200)
hash_table.insert("grape", 300)
hash_table.insert("cat", 400)
hash_table.insert("dog", 500)


# Выводим таблицу
hash_table.display()


# Получаем значения
print("Value for 'apple':", hash_table.get("apple"))
print("Value for 'dog':", hash_table.get("dog"))


# Удаляем элемент
hash_table.remove("apple")
hash_table.display()
