# Вычислить значение логического выражения при следующих
# значениях логических величин X, Y и Z: X = Ложь, Y = Истина, Z = Ложь:
# а) X и не (Z или Y) или не Z;
# б) не X или X и (Y или Z);
# в) (X или Y и не Z) и Z.

x = False
y = True
z = False

res_1 = (x and (not (z and y))) or (not z)  # True
res_2 = not x or x and (y or z)             # True
res_3 = (x or y and (not z)) and z          # False

print(res_1, res_2, res_3, sep="\n")
