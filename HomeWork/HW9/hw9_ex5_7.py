import math as m
import random as rnd

# 5.7. Составить программу вычисления значений функций при любых значениях a и b.:
a = rnd.uniform(1, 100)
a *= rnd.choice([-1, 1])
b = rnd.uniform(0, 100)

result_x = ((2 / (a ** 2 + 25)) + b) / (m.sqrt(b) + (a + b) / 2)
print(f"При a = {a} и b = {b} значение функции x =", result_x)

result_y = (abs(a) + 2 * m.sin(b)) / 5.5 * a
print(f"При a = {a} и b = {b} значение функции y =", result_y)

