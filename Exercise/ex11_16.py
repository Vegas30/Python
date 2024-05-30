# 11.16. Дан массив целых чисел. Выяснить:
#            а) является ли s-й элемент массива положительным числом;
#            б) является ли k-й элемент массива четным числом;
#            в) какой элемент массива больше: k-й или s-й.
import random
def input_list(n):
    list = []
    for _ in range(n):
        list.append(random.randint(-100,100))
    return list

def sravn_k_s_elements(array,s,k):
    return max(array[s], array[k])

def list_K_chet(array, n, k):
        if not (-n <= k < n):
            print("Ошибка ввода индекса. Выход за массив!")
        else:
            if array[k] % 2 == 0:
                print("Является.")
            else:
                print("Не является.")

def list_S_sign(array, s):
        if array[s] > 0:
            print("Является.")
        else:
            print("Не является.")

def main():
    n = int(input("Введите количество элементов массива"))
    array = input_list(n)
    print("Исходный массив: ", array)

    s = int(input("Введите индекс элемента для его проверки: "))
    if not( -n <= s < n):
        print("Ошибка ввода индекса. Выход за массив!")
    else:
        list_S_sign(array, s)

    k = int(input("Введите индекс элемента для его проверки: "))
    list_K_chet(array,n,k)

    result = sravn_k_s_elements(array,s,k)
    print("Наибольший элемент равен", result)
main()