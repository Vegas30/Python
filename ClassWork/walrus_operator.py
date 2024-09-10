import string
# 1. Есть список чисел, необходимо отфильтровать те числа которые больше 5 и подсчитать их кол-во

numbers = [1, 2, 3, 6, 7, 4, 8, 2, 10]
count = sum(1 for num in numbers if (filt := num) > 5)

# 2. Даны два число найти максимальный из них
num1 = 56
num2 = 78
result = max(num1, num2)
if res := num1 > num2:
    print(num1)
else:
    print(num2)

# 3. Напишите программу которая проверяет содержит ли введеная строка специальные символы
punc = string.punctuation
for char in (line:= input("Введите строку: ")):
    if char in punc:
        print("Содержит")
    else:
        print("не содержит")

# st = str(input("Введите строку: "))
# if res := any(char in string.punctuation for char in st):
#     print("Ok")

