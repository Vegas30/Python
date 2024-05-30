# 11.4. Массив предназначен для хранения значений ростов двенадцати
# человек. С помощью датчика случайных чисел заполнить массив
# целыми значениями, лежащими в диапазоне от 163 до 190
# включительно.
import random


def list_height(people):
    list = []
    for _ in range(12):
        list.append(random.randint(169, 190))
    return list

def main():
    people = 12
    array = list_height(people)
    print("Список с ростом 12 человек: ", array)


if __name__ == '__main__':
    main()