# Создаем список
my_list = [1, 2, 3]

# Получаем итератор для списка
my_iterator = iter(my_list)

# Итерируем через список с помощью итератора
try:
    while True:
        # Получаем следующий элемент
        element = next(my_iterator)
        print(element)
except StopIteration:
    # Если элементы закончились, перехватываем исключение StopIteration
    print("Итерация завершена")

for element in my_list:
    print(element)
