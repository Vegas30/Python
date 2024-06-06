# 51.Создайте список чисел от 1 до 10. Напишите программу, которая
# создаёт новый список, содержащий только те элементы, чьи индексы
# чётные.

def dobav_element(n):
    return n % 2 != 0


def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(array)
    list1 = list(filter(dobav_element, array))
    print(list1)


main()
