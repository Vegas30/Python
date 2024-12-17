# Реализация хэш-таблицы с методом цепочек
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Создаем пустые цепочки


    def _hash(self, key):
        return hash(key) % self.size  # Вычисляем индекс через хэш


    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Обновляем значение, если ключ уже существует
                return
        self.table[index].append([key, value])  # Добавляем новую пару


    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # Возвращаем значение по ключу
        return None


    def remove(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]  # Удаляем пару
                return


# Пример использования
hash_table = HashTable(8)
hash_table.insert("apple", 100)
hash_table.insert("banana", 200)
hash_table.insert("cherry", 300)


print(hash_table.get("apple"))   # Вывод: 100
print(hash_table.get("banana"))  # Вывод: 200
hash_table.remove("apple")
print(hash_table.get("apple"))   # Вывод: None
