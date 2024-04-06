# Дано четырехзначное число. Найти:
# а) сумму его цифр;
# б) произведение его цифр.

number = int(input("Введите четырехзначное число: "))

thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
digits = number % 10

sum_of_digits = thousands + hundreds + tens + digits
multy_of_digits = thousands * hundreds * tens * digits

print(f"Введено число {number} сумма его цифр: {sum_of_digits}, произведение его цифр: {multy_of_digits}")