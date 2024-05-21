import math
import random as rnd

# 5.3. Записать по правилам изучаемого языка программирования
# следующие выражения (все формулы должны вычисляться):

# а)
x1 = rnd.uniform(1, 100)
x1 *= rnd.choice([-1, 1])
x2 = rnd.uniform(1, 100)
x2 *= rnd.choice([-1, 1])
result_a = math.sqrt(x1 ** 2 + x2 ** 2)
print("а)", result_a)

# б)
x1 = rnd.uniform(-100, 100)
x2 = rnd.uniform(-100, 100)
x3 = rnd.uniform(-100, 100)
result_b = x1 * x2 + x1 * x3 + x2 * x3
print("б)", result_b)

# в)
a = rnd.uniform(-100, 100)
t = rnd.uniform(-100, 100)
v0 = rnd.uniform(-100, 100)
result_v = v0 * t + (a * t ** 2) / 2
print("в)", result_v)

# г)
m = rnd.uniform(-100, 100)
g = rnd.uniform(-100, 100)
v = rnd.uniform(-100, 100)
h = rnd.uniform(-100, 100)
result_g = (m * (v ** 2)) / 2 + m * g * h
print("г)", result_g)

# д)
R1 = rnd.uniform(-100, 100)
R2 = rnd.uniform(-100, 100)
result_d = 1 / R1 + 1 / R2
print("д)", result_d)

# е)
m = rnd.uniform(-100, 100)
g = rnd.uniform(-100, 100)
a = rnd.uniform(-100, 100)
result_e = m * g * math.cos(a)
print("е)", result_e)

# ж)
R = rnd.uniform(-100, 100)
result_j = 2 * math.pi * R
print("ж)", result_j)

# з)
b = rnd.uniform(-100, 100)
a = rnd.uniform(-100, 100)
c = rnd.uniform(-100, 100)
result_z = b ** 2 - 4 * a * c
print("з)", result_z)

# и)
y = rnd.uniform(-100, 100)
m1 = rnd.uniform(-100, 100)
m2 = rnd.uniform(-100, 100)
r = rnd.uniform(1, 100)
r *= rnd.choice([-1, 1])
result_i = y * ((m1 * m2) / r ** 2)
print("и)", result_i)

# к)
I = rnd.uniform(-100, 100)
R = rnd.uniform(-100, 100)
result_k = (I ** 2) * R
print("к)", result_k)

# л)
a = rnd.uniform(-100, 100)
b = rnd.uniform(-100, 100)
c = rnd.uniform(-100, 100)
result_l = a * b * math.sin(c)
print("л)", result_l)

# м)
a = rnd.uniform(-100, 100)
b = rnd.uniform(-100, 100)
c = rnd.uniform(-100, 100)
result_m = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(c))
print("м)", result_m)

# н)
a = rnd.uniform(-100, 100)
b = rnd.uniform(-100, 100)
c = rnd.uniform(-100, 100)
d = rnd.uniform(-100, 100)
result_n = (a * d + b * c) / (a * d)
print("н)", result_n)

# о)
x = rnd.uniform(-100, 100)
result_o = math.sqrt(1 - math.sin(x) ** 2)
print("о)", result_o)

# п)
a = rnd.uniform(1, 100)
b = rnd.uniform(1, 100)
c = rnd.uniform(-100, 100)
x = rnd.uniform(1, 100)
result_p = 1 / math.sqrt(a * x ** 2 + b * x + c)
print("п)", result_p)

# р)
x = rnd.uniform(1, 100)
result_r = (math.sqrt(x + 1) + math.sqrt(x - 1)) / (2 * math.sqrt(x))
print("р)", result_r)

# с)
x = rnd.uniform(-100, 100)
result_s = abs(x) + abs(x + 1)
print("с)", result_s)

# т)
x = rnd.uniform(-100, 100)
result_t = abs(1-abs(x))
print("т)", result_t)
