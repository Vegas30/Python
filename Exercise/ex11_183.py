# 11.183. Дан массив, упорядоченный по возрастанию, и число a, о
# котором известно следующее: оно не равно ни одному из элементов
# массива, больше первого и меньше последнего элемента.
# а) Вывести все элементы массива, меньшие a.
# б) Найти два элемента массива (их порядковые номера и
# значение), в интервале, между которыми находится значение n
# в) Найти элемент массива (его порядковый номер и значение),
# ближайший к a.


def find_a(array):
    first_elem = array[0]
    last_elem = array[len(array)-1]

    for elem in array:
        if first_elem < elem < last_elem and array.count(elem) == 1:
            return elem


def find_all_min_a():
    pass


def main():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



main()
