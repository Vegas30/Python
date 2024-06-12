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


# а)
def summ_elem_is_even(array):
    summ = sum(array)
    if summ % 2 == 0:
        print(f"Верно, сумма элементов массива {summ} есть четное число")
    else:
        print(f"Не верно, сумма элементов массива {summ} не четное число")


# б)
def summ_of_squares_is_5_dig_num(array):
    summ = 0
    for elem in array:
        summ += elem ** 2
    print(f"Сумма квадратов элементов массива: {summ}")
    summ_len = len(str(summ))
    if summ_len == 5:
        print("Верно, сумма квадратов элементов массива есть пятизначное число")
    else:
        print("Не верно, сумма квадратов элементов массива не пятизначное число")


def main():
    n = int(input("Введите длину массива: "))

    array_new = input_array(n)

    print("Наш массив: ", array_new)
    print("а)")
    summ_elem_is_even(array_new)
    print("\nв)")
    summ_of_squares_is_5_dig_num(array_new)


main()
