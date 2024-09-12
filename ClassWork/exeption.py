# 1. Напишите функцию, которая принимает два числа и возвращает частное. Обработайте
# деление на ноль.

# 2. Напишите функцию, которая запрашивает у пользователя целое число и обрабатывает
# исключение при неправильном вводе.

# 3. Напишите функцию, которая преобразует строку в число с плавающей точкой и
# обрабатывает исключение.

# 4. Которая возвращает элемент из списка по индексу и обрабатывает исключение.

# 5. Которая возвращает значение по ключу в словаре и обрабатывает исключение при
# отсутствии ключа

# 6. Напишите функцию, которая принимает два параметра и пытается их объединить в
# в строку

def concatenate(number1: str, number2: int | float) -> str:
    """

    :param number1:
    :param number2:
    :return:
    """
    try:
        return number1 + str(number2)
    except TypeError as e:
        return f"Ошибка - {e}"


def get_value(dict1: dict[str, any], key_dict: str) -> any:
    """

    :param dict1:
    :param key_dict:
    :return:
    """
    try:
        return dict1[key_dict]
        # dict1.get(key_dict,None)
    except KeyError as e:
        return f"Ошибка в {e}"


def get_element(lst: list[int, float], idx: int) -> int | float:
    """

    :param lst:
    :param idx:
    :return:
    """
    try:
        return lst[idx]
    except IndexError as e:
        return f"Ошибка в {e}"


def str_to_float_z3(s: str) -> float:
    """

    :param s:
    :return:
    """
    try:
        return float(s)
    except ValueError as e:
        print("Ошибка ", e)


def get_integer_z2() -> int:
    """
    Запрашивает число у пользователя

    :return: целое число
    """
    try:
        return int(input("Введите целое число: "))
    except ValueError as e:
        # print("Ошибка ", e)
        return f"Ошибка значения {e}"


def divide_z1(num1: float, num2: float) -> float:
    """
    Функция предзначена для деления двух чисел

    :param num1: Первое число (числитель)
    :param num2: Второе число (знаменатель)
    :return: Частное от деления первого числа на второе
    """
    try:
        return num1 / num2
    except ZeroDivisionError as e:
        # print("Ошибка: ", e)
        # raise ValueError("Деление на ноль невозможно")
        return f"Деление на ноль невозможно - {e}"


def main():
    # 1
    print(divide_z1(10, 0))

    # 2
    print(get_integer_z2())

    # 3
    print(str_to_float_z3("20.4"))

    # 4
    list1 = [1, 2, 3, 4]
    index = int(input("Введите индекс: "))
    result = get_element(list1, index)
    print(result)

    # 5
    dict1 = {"a": 1, "b": 2}
    print(get_value(dict1, "c"))

    # 6
    print(concatenate(5, 5))

if __name__ == '__main__':
    main()