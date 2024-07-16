def print_hi(name):
    """
    Приветствует пользователя по имени.
    Args:
        name (str): Имя пользователя.
    Returns:
        None
    """
    print(f'Hi, {name}')


def add(a, b):
    """
    Сложение двух чисел.
    Args:
        a (int, float): Первое число.
        b (int, float): Второе число.
    Returns:
        int, float: Сумма двух чисел.
    """
    return a + b


if __name__ == '__main__':
    print_hi('PyCharm')
    print(add(5, 3))
