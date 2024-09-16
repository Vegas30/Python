# src/valid/validation.py

# Проверка на корректный ввод
def validate_input_number(input_str: str) -> int:
    """
    Функция проверяет корректность ввода данных пользователем

    :param input_str: Принимает числовое значение от пользователя типа str.
    :return: Возвращает значение числовое типа int.
    """
    while True:
        try:
            number = int(input(input_str))
            return number
        except ValueError:
            print("Некорректный ввод. Введите число.")
