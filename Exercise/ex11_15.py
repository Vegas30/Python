# 11.15. Дан массив. Составить программу:
# а) расчета квадратного корня из любого элемента массива;
# б) расчета среднего арифметического двух любых элементов
# массива.

import random


def input_array(n):
    array = []
    for _ in range(n):
        array.append(random.randint(50, 100))
    return array


def sqrt_array_unut():
    pass


def main():
    n = int(input("Введите количество элементов в списке: "))
    array = input_array(n)

    nomer = int(input("Введите номер элемента для извлечения из "))
main()
