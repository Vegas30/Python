# Дано трехзначное число, в котором все цифры различны. Получить
# шесть чисел, образованных при перестановке цифр заданного числа.

# Запрашиваем у пользователя трехзначное число
number = int(input("Введите трехзначное число с различными цифрами: "))

# Извлекаем цифры числа
hundreds = number // 100
tens = (number // 10) % 10
digits = number % 10

# Формируем все возможные перестановки цифр
perm1 = hundreds * 100 + tens * 10 + digits
perm2 = hundreds * 100 + digits * 10 + tens
perm3 = tens * 100 + hundreds * 10 + digits
perm4 = tens * 100 + digits * 10 + hundreds
perm5 = digits * 100 + hundreds * 10 + tens
perm6 = digits * 100 + tens * 10 + hundreds

# Выводим все перестановки
print("Все возможные перестановки цифр:", perm1, perm2, perm3, perm4, perm5, perm6, sep="\n")
