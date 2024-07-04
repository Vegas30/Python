"""

Главный скрипт для модуля.
"""

from data.input_data import get_initial_temperatures
from math_module import add_elements_in_array


def main():
    """

    Основная функция для демонстрации использования функции анализа температур.
    :return:
    """
    temperatures = get_initial_temperatures()
    while True:
        print("\nМеню: ")
        print("1. Добавить элемент в список")
        print("0. Выйти из программы")

        choice = input("Введите желаемый пункт меню ")

        if choice == "1":
            add_elements_in_array.add_elem(temperatures, 5)
            print("Измененый список: ", temperatures)
        elif choice == "0":
            break
        else:
            print("Такой комманды нет.")


if __name__ == "__main__":
    main()
