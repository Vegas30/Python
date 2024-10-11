from copy import deepcopy


# 1. Напишите функцию, которая принимает список чисел и
# возвращает словарь, где ключи — это числа, а значения — их
# кубы.
# nums = [1, 2, 3, 4, 5]
# Ожидаемый результат: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

def lst_to_key_is_num_value_is_cube(lst):
    res_dict = {i: lst[i] ** 3 for i in range(len(lst))}
    return res_dict


# 2. Напишите функцию, которая принимает строку и возвращает
# словарь, где ключи — это символы, а значения — количество их
# вхождений в строку.
# s = "hello world"
# # Ожидаемый результат: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

def str_to_key_is_char_value_is_amount(str):
    char_count_dict = {}
    # for char in str:
    #     if char in char_count_dict:
    #         char_count_dict[char] += 1
    #     else:
    #         char_count_dict[char] = 1
    for char in str:
        char_count_dict[char] = char_count_dict.get(char, 0) + 1

    return char_count_dict


# 3. Напишите функцию, которая принимает список слов и
# возвращает словарь, где ключи — это первые буквы слов, а
# значения — списки слов, начинающихся с этой буквы.
# words = ["apple", "banana", "cherry", "apricot", "blueberry"]
# Ожидаемый результат: {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
def group_words_by_first_letter(words_lst):
    letter_dict = {}
    for word in words_lst:
        first_letter = word[0]
        # if first_letter in letter_dict:
        #     letter_dict[first_letter].append(word)
        # else:
        #     letter_dict[first_letter] = [word]

        letter_dict[first_letter] = letter_dict.get(first_letter, []) + [word]

    return letter_dict


# 4. Напишите функцию, которая принимает список строк и
# возвращает словарь, где ключи — это строки, а значения — их
# длины.
# strings = ["apple", "banana", "cherry"]
# # Ожидаемый результат: {'apple': 5, 'banana': 6, 'cherry': 6}
def get_string_lengths(strings_lst):
    # result_dict = {}
    # for string in strings_lst:
    #     result_dict[string] = len(string)

    result_dict = {string: len(string) for string in strings_lst}
    return result_dict


# 5. Напишите функцию, которая принимает список чисел и
# возвращает словарь, где ключи — это числа, а значения — True,
# если число четное, и False, если нечетное.
# nums = [1, 2, 3, 4, 5]
# Ожидаемый результат: {1: False, 2: True, 3: False, 4: True, 5: False}
def check_even_odd(numbers_lst):
    res_dict = {}
    for num in numbers_lst:
        res_dict[num] = num % 2 == 0
    return res_dict


# 6. Напишите функцию, которая принимает словарь и возвращает
# новый словарь, где ключи и значения поменяны местами.
# example_dict = {'a': 1, 'b': 2, 'c': 3}
# # Ожидаемый результат: {1: 'a', 2: 'b', 3: 'c'}
def reverse_key_value(lst):
    # merge = {}
    # for key, value in lst.items():
    #     merge[value] = key

    merge = {value: key for key, value in lst.items()}
    return merge


# 7. Напишите функцию, которая принимает словарь и удаляет из
# него все ключи, значения которых пусты (None, пустая строка,
# пустой список и т.д.).
# example_dict = {'a': 1, 'b': '', 'c': None, 'd': [], 'e': 2}
# Ожидаемый результат: {'a': 1, 'e': 2}
def dict_del_empty(dict):
    new_dict = {}
    for key, value in dict.items():
        if value:
            new_dict[key] = value
    return new_dict


# 8. Напишите функцию, которая принимает два словаря и
# объединяет их, добавляя только уникальные ключи из второго
# словаря в первый.
# dict1 = {'a': 1, 'b': 2} dict2 = {'b': 3, 'c': 4}
# Ожидаемый результат: {'a': 1, 'b': 2, 'c': 4}
def union_uniq(dict1, dict2):
    merge = dict1.copy()
    for key, value in dict2.items():
        if key in merge:
            continue
        else:
            merge[key] = value
    return merge


# 9. Напишите функцию, которая принимает два словаря и
# возвращает новый словарь, где для каждого ключа значения из
# обоих словарей суммируются.
# dict1 = {'a': 1, 'b': 2} dict2 = {'b': 3, 'c': 4}
# # Ожидаемый результат: {'a': 1, 'b': 5, 'c': 4}
def merge_dict(dict1, dict2):
    merge = dict1.copy()
    for key, value in dict2.items():
        if key in merge:
            merge[key] += value
        else:
            merge[key] = value
    return merge


# 10. Напишите функцию, которая принимает два списка
# одинаковой длины и создает словарь, где элементы первого
# списка — это ключи, а элементы второго списка — значения.
# keys = ["a", "b", "c"] values = [1, 2, 3]
# # Ожидаемый результат: {'a': 1, 'b': 2, 'c': 3}
def make_dict_from_two_list(keys_lst, values_lst):
    result_dict = dict(zip(keys_lst, values_lst))
    return result_dict


# 11. Напишите функцию, которая принимает два словаря и
# возвращает новый словарь, содержащий только общие ключи с
# минимальными значениями для каждого ключа.
# example_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}
# # Ожидаемый результат: {'a': 1, 'b': 2, 'e': 3}
def merge_dict_by_min(dict1, dict2):
    copy_dict1 = dict1.copy()
    for key, value in dict2.items():
        if key in copy_dict1:
            copy_dict1[key] = min(copy_dict1[key], value)
        else:
            copy_dict1[key] = value
    return copy_dict1


# 12. * Напишите функцию, которая принимает список словарей и
# возвращает один объединенный словарь. Если ключи
# совпадают, значения суммируются.
# dicts = [{'a': 1, 'b': 2}, {'a': 2, 'b': 3, 'c': 4}, {'b': 1, 'c': 2}]
# # Ожидаемый результат: {'a': 3, 'b': 6, 'c': 6}
def merge_dict_list(dict_lst):
    merge = {}
    for dictionary in dict_lst:
        for key, value in dictionary.items():
            # if key in merge:
            #     merge[key] += value
            # else:
            #     merge[key] = value
            merge[key] = merge.get(key, 0) + value
    return merge


# ---------------------------------------------------------------------------------------
# 1. Напишите функцию, которая принимает словарь и возвращает
# новый словарь, где ключи — это значения исходного словаря, а
# значения — списки ключей исходного словаря.
# example_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}
# Ожидаемый результат: {1: ['a', 'c'], 2: ['b', 'd'], 3: ['e']}
def transform_dict(input_dict):
    output_dict = {}
    for key, value in input_dict.items():
        if value in output_dict:
            output_dict[value].append(key)
        else:
            output_dict[value] = [key]
    return output_dict


# 2. Напишите функцию, которая принимает словарь и возвращает
# новый словарь, где только уникальные значения.
# example_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
# # Ожидаемый результат: {'a': 1, 'b': 2, 'd': 3}
def uniq_dict(input_dict):
    output_dict = {}
    for key, value in input_dict.items():
        if value not in output_dict.values():
            output_dict[key] = value
    return output_dict


# 3. Напишите функцию, которая принимает список словарей и
# возвращает один словарь, в котором для каждого ключа
# выбирается максимальное значение из всех словарей.
# dicts = [{'a': 1, 'b': 2}, {'a': 3, 'b': 1, 'c': 4}, {'b': 3, 'c': 2}]
def dict_max_value(dict_lst):
    merge = {}
    for dictionary in dict_lst:
        for key, value in dictionary.items():
            if key in merge:
                merge[key] = max(merge[key], value)
            else:
                merge[key] = value
    return merge


# 4. Напишите функцию, которая принимает список словарей и
# возвращает один словарь, в котором значения каждого ключа
# объединены в списки.
# dicts = [{'a': 1, 'b': 2}, {'a': 3, 'b': 1, 'c': 4}, {'b': 3, 'c': 2}]
# # Ожидаемый результат: {'a': [1, 3], 'b': [2, 1, 3], 'c': [4, 2]}
def dict_list_to_value_list(dict_lst):
    merge = {}
    for dictionary in dict_lst:
        for key, value in dictionary.items():
            if key in merge:
                merge[key].append(value)
            else:
                merge[key] = [value]
    return merge


# 5. Напишите функцию, которая принимает словарь и возвращает новый
# словарь, где значения заменены на их обратные значения.
# example_dict = {'a': 1, 'b': 2, 'c': 0.5}
# Ожидаемый результат: {'a': 1.0, 'b': 0.5, 'c': 2.0}
def reverse_value_dict(input_dict):
    # new_dict ={}
    # for key, value in input_dict.items():
    #     if key not in new_dict:
    #         new_dict[key] = 1/value
    new_dict = {key: 1 / value for key, value in input_dict.items()}
    return new_dict


# 6. * Напишите функцию, которая принимает список словарей и
# возвращает один словарь, где значения объединены в списки по
# общим ключам.
# dicts = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4, 'c': 5}, {'a': 6, 'c': 7}]
# # Ожидаемый результат: {'a': [1, 3, 6], 'b': [2, 4], 'c': [5, 7]}

def merge_dicts(list_dicts):
    merged_dict = {}
    for dictionary in list_dicts:
        for key, value in dictionary.items():
            if key in merged_dict:
                merged_dict[key].append(value)
            else:
                merged_dict[key] = value
    return merged_dict


# 7. !! Напишите функцию, которая принимает список словарей с
# информацией о студентах и их оценках по предметам, и
# возвращает словарь, где ключи — названия предметов, а
# значения — средние оценки по этим предметам.
# students = [ {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
# {'name': 'Bob', 'grades': {'math': 80, 'science': 90}}, {'name':
# 'Charlie', 'grades': {'math': 85, 'science': 80}} ]
# Ожидаемый результат: {'math': 85.0, 'science': 85.0}
def calculate_average_grades(list_dicts):
    subject_grades = {}
    subject_counts = {}
    for student in list_dicts:
        for subject, grade in student['grades'].items():
            if subject in subject_grades:
                subject_grades[subject] += grade
                subject_counts[subject] += 1
            else:
                subject_grades[subject] = grade
                subject_counts[subject] = 1
    average_grades = {subject: total_grades / subject_counts[subject] for subject, total_grades in
                      subject_grades.items()}
    return average_grades


# 8. Напишите функцию, которая принимает список словарей с информацией о студентах и их оценках по предметам,
# и возвращает словарь, где ключи — названия предметов, а значения — имена студентов
# с наивысшими оценками по этим предметам.
# students = [ {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
# {'name': 'Bob', 'grades': {'math': 80, 'science': 90}}, {'name':
# 'Charlie', 'grades': {'math': 85, 'science': 80}} ]
# Ожидаемый результат: {'math': 'Alice', 'science': 'Bob'}
def get_top_students(list_dict):
    top_students = {}
    for student in list_dict:
        for subject, grade in student['grades'].items():
            if subject in top_students:
                if grade > student['grades'][subject]:
                    top_students[subject] = student['name']
            else:
                top_students[subject] = student['name']
    return top_students


# 9. Напишите функцию, которая принимает список словарей с информацией о студентах и их оценками по предметам, и
# возвращает список имён студентов, у которых хотя бы по одному предмету оценка выше заданного порога.
# students = [ {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
# {'name': 'Bob', 'grades': {'math': 80, 'science': 90}}, {'name':
# 'Charlie', 'grades': {'math': 85, 'science': 80}} ]
# threshold = 85
# # Ожидаемый результат: ['Alice', 'Bob']
def get_students_above_threshold(list_dict: list[dict: str, any], threshold) -> list:
    above_threshold_students = []
    for student in list_dict:
        for grade in student['grades'].values():
            if grade > threshold:
                above_threshold_students.append(student['name'])
                break
    return above_threshold_students


# 10. Напишите функцию, которая принимает список словарей с
# информацией о студентах и их оценками по предметам, и
# возвращает словарь, где ключи — имена студентов, а значения
# — их средние оценки.
# students = [ {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
# {'name': 'Bob', 'grades': {'math': 80, 'science': 90}}, {'name':
# 'Charlie', 'grades': {'math': 85, 'science': 80}} ]
# # Ожидаемый результат: {'Alice': 87.5, 'Bob': 85.0, 'Charlie': 82.5}
# (РЕШИТЬ ЧЕРЕЗ ВКЛЮЧЕНИЯ)
def student_average_grades(list_dict: list[dict[str, any]]) -> dict[str, float]:
    # student_average_grades_dict = {}
    # for student in list_dict:
    #     total_grades = sum(student['grades'].values())
    #     average_grade = total_grades / len(student['grades'])
    #     student_average_grades_dict[student['name']] = average_grade
    student_average_grades_dict = {
        student['name']: sum(student['grades'].values()) / len(student['grades']) for student in
        list_dict}
    return student_average_grades_dict


# 11. Напишите функцию, которая принимает список словарей с информацией о студентах и их оценками по предметам, и
# возвращает словарь, где ключи — названия предметов, а значения — списки студентов, получивших заданную оценку по
# этому предмету.
# students = [ {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
# {'name': 'Bob', 'grades': {'math': 80, 'science': 90}}, {'name':
# 'Charlie', 'grades': {'math': 85, 'science': 80}} ] specific_grade = 85
# # Ожидаемый результат: {'science': ['Alice'], 'math': ['Charlie']}
def get_students_with_specific_grade(students: list[dict[str, any]], specific_grade: int) -> dict[str, list[str]]:
    students_with_specific_grade = {}
    for student in students:
        for subject, grade in student['grades'].items():
            if grade == specific_grade:
                if subject in students_with_specific_grade:
                    students_with_specific_grade[subject].append(student['name'])
                else:
                    students_with_specific_grade[subject] = student['name']
    return students_with_specific_grade


# 12. Напишите функцию, которая принимает список словарей с информацией о студентах
# и их оценками по предметам, и возвращает словарь, где ключи — названия предметов,
# а значения — словари с минимальной, максимальной и средней
# оценкой по каждому предмету.
# students = [ {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
# {'name': 'Bob', 'grades': {'math': 80, 'science': 90}}, {'name':
# 'Charlie', 'grades': {'math': 85, 'science': 80}} ]
# # Ожидаемый результат: {'math': {'min': 80, 'max': 90, 'average':
# 85.0}, 'science': {'min': 80, 'max': 90, 'average': 85.0}}
def calculate_grades_summary(students: list[dict[str, any]]) -> dict[str, dict[str, float]]:
    subjects = set()
    grades_summary = {}
    for student in students:
        for subject, grade in student['grades'].items():
            subjects.add(subject)
            if subject not in grades_summary:
                grades_summary[subject] = {'min': grade, 'max': grade, 'sum': grade, 'count': 1}
            else:
                grades_summary[subject]['min'] = min(grades_summary[subject]['min'], grade)
                grades_summary[subject]['max'] = max(grades_summary[subject]['max'], grade)
                grades_summary[subject]['sum'] = grades_summary[subject]['sum'] + grade
                grades_summary[subject]['count'] = grades_summary[subject]['count'] + 1

    for subject in subjects:
        grades_summary[subject]['average'] = grades_summary[subject]['sum'] / grades_summary[subject]['count']
        grades_summary[subject].pop('sum')
        grades_summary[subject].pop('count')

    return grades_summary


# 13. Напишите функцию, которая принимает список словарей с
# информацией о студентах и их оценками по предметам, и
# возвращает список имён студентов, которые получили
# одинаковые оценки по всем предметам.
# students = [ {'name': 'Alice', 'grades': {'math': 90, 'science': 90}},
# {'name': 'Bob', 'grades': {'math': 80, 'science': 80}}, {'name':
# 'Charlie', 'grades': {'math': 85, 'science': 80}} ]
# # Ожидаемый результат: ['Alice', 'Bob']
def find_students_with_same_grades(students: list[dict[str, any]]) -> list[str]:
    same_grades_students = []
    for student in students:
        if student['grades']['math'] == student['grades']['science']:
            same_grades_students.append(student['name'])
    return same_grades_students


# 14. Напишите функцию, которая принимает список словарей с
# информацией о студентах и их оценками по предметам, и
# возвращает имя студента с наименьшей суммой оценок.
# students = [
# {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
# {'name': 'Bob', 'grades': {'math': 80, 'science': 70}},
# {'name': 'Charlie', 'grades': {'math': 85, 'science': 80}} ]
# # Ожидаемый результат: 'Bob'
def student_with_min_total_grade(students):
    min_total_grade = float('inf')
    student_with_min_grade = ''
    for student in students:
        total_grade = sum(student['grades'].values())
        if total_grade < min_total_grade:
            min_total_grade = total_grade
            student_with_min_grade = student['name']

    return student_with_min_grade


# 15. Напишите функцию, которая принимает список словарей с
# информацией о студентах и их оценками по предметам, и
# возвращает список имён студентов, у которых все оценки выше
# среднего значения по всем предметам.
# students = [ {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
# {'name': 'Bob', 'grades': {'math': 80, 'science': 70}}, {'name':
# 'Charlie', 'grades': {'math': 85, 'science': 80}} ]
# # Ожидаемый результат: ['Alice']
def students_above_average(students):
    all_grades = []
    for student in students:
        all_grades.extend(student['grades'].values())

    average_grade = sum(all_grades) / len(all_grades)

    student_list = []
    for student in students:
        if all(grade > average_grade for grade in student['grades'].values()):
            student_list.append(student['name'])
    return student_list


# 16. Напишите функцию, которая принимает список словарей с
# информацией о студентах и их оценками по предметам, и
# возвращает сводную таблицу в виде словаря, где ключи —
# названия предметов, а значения — словари, в которых ключи —
# имена студентов, а значения — их оценки.
# students = [ {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
# {'name': 'Bob', 'grades': {'math': 80, 'science': 70}}, {'name':
# 'Charlie', 'grades': {'math': 85, 'science': 80}} ]
# # Ожидаемый результат: {'math': {'Alice': 90, 'Bob': 80, 'Charlie':
# 85}, 'science': {'Alice': 85, 'Bob': 70, 'Charlie': 80}}
def create_summary_table(students):
    summary_table = {}
    for student in students:
        for subject, grade in student['grades'].items():
            if subject not in summary_table:
                summary_table[subject] = {}
            summary_table[subject][student['name']] = grade

    return summary_table


# 17. Напишите функцию, которая принимает список словарей с
# информацией о студентах и их оценками, и возвращает словарь,
# где ключи — предметы, а значения — общие суммы оценок по
# каждому предмету.
# students = [ {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
# {'name': 'Bob', 'grades': {'math': 80, 'science': 90}}, {'name':
# 'Charlie', 'grades': {'math': 85, 'science': 80}} ]
# # Ожидаемый результат: {'math': 255, 'science': 255}
def calculate_total_grades(students):
    total_grades = {}
    for student in students:
        for subject, grade in student['grades'].items():
            # if subject not in total_grades:
            #     total_grades[subject] = 0
            # total_grades[subject] += grade
            total_grades[subject] = total_grades.get(subject, 0) + grade
    return total_grades


# 18. Напишите функцию, которая принимает список словарей с
# информацией о студентах и их оценками, и возвращает словарь,
# где ключи — предметы, а значения — кортежи с минимальной и
# максимальной оценками по каждому предмету.
# students = [ {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
# {'name': 'Bob', 'grades': {'math': 80, 'science': 90}}, {'name':
# 'Charlie', 'grades': {'math': 85, 'science': 80}} ]
# # Ожидаемый результат: {'math': (80, 90), 'science': (80, 90)}
def calculate_min_max_grades(students):
    min_max_grades = {}
    for student in students:
        for subject, grade in student['grades'].items():
            if subject not in min_max_grades:
                min_max_grades[subject] = (grade, grade)
            else:
                current_min, current_max = min_max_grades[subject]
                min_max_grades[subject] = (min(current_min, grade)), (max(current_max, grade))

    return min_max_grades


def main():
    # 1.
    nums = [1, 2, 3, 4, 5]
    result = lst_to_key_is_num_value_is_cube(nums)
    print("1.", result)

    # 2.
    s = "hello world"
    result = str_to_key_is_char_value_is_amount(s)
    print("2.", result)

    # 3.
    words = ["apple", "banana", "cherry", "apricot", "blueberry"]
    result_dict = group_words_by_first_letter(words)
    print("3.", result_dict)

    # 4.
    strings = ["apple", "banana", "cherry"]
    result_dict = get_string_lengths(strings)
    print("4.", result_dict)

    # 5.
    nums = [1, 2, 3, 4, 5]
    result_dict = check_even_odd(nums)
    print("5.", result_dict)

    # 6.
    example_dict = {'a': 1, 'b': 2, 'c': 3}
    result_dict = reverse_key_value(example_dict)
    print("6.", result_dict)

    # 7.
    example_dict = {'a': 1, 'b': '', 'c': None, 'd': [], 'e': 2}
    result_dict = dict_del_empty(example_dict)
    print("7.", result_dict)

    # 8.
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    result_dict = union_uniq(dict1, dict2)
    print("8.", result_dict)

    # 9.
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    result_dict = merge_dict(dict1, dict2)
    print("9.", result_dict)

    # 10.
    keys = ["a", "b", "c"]
    values = [1, 2, 3]
    result_dict = make_dict_from_two_list(keys, values)
    print("10.", result_dict)

    # 11.
    example_dict1 = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}
    example_dict2 = {'a': 1, 'b': 5, 'e': 7}
    dict_result = merge_dict_by_min(example_dict1, example_dict2)
    print("11.", dict_result)

    # 12.
    dicts = [{'a': 1, 'b': 2}, {'a': 2, 'b': 3, 'c': 4}, {'b': 1, 'c': 2}]
    result_dict = merge_dict_list(dicts)
    print("12.", result_dict)
    # ---------------------------------------------------------------------------------

    # 1.
    example_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}
    result_dict = transform_dict(example_dict)
    print("1.", result_dict)

    # 2.
    example_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
    result_dict = uniq_dict(example_dict)
    print("2.", result_dict)

    # 3.
    dicts = [{'a': 1, 'b': 2}, {'a': 3, 'b': 1, 'c': 4}, {'b': 3, 'c': 2}]
    result_dict = dict_max_value(dicts)
    print("3.", result_dict)

    # 4.
    dicts = [{'a': 1, 'b': 2}, {'a': 3, 'b': 1, 'c': 4}, {'b': 3, 'c': 2}]
    result_dict = dict_list_to_value_list(dicts)
    print("4.", result_dict)

    # 5.
    example_dict = {'a': 1, 'b': 2, 'c': 0.5}
    result_dict = reverse_value_dict(example_dict)
    print("5.", result_dict)

    # 6.
    dicts = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4, 'c': 5}, {'a': 6, 'c': 7}]
    result_dict = dict_list_to_value_list(dicts)
    print("6.", result_dict)

    # 7.
    students = [
        {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
        {'name': 'Bob', 'grades': {'math': 80, 'science': 90}},
        {'name': 'Charlie', 'grades': {'math': 85, 'science': 80}}
    ]
    result_dict = calculate_average_grades(students)
    print("7.", result_dict)

    # 8.
    students = [
        {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
        {'name': 'Bob', 'grades': {'math': 80, 'science': 90}},
        {'name': 'Charlie', 'grades': {'math': 85, 'science': 80}}
    ]
    result_dict = get_top_students(students)
    print("8.", result_dict)

    # 9.
    students = [
        {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
        {'name': 'Bob', 'grades': {'math': 80, 'science': 90}},
        {'name': 'Charlie', 'grades': {'math': 85, 'science': 80}}
    ]
    threshold = 85
    result_dict = get_students_above_threshold(students, threshold)
    print("9.", result_dict)

    # 10.
    students = [
        {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
        {'name': 'Bob', 'grades': {'math': 80, 'science': 90}},
        {'name': 'Charlie', 'grades': {'math': 85, 'science': 80}}
    ]
    result_dict = student_average_grades(students)
    print("10.", result_dict)

    # 11.
    students = [
        {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
        {'name': 'Bob', 'grades': {'math': 80, 'science': 90}},
        {'name': 'Charlie', 'grades': {'math': 85, 'science': 80}}
    ]
    specific_grade = 85
    result_dict = get_students_with_specific_grade(students, specific_grade)
    print("11.", result_dict)

    # 12.
    students = [
        {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
        {'name': 'Bob', 'grades': {'math': 80, 'science': 90}},
        {'name': 'Charlie', 'grades': {'math': 85, 'science': 80}}
    ]
    result_dict = calculate_grades_summary(students)
    print("12.", result_dict)

    # 13.
    students = [
        {'name': 'Alice', 'grades': {'math': 90, 'science': 90}},
        {'name': 'Bob', 'grades': {'math': 80, 'science': 80}},
        {'name': 'Charlie', 'grades': {'math': 85, 'science': 80}}
    ]
    result_list = find_students_with_same_grades(students)
    print("13.", result_list)

    # 14.
    students = [
        {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
        {'name': 'Bob', 'grades': {'math': 80, 'science': 70}},
        {'name': 'Charlie', 'grades': {'math': 85, 'science': 80}}
    ]
    result = student_with_min_total_grade(students)
    print("14.", result)

    # 15.
    students = [
        {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
        {'name': 'Bob', 'grades': {'math': 80, 'science': 70}},
        {'name': 'Charlie', 'grades': {'math': 85, 'science': 80}}
    ]
    result = students_above_average(students)
    print("15.", result)

    # 16.
    students = [
        {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
        {'name': 'Bob', 'grades': {'math': 80, 'science': 70}},
        {'name': 'Charlie', 'grades': {'math': 85, 'science': 80}}
    ]
    result = create_summary_table(students)
    print("16.", result)

    # 17.
    students = [
        {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
        {'name': 'Bob', 'grades': {'math': 80, 'science': 90}},
        {'name': 'Charlie', 'grades': {'math': 85, 'science': 80}}
    ]
    result = calculate_total_grades(students)
    print("17.", result)

    # 18.
    students = [
        {'name': 'Alice', 'grades': {'math': 90, 'science': 85}},
        {'name': 'Bob', 'grades': {'math': 80, 'science': 90}},
        {'name': 'Charlie', 'grades': {'math': 85, 'science': 80}}
    ]

    # Вызов функции и вывод результата
    result = calculate_min_max_grades(students)
    print("18.", result)


if __name__ == '__main__':
    main()
