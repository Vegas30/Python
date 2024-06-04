# 11.144. Дан массив. Поменять местами:
# а) второй и пятый элементы;
# б) m-й и n-й элементы;
# в) третий и максимальный элементы. Если элементов с
# максимальным значением несколько, то в обмене должен участвовать
# первый из них;
# г) первый и минимальный элементы. Если элементов с
# минимальным значением несколько, то в обмене должен участвовать
# последний из них.
import random


def input_list(n):
    list = []
    for _ in range(n):
        list.append(random.randint(-100, 100))
    return list


def output_list(array):
    print("Массив после воздействия: ", array)


def change_elements(array, n, m):
    n_index = array.index(n)
    m_index = array.index(m)
    array[n_index], array[m_index] = m, n
    output_list(array)


def change_3_elements_and_max_elements(array):
    elements_3 = array[2]
    maximum_element = max(array)
    maximum_index_element = array.index(maximum_element)
    array[2], array[maximum_index_element] = maximum_element, elements_3


def main():
    n_array = int(input("Введите кол-во элементов массива: "))
    array = input_list(n_array)
    output_list(array)
    m = int(input("Введите первый элемента для обмена: "))
    n = int(input("Введите второй элемента для обмена: "))
    change_elements(array, n, m)
    change_3_elements_and_max_elements(array)


main()
