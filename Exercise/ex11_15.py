# 11.15. Дан массив. Составить программу:
# а) расчета квадратного корня из любого элемента массива;
# б) расчета среднего арифметического двух любых элементов
# массива.

import random
import math


def input_array(n):
    array = []
    for _ in range(n):
        array.append(random.randint(50, 100))
    return array


def sqrt_array_unit(index, array, n):
    # for i in range(n):
    #     if i == index:
    #         array[i] = math.sqrt(array[i])
    # return array
    #
    # array[index] = math.sqrt(array[index])

    array.insert(index, math.sqrt(array[index]))
    return array


def main():
    n = int(input("Введите количество элементов в списке: "))
    array = input_array(n)
    print("Исходный массив", array)
    nomer = int(input("Введите номер элемента для извлечения из него корня: "))
    result = sqrt_array_unit(nomer - 1, array, n)
    print(result)


main()
