# src/valid/validation.py

# Проверка на корректный ввод
def validate_input_number(input_str: str) -> int:
    while True:
        try:
            number = int(input(input_str))
            return number
        except ValueError:
            print("Некорректный ввод. Введите число.")
