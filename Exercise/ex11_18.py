# 11.18. Дан массив. Все его элементы:
#           а) перевернуть список;
#           б) умножить на последний элемент;
#           в) увеличить на число В.
import random


def input_list(n):
    list = []
    for _ in range(n):
        list.append(random.randint(-100, 100))
    return list


def reverse_list(array):
    return reversed(array)


def multiply_list(array):
    # [1,2,3,4] -> [4,8,12,16]
    unit = array[-1]
    list = []
    for i in array:
        list.append(i * unit)
    return list


def sum_B(array, B):
    # [1,2,3,4] -> B = 2 -> [3,4,5,6]
    list = []
    for i in array:
        list.append(i + B)
    return list


def main():
    n = int(input("Введите количество элементов массива"))
    array = input_list(n)
    print("Исходный массив: ", array)

    print("\n")

    result_array = reverse_list(array)
    print("Перевернутый:", list(result_array), "\nИсходный:", array)
    print("\n")
    list_mult = multiply_list(array)
    print("Массив умноженный: ", list_mult, "\nИсходный:", array)
    print("\n")
    B = int(input("Введите число B: "))
    list_B = sum_B(array, B)
    print("Массив + B: ", list_B, "\nИсходный:", array)


main()
