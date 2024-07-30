from math import factorial

# # 6. Напишите функцию, кторая принимает два списка одинаковой длины и создает из них словарь, где элементы первого списка - ключи, а второго значения
#
# keys = ['a', 'b', 'c']
# value = ['name', 24 , 'age']
#
# dict_result = dict(zip(keys, value))
# print(list(zip(keys, value)))
# print(dict_result)
#
# # 7. Напишите функцию которая принимает два словаря и объединяет их.
# # Если ключи совпадают, выберите наибольшее значение.
#
#
# def union_func(dict1, dict2):
#     copy_dict1 = dict1.copy()
#     for key, value in dict2.items():
#         if key in copy_dict1:
#             copy_dict1[key] = max(copy_dict1[key],value)
#         else:
#             copy_dict1[key] = value
#     return copy_dict1
#
# def main():
#     dict1 = {'a': 1, 'b': 5, 'name': 3}
#     dict2 = {'a': 5, 'b': 3, 'name': 3}
#     result_dict = union_func(dict1, dict2)
#     print(result_dict)
#
# main()

# 8. Напишите функцию,
# которая принимает словарь с именами студентов и их оценками.
# Функция должна возвращать студентов, у которых оценка выше среднего.
#
# students = {"Maxim": 60, 'Bob': 85, 'Alice': 78, 'Alina': 68}
# def best_student(students):
#     average = sum(students.value() / len(students))
#     result_list_students = {student for student, grade in students.items() if grade > }
#

# # Напишите функцию
#
# students = [
#     {'name': 'Alice', 'age': 24, 'grades': {'math': 90, 'physics': 85, 'chemistry': 67}},
#     {'name': 'Bob', 'age': 23, 'grades': {'math': 70, 'physics': 80, 'chemistry': 97}},
#     {'name': 'Charlie', 'age': 22, 'grades': {'math': 85, 'physics': 89, 'chemistry': 97}}
#
# ]
#
# result_dict = {}
#
# for student in students:
#     name = student['name']
#     grade = student['grades']
#     print(name, grade)
#     average = round(sum(grade.values()) / len(grade), 2)
#     result_dict[name] = average
# print(result_dict)

# # 10. Напишите функцию которая принимает список чисел и возвращает словарь, где ключи - числа, а значения их факториалы.
#
# nums = [1, 2, 3, 4, 5]
#
# result = {num: factorial(num) for num in nums}
# print(result)
# result = dict(zip(nums, map(lambda x: factorial(x), nums)))
# print(result)
#
# # Напишите функцию которая принимает список чисел и возвращает словарь,
# # где ключи - 'even' и 'odd', а значения - списки четных и нечетных чисел
#
# nums = [1, 2, 3, 4, 5, 6]
# # Итог: {even:[2,4,6], odd:[1,3,5]}
# dict1 = {'even': [], 'odd': []}
# for num in nums:
#     if num % 2 == 0:
#         dict1['even'].append(num)
#     else:
#         dict1['odd'].append(num)
#
# print(dict1)
#
# # 12.Напишите функцию, которая принимает словарь, где значения могут повторятся,
# # и возвращает новый словарь, где ключи - уникальные значения из исходного словаря,
# # а значения - списки ключей, соответствующие этим значениям.
#
# dict1 = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}
# # {1:['a', 'c'], 2:['b','d'], 3: ['e']}
#
# result_dict = {}
# for key, value in dict1.items():
#     if value in result_dict:
#         result_dict[value].append(key)
#     else:
#         result_dict[value] = [key]
#
# print(result_dict)
# # ------------------------------------------------------------------------
# result_dict = {}
# # 13. Напишите функцию, которая принимает список строк и группирует их по длине.
# # Верните словарь, где ключи - это длины строк, а значения - списки строк соответствующей длины.
#
# strings = ['a', 'bb', 'ccc', 'dd', 'eeee']
#
# result_dict = {}
# for i in strings:
#     length = len(i)
#     if length in result_dict:
#         result_dict[length].append(i)
#     else:
#         result_dict[length] = [i]
#
# print(result_dict)
#
# # 14. Напишите функцию которая принимает два словаря и возвращает только те пары ключ-значение, которые есть в обоих словарях
#
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# set1 = set(dict1)
# set2 = set(dict2)
# set_result = set1 & set2
# dict_result = {}
# for key, value in dict1.items():
#     if key in set_result:
#         dict_result[key] = value
#
# print(dict_result)

# # Напишите функцию которая принимает список словарей с информацией о студентах и их оценками,
# # и возвращает словарь, где ключи - предметы а значения кортежи с минимальной и максимальной оценками
# # по каждому предмету
# students = [
#     {'name': 'Alice', 'age': 24, 'grades': {'math': 90, 'physics': 85, 'chemistry': 67}},
#     {'name': 'Bob', 'age': 23, 'grades': {'math': 70, 'physics': 80, 'chemistry': 97}},
#     {'name': 'Charlie', 'age': 22, 'grades': {'math': 85, 'physics': 89, 'chemistry': 97}}
#
# ]
#
# min_max = {}
#
# for student in students:
#     for subject, grade in student['grades'].items():
#         if subject not in min_max:
#             min_max[subject] = (grade, grade)  # это если предметов еще нет в пустом словаре
#         else:
#             current_min, current_max = min_max[subject]
#             min_max[subject] = (min(grade, current_min), max(grade, current_max))
# print(min_max)
#
# # Напишите функцию которая принимает список словарей с информацией о студентах и их оценками,
# # и возвращает словарь, где ключи - предметы а значения - средние оценки по предметам,
# # округленные до ближайшего целого
#
# students = [
#     {'name': 'Alice', 'age': 24, 'grades': {'math': 90, 'physics': 85, 'chemistry': 67}},
#     {'name': 'Bob', 'age': 23, 'grades': {'math': 70, 'physics': 80, 'chemistry': 97}},
#     {'name': 'Charlie', 'age': 22, 'grades': {'math': 85, 'physics': 89, 'chemistry': 97}}
#
# ]
#
# subject_totals = {}
# subject_counts = {}
# for student in students:
#     for subject, grade in student['grades'].items():
#         if subject not in subject_totals and subject not in subject_counts:
#             subject_totals[subject] = grade
#             subject_counts[subject] = 1
#         else:
#             subject_totals[subject] = subject_totals[subject] + grade
#             subject_counts[subject] = subject_counts[subject] + 1
# result_dict = {subject: round(subject_totals[subject] / subject_counts[subject]) for subject in subject_totals}
# print(result_dict)
#
# for student in students:
#   for subject, grade in student['grades'].items():
#       subject_totals[subject] = subject_totals.get(subject,0) + grade
#       subject_counts[subject] = subject_counts.get(subject,0) + 1
# result_dict = {subject: round(subject_totals[subject]/subject_counts[subject]) for subject in subject_totals}
# print(result_dict)

# Напишите функцию, которая принимает список словарей возвращает список имен студентов,
# которые здали все предметы выше 50

students = [
    {'name': 'Alice', 'age': 24, 'grades': {'math': 90, 'physics': 85, 'chemistry': 67}},
    {'name': 'Bob', 'age': 23, 'grades': {'math': 70, 'physics': 80, 'chemistry': 97}},
    {'name': 'Charlie', 'age': 22, 'grades': {'math': 85, 'physics': 89, 'chemistry': 97}}

]
result = []
for student in students:
    if all(grade > 50 for grade in student['grades'].values()):
        result.append(student['name'])
print(result)

result = []
flag = True
for student in students:
    for grade in student['grades'].values():
        if grade < 50:
            flag = False
    if flag:
        result.append(student['name'])
    flag = True
print(result)

result = [student['name'] for student in students if all(grade > 50 for grade in student['grades'].values())]
print(result)

# Напишите функцию, которая принимает список словарей и возвращает словарь,
# где ключи это предметы, а значения - общие суммы оценок по каждому предмету
students = [
    {'name': 'Alice', 'age': 24, 'grades': {'math': 90, 'physics': 85, 'chemistry': 67}},
    {'name': 'Bob', 'age': 23, 'grades': {'math': 70, 'physics': 80, 'chemistry': 97}},
    {'name': 'Charlie', 'age': 22, 'grades': {'math': 85, 'physics': 89, 'chemistry': 97}}

]
subject_totals = {}
for student in students:
    for subject, grade in student['grades'].items():
        subject_totals[subject] = subject_totals.get(subject, 0) + grade
result_dict = {subject: subject_totals[subject] for subject in subject_totals}
print(result_dict)

# возвращает сводную таблицу в виде словаря где ключи названия предметов,
# а значения - словари, в которых ключи - имена студентов, а значения - их оценки.
students = [
    {'name': 'Alice', 'age': 24, 'grades': {'math': 90, 'physics': 85, 'chemistry': 67}},
    {'name': 'Bob', 'age': 23, 'grades': {'math': 70, 'physics': 80, 'chemistry': 97}},
    {'name': 'Charlie', 'age': 22, 'grades': {'math': 85, 'physics': 89, 'chemistry': 97}}
]

result_dict = {}
for student in students:
    for subject, grade in student['grades'].items():
        if subject not in result_dict:
            result_dict[subject] = {}
        result_dict[subject][student['name']] = grade
print(result_dict)