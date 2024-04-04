# 3.4. Вычислить значение логического выражения при следующих
# значениях логических величин X, Y и Z: X = Истина, Y = Истина, Z =
# Ложь:
# а) не X и Y;
# б) X или не Y;
# в) X или Y и Z.

x = True
y = False
z = False

result_1 = not x and y # False
result_2 = x or (not y) # True
result_3 = x or (y and z) # True

print(result_1, result_2, result_3)