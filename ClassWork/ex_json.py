# Дан Json файл с информацией о пользователях. Необходимо обновить возраст одного из
# полльзователь

import json

students = [
    {"name": "Иван Иван", "age": 30, "group": "MP-21"},
    {"name": "Иван Иванов", "age": 56, "group": "MP-51"},
    {"name": "Иван Ивнов", "age": 25, "group": "MP-11"},
    {"name": "Ин Иванов", "age": 98, "group": "MP-41"},
]

# with open('student_rename.json', 'w', encoding='utf-8') as file:
#     json.dump(students, file, ensure_ascii=False, indent=4)
#
# name_client = input("Введите имя пользователя: ")
#
# with open('student_rename.json', 'r', encoding='utf-8') as file:
#     users = json.load(file)
#
# flag = True
# for user in users:
#     if user['name'] == name_client:
#         flag = False
#         user['age'] = 35
# else:
#     if flag:
#         print("Клиент не найден")
#
# with open('student_rename.json', 'w', encoding='utf-8') as file:
#     json.dump(users, file, ensure_ascii=False, indent=4)

# --------------------------------------------------------------------

# with open('student_rename.json', 'r+', encoding='utf-8') as file:
#     users = json.load(file)
#
#     flag = True
#     for user in users:
#         if user['name'] == name_client:
#             flag = False
#             user['age'] = 35
#     else:
#         if flag:
#             print("Клиент не найден")
#
#     file.seek(0)
#
#     json.dump(users, file, ensure_ascii=False, indent=4)
#
#     file.truncate()

# -------------------------------------------------------------------

# 3. Программа должна записать и считать данные из CSV файла и сохранить их виде списка кортежей.
# import csv
#
# students = [
#     ('Иванов Иван', 20, 85),
#     ('Смирнов Александр', 30, 50),
#     ('Козлова Мария', 22, 95),
#     ('Иван Иван', 37, 100)
# ]
#
# with open('studik.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#
#     writer.writerow(['name', 'age', 'grade'])
#     writer.writerows(students)
#
# data_set = []
# with open('studik.csv', 'r', encoding='utf-8', newline='') as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
#         data_set.append(tuple(row))
#
# print(data_set)

# 4. Напишите программу, которая сереализует список чисел в бинарный формат с
# использованием msgpack, сохраняет в файл, а затем обратно десереализует в список

import msgpack
numbers = [10, 20, 30, 40, 50,]

with open('numbers.bin', 'wb') as file:
    packed_data = msgpack.dumps(numbers)
    file.write(packed_data)

with open('numbers.bin', 'rb') as file:
    packed_data = file.read()
    unpacked_data = msgpack.unpackb(packed_data)

print(unpacked_data)
