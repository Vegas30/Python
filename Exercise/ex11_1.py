# 11.1. Заполнить массив из восьми элементов следующими
# значениями: первый элемент массива равен 37, второй — 0, третий —
# 50, четвертый — 46, пятый — 34, шестой — 46, седьмой — 0,
# восьмой —13.

def input_array(array):
    for _ in range(8):
        array.append(int(input("Введите число: ")))
    return array


def main():
    array = []
    array = input_array(array)
    print(array)

main()