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

def main():
    # 1.
    nums = [1, 2, 3, 4, 5]
    result = lst_to_key_is_num_value_is_cube(nums)
    print("1.", result)

    # 2.
    s = "hello world"
    result = str_to_key_is_char_value_is_amount(s)
    print("2.", result)


if __name__ == '__main__':
    main()
