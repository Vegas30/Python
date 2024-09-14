# src/modific/modification.py
import random


# 4. Добавить в список температур еще один список температур за последние несколько дней месяца.
def add_few_days(month: list[int], n: int) -> list[int]:
    new_array = month + month[n:]
    return new_array


# 5. Удалить температуру последнего дня из списка.
def del_last_day(month: list[int]) -> list[int]:
    new_array = month[:]
    new_array.pop()
    return new_array


# 6. Объединить два списка температур, представляющих собой данные двух разных месяцев.

# Создаем второй месяц и заполняем его случайными температурами с заданным диапазоном
def make_second_month(n: int, m: int) -> list[int]:
    second_month = [random.randint(n, m) for _ in range(31)]
    return second_month


def join_two_month(first_month: list[int], second_month: list[int]) -> list[int]:
    result_array = first_month.extend(second_month)
    return result_array


# 8. Преобразовать список температур из Цельсия в Фаренгейты.
def celsius_to_fahrenheit(month: list[int]) -> list[float]:
    # (100 °C × 9/5) + 32 = 212 °F
    temp_in_fahrenheit = [celsius * 1.8 for celsius in month]
    return temp_in_fahrenheit


# 11. Очистить список температур.
def clear_temperature_list(month: list[int]):
    month.clear()
