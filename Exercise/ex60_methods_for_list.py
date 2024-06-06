# 60.Создайте список случайных чисел. Напишите программу, которая
# проверяет, есть ли в списке хотя бы одно отрицательное число и все
# ли числа положительные.
import random


def input_array(n):
    array = []
    for _ in range(n):
        array.append(random.randint(-3, 10))
    return array

def odd_even(array):

    for i in array:
        if i<0:
            print("Есть отрицательные")
            break
    else:
        print("Все положительные")


def main():

    n = random.randint(5, 10)
    array = input_array(n)
    odd_even(array)
    print(array)


main()
