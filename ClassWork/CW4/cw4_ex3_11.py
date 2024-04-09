# 3.11 Вычислить значение логического выражения:

# a)
x = 1
y = -1

res_1 = x ** 2 - y ** 2 <= 0
print("а)", res_1)

# б)
x = 2
y = -2
res_2 = (x >= 2) or (y ** 2 != 4)
print("б)", res_2)

# в)
x = 2
y = 2

res_3 = (x >= 0) and (y ** 2 > 4)
print("в)", res_3)

# г)
x = 1
y = 2

res_4 = (x * y != 4) and (y > x)
print("г)", res_4)

# д)
x = 2
y = 1
res_5 = (x * y != 0) or (y < x)
print("д)", res_5)

# e)
x = 1
y = 2

res_6 = (not (x * y < 1)) and (y > x)
print("е)", res_6)

# ж)
x = 2
y = 1

res_7 = (not (x * y < 0)) or (y > x)
print("ж)", res_7)
