# 11.29. Дан массив целых чисел. Выяснить:
# а) верно ли, что сумма элементов массива есть четное число;
# б) верно ли, что сумма квадратов элементов массива есть
# пятизначное число.

import random


def input_array(n):
    array = []
    for _ in range(n):
        array.append(random.randint(0, 10))
    return array

def summ_elem_is_even(array):
    summ = sum(array)
    if summ % 2 == 0:
        print(f"Верно, сумма элементов массива {summ} есть четное число")
    else:
        print(f"Не верно, сумма элементов массива {summ} не четное число")


def main():
    array_new = input_array(10)
    print(array_new)
    summ_elem_is_even(array_new)

main()
