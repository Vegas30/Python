import math as m
import random as rnd
# 5.4. Составить программу вычисления значения функции 𝑦
a = rnd.uniform(-100, 100)
result = (a**2 + 10)/ m.sqrt(a**2 + 1)
print(f"При a = {a}, значение функции y =", result)
