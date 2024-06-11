# 11.182. Известно, что в массиве имеются нулевые элементы.
# Напечатать:
# а) все элементы, кроме первого из них;
# б) все элементы, кроме последнего из них.


def all_not_first_number(array):
    for i in range(len(array)):
        if array[i] % 10 == 0:
            array.remove(array[i])
            break
    print(array)

def all_not_last_number(array):
    array.reverse()
    for i in range(len(array)):
        if array[i] % 10 == 0:
            array.remove(i)
            break
    array.reverse()
    print(array)

def all_not_last_number_old(array):
    flag = True
    for i in range(len(array)):
        if array[i] % 10 == 0 and flag:
            flag = False
            continue
        print(array[i])



def main():
    array = [1, 2, 20, 4, 5, 0, 5, 0, 8, 0, 10]
    array2 = array[:]
    all_not_first_number(array)
    all_not_last_number(array2)

main()
