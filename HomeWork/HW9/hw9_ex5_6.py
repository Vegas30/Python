import math as m
import random as rnd

# 5.6. Составить программу вычисления значений функций при любых значениях х и y.:
x = rnd.uniform(1, 100)
x *= rnd.choice([-1,1])
y = rnd.uniform(1, 100)
y *= rnd.choice([-1,1])

result_z = (x + (2 + y)/x**2)/(y + (1/m.sqrt(x**2 + 10)))
print(f"При x = {x} и y = {y} значение функции z =", result_z)

result_q = 2.8*m.sin(x) + abs(y)
print(f"При x = {x} и y = {y} значение функции q =", result_q)

