# Пользователь вводит с клавиатуры три числа. Первое
# число — зарплата за месяц, второе число — сумма месячного платежа по
# кредиту в банке, третье число — задолженность за коммунальные услуги.
# Необходимо вывести на экран сумму, которая останется у пользователя
# после всех выплат.

# Запросить у пользователя данные
salary = float(input("Введите зарплату за месяц: "))
credit_payment = float(input("Введите сумму месячного платежа по кредиту: "))
utilities_debt = float(input("Введите задолженность за коммунальные услуги: "))

# Вычислить оставшуюся сумму после всех выплат
remaining_money = salary - credit_payment - utilities_debt

# Вывести результат
print(f"Сумма, которая останется после всех выплат: {remaining_money}")
