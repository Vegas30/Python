# 6.27. Дано натуральное число.
# а) Определить его максимальную и минимальную цифры.
# б) Определить, на сколько его максимальная цифра превышает
# минимальную.
# в) Найти сумму его максимальной и минимальной цифр

def max_and_min(number):
    maks = number % 10
    minn = number % 10
    while number > 0:
        unit = number % 10
        number //= 10
        maks = max(maks, unit)
        minn = min(minn, unit)
