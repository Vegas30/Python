# 54.Создайте два списка чисел одинаковой длины. Напишите программу,
# которая создаёт список произведений пар элементов из обоих
# списков.


def dobav_element(x, y):
    return x * y


def main():
    array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = list(map(dobav_element, array1, array2))
    print(result)

    # result2 = []
    #     for i in range(min(len(array1), len(array2))):
    #         list1 = result2.append(array1[i] * array2[i])



main()
