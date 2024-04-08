# 3. Дано четырехзначное число. Найти:
# а) сумму его цифр;
# б) произведение его цифр.

# Получаем трехзначное число
number = int(input("Введите четырехзначное число: "))

# Разделяем число на цифры и присваиваем их переменным
thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
digits = number % 10

# Вычисляем сумму чисел
sum_of_digits = thousands + hundreds + tens + digits
# Вычисляем произведение чисел
multy_of_digits = thousands * hundreds * tens * digits

# Выводим результат на экран
print(f"Введено число {number} сумма его цифр: {sum_of_digits}, произведение его цифр: {multy_of_digits}")