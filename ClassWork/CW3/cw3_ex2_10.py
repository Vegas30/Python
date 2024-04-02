# Дано трехзначное число. В нем зачеркнули первую слева цифру и приписали ее в конце. Найти полученное число.

number = int(input("Введите трехзначное число: "))
hundreds = number // 100
tens = (number // 10) % 10
digits = number % 10

new_number = tens * 100 + digits * 10 + hundreds
new_number2 = digits * 100 + hundreds * 10 + tens

print(f"Новое число: {new_number}")
print(f"Новое число: {((number // 10) % 10) *100 + (number % 10) * 10 + number // 100}")

print(f"Второе новое число: {(number % 10) * 100 + (number // 100) * 10 + (number // 10) % 10}")
