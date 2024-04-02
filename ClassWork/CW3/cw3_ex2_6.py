number = int(input("Введите двузначное число: "))
# а)

tens = number // 10 #23 // 10 = 2
digits = number % 10 #23 % 10 = 3
sum_tens_and_digits = tens + digits
multy_tens_and_digits = tens * digits
print(f"В нашем числе {number} находится {tens} - десятков и {digits} - единиц")
print(f"Сумма цифр в числе равна {sum_tens_and_digits}")
print(f"Произведение цифр в числе равна {multy_tens_and_digits}")
