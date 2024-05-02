import math as m
import random as r

# 5.2. Получить линейную запись следующих выражений (все формулы
# должна вычисляться):

# а)
x = r.uniform(1, 100)
result_a = -1 / x ** 2
print("а)", result_a)

# б)
a = r.uniform(-100, 100)
b = r.uniform(1, 100)
c = r.uniform(1, 100)
result_b = a / b * c
print("б)", result_b)

# в)
a = r.uniform(-100, 100)
b = r.uniform(1, 100)
c = r.uniform(-100, 100)
result_v = (a / b) * c
print("в)", result_v)

# г)
a = r.uniform(-100, 100)
b = r.uniform(-100, 100)
result_g = (a + b) / 2
print("г)", result_g)

# д)
a = r.uniform(1, 100)
b = r.uniform(-100, 100)
result_d = 5.45 * ((a + 2 * b) / 2 - a)
print("д)", result_d)

# е)
a = r.uniform(1, 100)
b = r.uniform(-100, 100)
c = r.uniform(-100, -1)
result_e = (-b + m.sqrt(b ** 2 - 4 * a * c) / 2 * a)
print("е)", result_e)

# ж)
a = r.uniform(1, 100)
b = r.uniform(-100, 100)
c = r.uniform(1, 100)
c *= r.choice([-1, 1])
result_j = (-b+1/a)/(2/c)
print("ж)", result_j)

# з)
a = r.uniform(-100, 100)
b = r.uniform(-100, 100)
result_z = 1/(1+(a+b)/2)
print("з)", result_z)

# и)
result_i = 1/(1+(1/(2+(1/(2+(3/5))))))
print("и)", result_i)
