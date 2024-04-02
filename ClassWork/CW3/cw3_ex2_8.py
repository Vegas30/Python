# Дано трехзначное число.Найти:
# а) число единиц в нем;
# б) число десятков в нем;
# в) сумму его цифр;
# г) произведение его цифр;


number = int(input("Введите трехзначное число: "))
hundreds = number // 100
tens = (number // 10) % 10
digits = number % 10
sum_digits = digits + tens + hundreds
multy_digits = digits * tens * hundreds

new_number = digits * 10 + tens

print(f"Сумма цифр: {sum_digits}")
print(f"Произведение цифр: {multy_digits}")

