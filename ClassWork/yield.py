# 1. Напишите генератор, который возвращает первые n чисел Фибоначчи

def fibonachi(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# 2. Релизуйте функцию-генератор, которая будет возвращать все четные числа до конца значения n

def even_numbers(n):
    for num in range(1, n):
        if num % 2 == 0:
            yield num


# 3. Напишите генератор, который будет возвращать простые числа до значения n.
import math


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_numbers(n):
    for num in range(2, n + 1):
        if is_prime(num):
            yield num


# 4. Реализуем функцию-генератор, которая возвращает строки, начинающиеся на букву

def replace_letter(str, letter):
    for element in str:
        if element.startswith(letter):
            yield element
        # if element[0] == letter:
        #     yield element


# 5. Реализуйте функцию-генератор, которая возвращает текущую сумму элементов списка
def summa_element(numbers):
    total = 0
    for num in numbers:
        total += num
        yield total


# 6. Напишите генератор, который возвращает числа от 1 до n, которые делятся на 3
# или оканчиваются цифрой 7.
def del_3_or_end_7(n):
    for elem in range(1, n + 1):
        if elem % 3 == 0 or elem % 10 == 7:
            yield elem

        if elem % 3 == 0 or (str(elem)[-1]) == '7':
            yield elem

        if elem % 3 == 0 or str(elem).endswith('7'):
            yield elem


# 7. Реализуйте функцию-генератор, которая возвращает числа в отсортированном виде.
print()


def sorted_numbers(n):
    for elem in sorted(n):
        yield elem


def main():
    # n = 10
    #
    # # 0,1,1,2,3,5,8,13
    # for num in fibonachi(n):
    #     print(num)
    #
    # print(list(fibonachi(n)))
    #
    # for num in even_numbers(n):
    #     print(num)
    #
    # for prime in prime_numbers(n):
    #     print(prime)

    str = ['арбуз', 'помидор', 'ананас', 'аPython', 'бPython']
    letter = 'a'
    for elem in replace_letter(str, letter):
        print(elem)

    numbers = [1, 2, 3, 4, 5]
    summa_element(numbers)
    for num in summa_element(numbers):
        print(num)

    n = 10
    for num in del_3_or_end_7(n):
        print(num, end=' ')

    n = [5, 3, 8, 1, 2]

    for num in sorted_numbers(n):
        print(num)


if __name__ == '__main__':
    main()
