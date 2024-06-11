# 11.180. Известно, что в массиве имеются элементы, равные 5.
# Определить:
# а) номер первого из них;
# б) номер последнего из них.
# В обеих задачах условный оператор не использовать.

def first_number(array):
    first_numdber = array.index(5) + 1
    return first_numdber


def last_number(array):
    last_number = (len(array) - 1 - (array[::-1].index(5))) + 1
    return last_number


def first_and_last_number_cycle(array):
    first_index = None
    last_index = None
    for i in range(len(array)):
        if array[i] == 5:
            if first_index is None:
                first_index = i
            last_index = i
    first_num = first_index + 1
    last_num = last_index + 1
    return first_num, last_num


def main():
    array = [1, 2, 3, 4, 5, 6, 5, 7, 8, 9, 10]
    # first_5 = first_number(array)
    # print(first_5)
    # last_5 = last_number(array)
    # print(last_5)
    first_5, last_5 = first_and_last_number_cycle(array)
    print(first_5, last_5)

main()
