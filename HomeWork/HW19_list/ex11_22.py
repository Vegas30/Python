# 11.22. В массиве хранятся сведения о стоимости 12 различных
# предметов. Определить общую стоимость всех предметов.

import random


def input_array(n):
    array = []
    for _ in range(n):
        array.append(random.randint(0, 100))
    return array


def total_summ(array):
    return sum(array)


def main():
    n = int(input("Введите длину массива: "))

    array_new = input_array(n)

    print("Наш массив: ", array_new)

    result = total_summ(array_new)

    print(f"Общая стоимость всех предметов: {result}")
