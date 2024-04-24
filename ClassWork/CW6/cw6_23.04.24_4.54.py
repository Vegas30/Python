# 4.54. Дата некоторого дня характеризуется тремя натуральными числами:
# g (год), m (порядковый номер месяца) и n (число). По заданным g, n и m определить:
# а) дату предыдущего дня;
# б) дату следующего дня.
# В обеих задачах рассмотреть два случая:
# 1) заданный год не является високосным;
# 2) заданный год может быть високосным.

g = 2024  # Пример года
m = 2     # Пример месяца
n = 28    # Пример числа

# Проверяем, является ли год високосным
is_leap_year = (g % 4 == 0 and g % 100 != 0) or (g % 400 == 0)

# Определяем количество дней в месяце
if m in [1, 3, 5, 7, 8, 10, 12]:
    days_in_month = 31
elif m in [4, 6, 9, 11]:
    days_in_month = 30
elif m == 2:
    if is_leap_year:
        days_in_month = 29
    else:
        days_in_month = 28
else:
    days_in_month = 0  # Неверный месяц

# Находим предыдущий день
if n > 1:
    prev_day = n - 1
    prev_month = m
    prev_year = g
elif m > 1:
    prev_month = m - 1
    if prev_month in [1, 3, 5, 7, 8, 10, 12]:
        prev_day = 31
    elif prev_month in [4, 6, 9, 11]:
        prev_day = 30
    elif prev_month == 2:
        if is_leap_year:
            prev_day = 29
        else:
            prev_day = 28
    prev_year = g
else:
    prev_day = 31
    prev_month = 12
    prev_year = g - 1

# Находим следующий день
if n < days_in_month:
    next_day = n + 1
    next_month = m
    next_year = g
elif m < 12:
    next_day = 1
    next_month = m + 1
    next_year = g
else:
    next_day = 1
    next_month = 1
    next_year = g + 1

print("Предыдущий день:", prev_year, prev_month, prev_day)
print("Следующий день:", next_year, next_month, next_day)
