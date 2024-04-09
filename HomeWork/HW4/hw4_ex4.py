# 4. Вычислить значение логического выражения при следующих
# значениях логических величин X, Y и Z: X = Ложь, Y = Ложь, Z = Истина:
# 1) X или Y и не Z;
# 2) X и не Y или Z;
# 3) не X и не Y;
# 4) X и (не Y или Z);
# 5) не (X и Z) или Y;
# 6) X или (не (Y или Z)).

x = False
y = False
z = True

res_1 = x or y and not z    # False
res_2 = x and not y or z    # True
res_3 = not x and not y     # True
res_4 = x and (not y or z)  # False
res_5 = not (x and z) or y  # True
res_6 = x or (not (y or z)) # False

print(res_1, res_2, res_3, res_4, res_5, res_6, sep="\n")
