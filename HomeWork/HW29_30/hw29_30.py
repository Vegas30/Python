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


if __name__ == '__main__':
    main()
