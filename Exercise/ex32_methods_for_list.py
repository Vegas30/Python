# 32.Создайте список из чисел от 1 до 5. Скопируйте его и удалите все
# чётные числа из копии. Убедитесь, что оригинальный список не
# изменился.


def del_element(array):
    for i in range(len(array) - 1, 0, -2):
        print(array.pop(i))


def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(array)
    del_element(array)


main()
