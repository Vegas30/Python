# Дано трехзначное число. Найти число, полученное при прочтении его цифр справа налево

number = int(input("Введите трехзначное число: "))
hundreds = number // 100
tens = (number // 10) % 10
digits = number % 10

new_number = (digits * 100) + tens * 10 + hundreds

print(f"Новое число: {new_number}")
