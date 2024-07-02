# 11.37. Дан массив целых чисел. Напечатать:
# а) все четные элементы;
# б) все элементы, оканчивающиеся нулем.
import random

# a)
def print_all_even(arr):
    result_arr = []
    for elem in arr:
        if elem % 2 == 0:
            result_arr.append(elem)
    print(result_arr)
# б)
def print_all_zeroend(arr):
    result_arr = []
    for elem in arr:
        if elem % 10 == 0:
            result_arr.append(elem)
    print(result_arr)

def main():
    array = [random.randint(-100, 100) for _ in range(20)]
    print("Наш массив целых чисел: ", array)

    print("\nа) все четные элементы: ")
    print_all_even(array)

    print("\nб) все элементы, оканчивающиеся нулем: ")
    print_all_zeroend(array)


if __name__ == '__main__':
    main()
