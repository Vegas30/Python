# 2.14. Дано трехзначное число, в котором все цифры различны.
# Получить шесть чисел, образованных при перестановке цифр заданного числа.
number = 111
if not 100<=number<=999:
    print("Число не трехзначное")
else:
    digit = number % 10
    tens = (number // 10) % 10
    hundred = number // 100
    if digit != tens != hundred:
        chislo_1 = digit * 100 + tens * 10 + hundred
        chislo_3 = tens * 100 + hundred * 10 + digit
        chislo_3 = 2
        chislo_4 = 3
        chislo_5 = 4
        chislo_6 = 5

import random as r
while True:
    number = r.randint(100,999)
    digits = set(str(number))
    if len(digits) == 3:
        break
    print(f"Число {number} не подошло")

str_n = str(number)
list1 = [
    str_n[0] + str_n[1] + str_n[2],
    str_n[1] + str_n[2] + str_n[0]
]
list1 = list(map(int,list1))
print(list1)


from itertools import permutations
while True:
    number = r.randint(100,999)
    digits = set(str(number))
    if len(digits) == 3:
        break
    print(f"Число {number} не подошло")

perms = list(permutations(str(number)))

result = list(int(''.join(p)) for p in perms)
print(result)