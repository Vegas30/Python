# 11.19. Определить:
# а) сумму всех элементов массива;
# б) произведение всех элементов массива;
# в) сумму квадратов всех элементов массива;
# г) сумму шести первых элементов массива;
# д) сумму элементов массива с k1-го по k2-й (значения k1 и k2
# вводятся с клавиатуры; k2 > k1);
# е) среднее арифметическое всех элементов массива;
# ж) среднее арифметическое элементов массива с s1-го по s2-й (значения s1 и s2
# вводятся с клавиатуры; s2 > s1).
import random


def create_list(n):
    list_new = []
    for _ in range(n):
        list_new.append(random.randint(-100, 100))
    return list_new


# а)
def summ_all_elements(array):
    summ = 0
    for i in array:
        summ += i
    return summ


# б)
def multiply_all_elements(array):
    result = 1
    for i in array:
        if i == 0:
            result = 0
            print("Обнуление!")
            break
        result *= i
    return result


# в)
def sum_of_squares_all_elements(array):
    summ = 1
    for i in array:
        summ += i ** 2
    return summ


# г)
def summ_first_6_elements(array):
    summ = 0
    for i in range(0, 6):
        summ += array[i]
    return summ


# д)
def summ_from_k1_to_k2_elements(array, k1, k2):
    if not 0 <= k1 < k2 < len(array):
        print("Ошибка: убедитесь, что 0 <= k1 < k2 <= размеру списка и k2 > k1.")
    else:
        summ = 0
        for i in range(k1, k2 + 1):
            summ += array[i]
        return summ


def main():
    n = int(input("Введите количество элементов массива: "))
    array = create_list(n)
    print("Исходный массив: ", array)

    print("\n")
    #
    # summ_array = summ_all_elements(array)
    # print("а) сумма всех элементов массива: ", summ_array, "\nИсходный:", array)
    # print("\n")
    #
    # multiply_array = multiply_all_elements(array)
    # print("б) произведение всех элементов массива: ", multiply_array, "\nИсходный:", array)
    # print("\n")
    #
    # sum_of_squares_array = sum_of_squares_all_elements(array)
    # print("в) сумму квадратов всех элементов массива: ", sum_of_squares_array, "\nИсходный:", array)
    # print("\n")

    # summ_6_elem_array = summ_first_6_elements(array)
    # print("г) сумму шести первых элементов массива: ", summ_6_elem_array, "\nИсходный:", array)
    # print("\n")

    k1 = int(input("Введите начальный индекс k1 (начиная с 0): "))
    k2 = int(input(f"Введите конечный индекс k2 (меньше {len(array)}): "))
    summ_from_k1_to_k2_elem_array = summ_from_k1_to_k2_elements(array, k1, k2)
    print("д) сумму элементов массива с k1-го по k2-й: ", summ_from_k1_to_k2_elem_array, "\nИсходный:", array)
    print("\n")


if __name__ == '__main__':
    main()
