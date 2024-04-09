# Вычислить значение логического выражения при следующих
# значениях логических величин X, Y и Z: X = Ложь, Y = Истина, Z =
# Ложь:
# а) X или Z;
# б) X и Y;
# в) X и Z.

x = False
y = True
z = False

x_or_z = x or z  # False
x_and_y = x and y  # False
x_and_z = x and z  # False

print(x_or_z, x_and_y, x_and_z)
