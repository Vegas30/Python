# 6.5. Дана последовательность целых чисел a1,a2,...,a18 в начале
# которой записано несколько равных между собой элементов.
# Определить количество таких элементов последовательности.
# Условный оператор не использовать.

def calculate_some():
    count = 1
    count_while = 0
    number = int(input("Введите первый элемент последовательности: "))
    number_next = int(input("Введите следующий элемент последовательности: "))
    while number == number_next and count_while <= 18:
        count += 1
        number_next = int(input("Введите следующий элемент последовательности: "))
    return count


def calculate_some2():
    count = 0
    count_while = 0
    number = int(input("Введите первый элемент последовательности: "))
    num_temp = number
    while number == num_temp and count_while <= 18:
        count += 1
        count_while += 1
        number = int(input("Введите следующий элемент последовательности: "))
    return count

def main():
    result = calculate_some2()
    print(result)

if __name__ == '__main__':
    main()