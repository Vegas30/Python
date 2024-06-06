# 18.Создайте список случайных чисел. Напишите функцию, которая
# очищает список, если количество чётных чисел больше нечётных.

def even(array):
    coun = 0
    for i in array:
        if i % 2 == 0:
            coun += 1
    return coun

def odd(array):
    coun = 0
    for i in array:
        if i % 2 != 0:
            coun += 1
    return coun

def dobav_element(array):
    if odd(array) < even(array):
        array.clear()

def main():
    array = [1,2,2,2,5]
    print(array)
    dobav_element(array)
    print(array)

main()

