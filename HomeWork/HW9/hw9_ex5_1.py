import math as m
import random as r

# 5.1. Записать по правилам изучаемого языка программирования
# следующие выражения (все формулы должны вычисляться):
# а)
x = r.uniform(-100, 100)
result_a = 2 * x
print("а)", result_a)

# б)
x = r.random()
result = m.sin(x)
print("б) sin(x)=", result)

# в)
a = r.uniform(-100, 100)
result_v = round(a ** 2, 2)
print("в)", result_v)

# г)
x = r.uniform(1, 100)
result_g = round(m.sqrt(x), 2)
print("г)", result_g)

# д)
n = r.uniform(1, 100)
result_d = round(abs(n), 2)
print("д)", result_d)

# е)
y = r.uniform(-100, 100)
result_e = round(5 * m.cos(y), 2)
print("е)", result_e)

# ж)
a = r.uniform(-100, 100)
result_j = -7.5 * (a ** 2)
print("ж)", round(result_j, 2))

# з)
x = r.uniform(1, 100)
result_z = round(3 * m.sqrt(x), 2)
print("з)", result_z)

# и)
a = r.random()
b = r.random()
result_i = round(m.sin(a) * m.cos(b) + m.cos(a) * m.sin(b), 2)
print("и)", result_i)

# к)
a = r.uniform(-100, 100)
b = r.uniform(1, 100)
result_k = round(a * m.sqrt(2 * b), 2)
print("к)", result_k)

# л)
a = r.uniform(-100, 100)
b = r.uniform(-100, 100)
result_l = round(3 * m.sin(2 * a) * m.cos(3 * b), 2)
print("л)", result_l)

# м)
x = r.uniform(0, 100)
y = r.uniform(0, 100)
result_m = round(-5 * m.sqrt(x + m.sqrt(y)))
print("м)", result_m)

