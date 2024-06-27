# 11.38. Дан массив натуральных чисел. Напечатать:
# а) все элементы массива, являющиеся двузначными числами;
# б) все элементы массива, являющиеся трехзначными числами.
import random

# a)
def print_two_digit_num(arr):
    result_arr = []
    for elem in arr:
        if 10 <= elem <= 99:
            result_arr.append(elem)
    print(result_arr)
# б)
def print_tree_digit_num(arr):
    result_arr = []
    for elem in arr:
        if 100 <= elem <= 999:
            result_arr.append(elem)
    print(result_arr)

def main():
    array = [random.randint(1, 1000) for _ in range(20)]
    print("Наш массив натуральных чисел: ", array)

    print("\nа) все элементы массива, являющиеся двузначными числами: ")
    print_two_digit_num(array)

    print("\nб) все элементы массива, являющиеся трехзначными числами: ")
    print_tree_digit_num(array)


if __name__ == '__main__':
    main()
