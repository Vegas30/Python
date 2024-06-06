# 5. Создайте два списка разной длины. Напишите функцию, которая
# объединяет их, добавляя элементы второго списка в первый
# поэлементно (например, первый элемент второго списка к первому
# элементу первого списка, и так далее).

def dobav_element(arr1, arr2):
    result = []
    for i in range(max(len(arr2), len(arr1))):
        if i < len(arr1):
            result.append(arr1[i])
        if i < len(arr2):
            result.append(arr2[i])
    return result


def main():
    array1 = [1, 2, 3, 4, 5]
    array2 = [7, 3, 4]
    result = dobav_element(array1, array2)
    print(result)


main()
