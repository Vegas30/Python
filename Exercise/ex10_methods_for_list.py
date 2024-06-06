# 10.Создайте список из чисел от 1 до 10, дублируя каждое число
# трижды. Напишите функцию, которая удаляет все вхождения числа 5.

def dobav_element(array):
    for i in array:
        if i == 5:
            array.remove(i)


def main():
    array1 = [1, 2, 3, 4, 5, ] * 3
    print(array1)
    dobav_element(array1)
    print(array1)


main()