a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
if a > b:
    maximum = a
else:
    maximum = b
if c > maximum:
    maximum = c

print("Максимальное число: ", maximum)
