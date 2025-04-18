# src/analitic/analitics.py

# 1. Найти индекс первого дня, когда температура превысила заданное значение.
def first_day_index(month: list[int], t: int) -> int:
    """
    Функция находит индекс первого дня, когда температура превысила заданное значение.

    :param month: Список чисел, представляющих собой дневные температуры (в градусах Цельсия) в течение одного месяца (30 дней).
    :param t: Искомая температура должна превысить заданное значение.
    :return: Индекс первого дня, когда температура превысила заданное значение.
    """

    for day in month:
        if day > t:
            index_of_day = month.index(day)
            return index_of_day


# 2. Найти индекс последнего дня, когда температура не превышала заданное значение.

def last_day_index(month: list[int], t: int) -> int:
    """
    Функция находит индекс последнего дня, когда температура не превышала заданное значение

    :param month: Список чисел, представляющих собой дневные температуры (в градусах Цельсия) в течение одного месяца (30 дней).
    :param t: Искомая температура не должна превысить заданное значение.
    :return: Индекс последнего дня, когда температура не превышала заданное значение.
    """

    reversed_month = month[::-1]
    for day in reversed_month:
        if day < t:
            index_of_day = month.index(day)
            return index_of_day


# 3. Подсчитать количество дней, когда температура была ниже заданного значения.
def low_tmp_days_amount(month: list[int], t: int) -> int:
    """
    Функция подсчитывает количество дней, когда температура была ниже заданного значения.

    :param month: Список чисел, представляющих собой дневные температуры
    :param t: Заданное значение температуры.
    :return: Кол-во дней.
    """
    result = sum(list(filter(lambda x: t > x, month)))
    return result


# 7. Отфильтровать список, оставив только температуры, превышающие заданное значение.
def high_temp_filter(month: list[int], t: int) -> list[int]:
    """
    Функция отфильтровывает список, оставив только температуры, превышающие заданное значение.

    :param month: Список чисел, представляющих собой дневные температуры.
    :param t: Заданное значение температуры.
    :return: Отфильтрованный список с температурами, превышающими заданное значение.
    """
    new_array = list(filter(lambda x: t < x, month))
    return new_array


# 9. Проверить, был ли хотя бы один день с температурой выше заданного значения.
def any_day_high_level_temp(month: list[int], t: int):
    """
    Функция проверяет, был ли хотя бы один день с температурой выше заданного значения.

    :param month: Список чисел, представляющих собой дневные температуры.
    :param t: Заданное значение температуры.
    :return:
    """
    if any(num > t for num in month):
        print("Верно, был хотя бы один день с температурой выше заданного значения")
    else:
        print("Не верно, не было хотя бы одного дня с температурой выше заданного значения")


# 10. Проверить, были ли все дни с температурой выше заданного значения.
def all_days_high_level_temp(month: list[int], t: int):
    """
    Функция проверяет, были ли все дни с температурой выше заданного значения.

    :param month: Список чисел, представляющих собой дневные температуры.
    :param t: Заданное значение температуры.
    :return:
    """
    if all(num > t for num in month):
        print("Верно, все дни с температурой выше заданного значения")
    else:
        print("Не верно, не все дни с температурой выше заданного значения")


# 12. Отсортировать список температур по возрастанию или убыванию (на
# основе любого выбранного вами ключа).

def sort_list_by_key(month: list[int], selected_key: callable) -> list[int]:
    """
    Функция сортирует список температур по возрастанию или убыванию (на основе любого выбранного вами ключа).

    :param month: Список чисел, представляющих собой дневные температуры.
    :param selected_key: Выбранный вами ключ.
    :return: Отсортированный список температур по возрастанию или убыванию (на основе любого выбранного вами ключа).
    """
    sorted_month = sorted(month, key=selected_key)
    return sorted_month


# 13. Подсчитать общее количество дней (элементов) в списке температур.
def count_days_amount(month: list[int]) -> int:
    """
    Функция подсчитывает общее количество дней (элементов) в списке температур.

    :param month: Список чисел, представляющих собой дневные температуры.
    :return: Количество дней (элементов) в списке температур.
    """
    days_amount = len(month)
    return days_amount
