# 6.9. Среди чисел 1, 4, 9, 16, 25, ... найти первое число, большее n.
def find_next_number(n):
    i = 1
    while True:
        current_number = i ** 2
        if current_number > n:
            return current_number
        i += 1


# 6.10. Дано число n.
# а) Напечатать те натуральные числа, квадрат которых не
# превышает n.
def print_squares_less_than_n(n):
    i = 1
    while i ** 2 <= n:
        print(i, end=" ")
        i += 1


# б) Найти первое натуральное число, квадрат которого больше n.
def find_first_square_greater_than_n(n):
    i = 1
    while True:
        current_number = i ** 2
        if current_number > n:
            return current_number
        i += 1


# 6.21. Последовательность Фибоначчи образуется так: первый и
# второй члены последовательности равны 1, каждый следующий равен
# сумме двух предыдущих (1, 1, 2, 3, 5, 8, 13, ...). Найти:
# а) первое число в последовательности Фибоначчи, большее n
# (значение n вводится с клавиатуры; n > 1);
def find_first_fibonacci_number_greater_than_n(n):
    a, b = 1, 1
    while True:
        a, b = b, a + b
        if b > n:
            return b


# б) сумму всех чисел в последовательности Фибоначчи, которые
# не превосходят 1000.
def sum_fibonacci_numbers_not_exceeding_limit(limit):
    a, b = 1, 1
    total_sum = 0
    while a < limit:
        total_sum += a
        a, b = b, a + b
    return total_sum


# 6.22. Дано натуральное число. Определить:
# а) количество цифр 3 в нем;
def count_num_3(number):
    # count = str(number).count('3')
    count = 0
    for num in str(number):
        if num == '3':
            count += 1
    return count


# б) сколько раз в нем встречается последняя цифра;
def count_last_digit(number):
    # last_digit = str(number)[-1]
    # count = str(number).count(last_digit)
    count = 0
    last_digit = number % 10
    for digit in str(number):
        if digit == str(last_digit):
            count += 1
    return count


# в) количество четных цифр в нем. Составное условие и более
# одного неполного условного оператора не использовать;
def count_even_digits(number):
    # count = sum(1 for digit in str(number) if int(digit) % 2 == 0)
    count = 0
    for digit in str(number):
        if int(digit) % 2 == 0:
            count += 1
    return count


# г) сумму его цифр, больших пяти;
def sum_digits_greater_than_5(number):
    # summa = sum(int(digit) for digit in str(number) if int(digit > 5))
    summa = 0
    for digit in str(number):
        if int(digit) > 5:
            summa += int(digit)
    return summa


# д) произведение его цифр, больших семи;
def product_digits_greater_than_7(number):
    product = 1
    for digit in str(number):
        if int(digit) > 7:
            product *= int(digit)
    return product


# е) сколько раз в нем встречаются цифры 0 и 5 (всего).
def count_0_and_5(number):
    # count = str(number).count('0') + str(number).count('5')
    count = 0
    for digit in str(number):
        if digit == '0' or digit == '5':
            count += 1
    return count


# 6.24. Дана непустая последовательность целых чисел,
# оканчивающаяся нулем. Найти:
# а) сумму всех чисел последовательности, больших числа x;
def sum_greater_than_x(sequence, x):
    # summa = sum(num for num in sequence if num > x)
    summa = 0
    for num in sequence:
        if num > x:
            summa += num
    return summa


# б) количество всех четных чисел последовательности.
def count_even_numbers(sequence, x):
    # count = sum(1 for num in sequence if num % 2 == 0)
    count = 0
    for num in sequence:
        if num % 2 == 0:
            count += 1
    return count


# 6.27. Дано натуральное число.
# а) Определить его максимальную и минимальную цифры.
def min_max_digit(number):
    min_digit = 9
    max_digit = 0
    for digit in str(number):
        if int(digit) < min_digit:
            min_digit = int(digit)
        if int(digit) > max_digit:
            max_digit = int(digit)

    return min_digit, max_digit


# б) Определить, на сколько его максимальная цифра превышает
# минимальную.
def diff_max_min(min_dig, max_dig):
    if min_dig < max_dig:
        return max_dig - min_dig


# в) Найти сумму его максимальной и минимальной цифр.
def sum_min_max(min_dig, max_dig):
    return min_dig + max_dig

def get_natural_number(text):
    while True:
        try:
            number = int(input(text))
            if number > 0:
                return number
            # else:
            #     print(text)
        except ValueError as e:
            print(f"Ошибка! {text}", e)


def main():
    # 6.9.
    result = find_next_number(24)
    print("№ 6.9", result)
    # 6.10. а)
    print("№ 6.10 а)", end=" ")
    print_squares_less_than_n(42)
    # 6.10. б)
    result = find_first_square_greater_than_n(42)
    print("\n№ 6.10 б)", result)
    # 6.21. а)
    text = "Введите значение n (n > 1): "
    n = get_natural_number(text)
    result = find_first_fibonacci_number_greater_than_n(n)
    print("№ 6.21 а)", result)
    # 6.21. б)
    limit = 1000
    result = sum_fibonacci_numbers_not_exceeding_limit(limit)
    print("№ 6.21 б)", result)
    # 6.22. а)
    text = "Введите натуральное число: "
    number = get_natural_number(text)
    result = count_num_3(number)
    print("№ 6.22 а)", result)
    # 6.22. б)
    result = count_last_digit(number)
    print("№ 6.22 б)", result)
    # 6.22. в)
    result = count_even_digits(number)
    print("№ 6.22 в)", result)
    # 6.22. г)
    result = sum_digits_greater_than_5(number)
    print("№ 6.22 г)", result)
    # 6.22. д)
    result = product_digits_greater_than_7(number)
    print("№ 6.22 д)", result)
    # 6.22. е)
    result = count_0_and_5(number)
    print("№ 6.22 е)", result)
    # 6.24. а)
    sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    x = 3
    result = sum_greater_than_x(sequence, x)
    print("№ 6.24 а)", result)
    # 6.24. б)
    result = count_even_numbers(sequence, x)
    print("№ 6.24 б)", result)
    # 6.27. а)
    number = 987654321
    min_dig, max_dig = min_max_digit(number)
    print(f"№ 6.27 а) Минимальная цифра: {min_dig}, максимальная цифра: {max_dig}")
    # 6.27. б)
    result = diff_max_min(min_dig, max_dig)
    print(f"№ 6.27 б) Максимальная цифра: {max_dig} превышает минимальную цифру: {min_dig} на {result}")
    # 6.27. в)
    result = sum_min_max(min_dig, max_dig)
    print(f"№ 6.27 в) Сумма максимальной цифры: {max_dig} и минимальной цифры: {min_dig} равна {result}")


if __name__ == '__main__':
    main()
