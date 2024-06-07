# 1. Создайте список чисел от 1 до 5. Затем добавьте к этому
# списку квадраты чисел от 6 до 10 с помощью цикла.
def dobav_element(arr):
    arr = arr.copy()
    for i in range(6, 10 + 1):
        arr.append(i * i)
    return arr


def main():
    array = [1, 2, 3, 4, 5]
    arr = dobav_element(array)
    print(array, arr)


main()
