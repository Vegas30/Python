# 1. Создайте список всех чисел от 1 до 30 включительно, которые
# делятся на 3.
result_list = [num for num in range(1, 31) if num % 3 == 0]
print("1.", result_list)
# 2. Создайте список цифр числа 12345.
number_list = [int(digit) for digit in str(12345)]
print("2.", number_list)
# 3. Создайте список сумм цифр чисел от 10 до 20 включительно.
sum_digits_list = [sum(int(digit) for digit in str(num)) for num in range(10, 21)]
print("3.", sum_digits_list)
# 4. Создайте список всех чисел от 1 до 50 включительно, которые
# содержат цифру 3. (‘3’ in str(13) подсказка интересного решения)
num_list_3 = [num for num in range(1, 51) if '3' in str(num)]
print("4.", num_list_3)
# 5. Создайте список кортежей, где каждый кортеж состоит из числа от 1
# до 10 включительно и его квадрата.
tuple_list = [(num, num ** 2) for num in range(1, 11)]
print("5.", tuple_list)
# 6. Напишите lambda-функцию, которая принимает два числа и
# возвращает их произведение.
multiply = lambda x, y: x * y
num1 = 5
num2 = 3
result = multiply(num1, num2)
print(f"6. Произведение чисел {num1} и {num2} равно {result}")
# 7. Напишите lambda-функцию, которая принимает три числа и
# возвращает их сумму.
sum_three_numbers = lambda x, y, z: x + y + z
num1 = 2
num2 = 4
num3 = 6
result = sum_three_numbers(num1, num2, num3)
print(f"7. Сумма чисел {num1}, {num2}, и {num3} равна {result}")
# 8. Напишите lambda-функцию, которая принимает два логических
# значения и возвращает их логическое И.
logical_and = lambda x, y: x and y
value1 = True
value2 = False
result = logical_and(value1, value2)
print(f"8. Логическое И между {value1} и {value2} равно {result}")
# 9. Используйте lambda и функцию filter(), чтобы оставить в списке
# только числа, кратные 4.
num_list = [num for num in range(1, 41)]
result_list = list(filter(lambda x: x % 4 == 0, num_list))
print("9.", result_list)
# 10. Используйте lambda и функцию map(), чтобы возвести каждый
# элемент в списке в куб.
num_list = [num for num in range(1, 11)]
result_list = list(map(lambda x: x ** 3, num_list))
print("10.", result_list)
