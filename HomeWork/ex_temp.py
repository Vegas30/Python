# 1. Найти индекс первого дня, когда температура превысила заданное значение.
def first_day_index(month, t):
    for day in month:
        if day > t:
            index_of_day = month.index(day)
            return index_of_day


# 2. Найти индекс последнего дня, когда температура не превышала заданное значение.
def last_day_index(month, t):
    reversed_month = month[::-1]
    for day in reversed_month:
        if day < t:
            index_of_day = month.index(day)
            return index_of_day