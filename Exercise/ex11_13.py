import random


def input_list(n):
    list = []
    for _ in range(n):
        list.append(random.randint(-100, 100))
    return list


def list_search_index(array, n):
    index = int(input("Введите индекс желаемого элемента массива: "))
    if not (-n <= index < n):
        print("Ошибка ввода индекса. Выход за пределы массива")
    else:
        return array[index]


def main():
    n = int(input("Введите количество элементов массива"))
    array = input_list(n)
    print("Исходный массив: ", array)
    result_number = list_search_index(array, n)
    print("Элемент массива под выбранным индексом = ", result_number)


main()
