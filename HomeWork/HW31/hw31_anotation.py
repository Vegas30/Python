import random
import string


# 1. Функция для подсчета частоты элементов в списке с возможностью
# выбора элементов для подсчета.
def count_frequencies(items: list[str, int | float], filter_items: list[str, int | float] = None,
                      ignore_case: bool = False) -> dict[any]:
    frequencies = {}
    for item in items:
        if filter_items and item not in filter_items:
            continue
        key = item.lower() if ignore_case and isinstance(item, str) else item
        frequencies[key] = frequencies.get(key, 0) + 1
    return frequencies


# - items: Список элементов (строки, числа или другие объекты), для которых нужно подсчитать частоту.
# - filter_items: Необязательный параметр — список элементов, которые нужно учитывать при подсчете
# (остальные игнорируются).
# - ignore_case: Булево значение, указывающее, нужно ли игнорировать регистр для строк.

# 2. Функция для объединения двух словарей с разными стратегиями
# слияния
def merge_dicts(dict1: list[str, int | float], dict2: list[str, int | float], merge_strategy: str = 'overwrite') -> \
        dict[str, int | float]:
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            if merge_strategy == 'overwrite':
                merged[key] = value
            elif merge_strategy == 'keep':
                continue
            elif merge_strategy == 'sum' and isinstance(value, (int, float)):
                merged[key] += value
        else:
            merged[key] = value
    return merged


# - dict1, dict2: Два словаря, которые нужно объединить.
# - merge_strategy: Строка, определяющая стратегию слияния значений для
# одинаковых ключей ('overwrite' — перезаписывать, 'keep' — сохранять
# старое, 'sum' — складывать, если это числа).

# 3. Функция для обработки данных о студентах (список словарей) и сортировки их по разным полям
def sort_students(students: list[dict[str, any]], sort_by: str = 'name', reverse: bool = False) -> list[dict[str, any]]:
    return sorted(students, key=lambda student: student.get(sort_by), reverse=reverse)


# - students: Список студентов, представленных как словари (например, {'name': 'Иван', 'age': 21}).
# - sort_by: Строка, определяющая, по какому полю сортировать студентов (например, 'name', 'age').
# - reverse: Булево значение, определяющее, сортировать ли в обратном порядке.


# 4. Функция для фильтрации списка чисел по нескольким условиям
def filter_numbers(numbers: list[int | float], min_value=None, max_value=None, even_only=False, odd_only=False):
    result = []
    for num in numbers:
        if min_value is not None and num < min_value:
            continue
        if max_value is not None and num > max_value:
            continue
        if even_only and num % 2 != 0:
            continue
        if odd_only and num % 2 != 1:
            continue
        result.append(num)
    return result


# - numbers: Список чисел для фильтрации.
# - min_value: Минимальное значение для фильтрации (включительно). Если None, фильтрация по этому параметру не выполняется.
# - max_value: Максимальное значение для фильтрации (включительно).
# - even_only: Если True, возвращаются только четные числа.
# - odd_only: Если True, возвращаются только нечетные числа.

# 5. Функция для получения пересечения нескольких списков с возможностью игнорирования регистров (если элементы строки)
def intersect_lists(*lists: list[any], ignore_case: bool = False) -> list[any]:
    if not lists:
        return []
    common = set(lists[0])
    for lst in lists[1:]:
        if ignore_case and all(isinstance(i, str) for i in lst):
            common &= set(i.lower() for i in lst)
        else:
            common &= set(lst)
    return list(common)


# - *lists: Произвольное количество списков, для которых нужно найти общие элементы.
# - ignore_case: Если True, строки сравниваются без учета регистра.

# 6. Функция для генерации случайного пароля с заданными параметрами


def generate_password(length: int = 8, use_upper: bool = True, use_digits=True, use_special=True) -> str:
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


# - length: Длина генерируемого пароля (по умолчанию 8 символов).
# - use_upper: Если True, в пароле будут использоваться заглавные буквы.
# - use_digits: Если True, в пароле будут использоваться цифры.
# - use_special: Если True, в пароле будут использоваться специальные
# символы (например, @, #, !).

# 7. Функция для вычисления среднего значения по нескольким спискам
# чисел, исключая пропущенные данные (None)
def calculate_averages(*number_lists: list[int | float]) -> list[int | float]:
    averages = []
    for lst in number_lists:
        filtered_numbers = [num for num in lst if num is not None]
        if filtered_numbers:
            avg = sum(filtered_numbers) / len(filtered_numbers)
            averages.append(avg)
        else:
            averages.append(None)
    return averages


# - *number_lists: Произвольное количество списков чисел, в которых
# нужно вычислить среднее значение, исключая None.

# 8. Функция для поиска подстрок в нескольких строках и подсчета их
# количества

def find_substrings(strings: list[str], substrings: list[str]) -> int:
    result = {sub: 0 for sub in substrings}
    for s in strings:
        for sub in substrings:
            result[sub] += s.count(sub)

    return result


# - strings: Список строк, в которых нужно искать подстроки.
# - substrings: Список подстрок, которые нужно найти в строках.

# 9. Функция для обновления данных о сотрудниках (список словарей) с
# возможностью удаления старых записей
def update_employees(employees: list[dict[str, any]], updates: list[dict[str, any]],
                     delete_absent: bool = False) -> list[dict[str, any]]:
    employee_map = {e['id']: e for e in employees}
    for update in updates:
        if update['id'] in employee_map:
            employee_map[update['id']].update(update)
        else:
            employee_map[update['id']] = update
        if delete_absent:
            employee_map = {k: v for k, v in employee_map.items() if k in [u['id'] for u in updates]}
    return list(employee_map.values())


# - employees: Список словарей с информацией о сотрудниках (например,
# {'id': 1, 'name': 'Анна'}).
# - updates: Список обновлений для сотрудников (также словари с
# ключами, такими как id, name, и т.д.).
# - delete_absent: Если True, сотрудники, отсутствующие в обновлениях,
# будут удалены из списка.


# 10. Функция для подсчета суммы цен товаров с учётом скидок и налогов
def calculate_total_price(items: list[dict[str, str | float]], discounts: dict[str, float] = None,
                          taxes: dict[str, float] = None) -> float:
    total = 0
    for item in items:
        price = item['price']
        if discounts and item['name'] in discounts:
            price -= price * discounts[item['name']]
        if taxes and item['category'] in taxes:
            price += price * taxes[item['category']]
        total += price
    return total


# - items: Список товаров, где каждый товар — это словарь с ценой,
# именем и категорией (например, {'name': 'яблоко', 'price': 50, 'category': 'фрукты'}).
# - discounts: Словарь скидок по именам товаров (например, {'яблоко': 0.1} означает 10% скидку на яблоки).
# - taxes: Словарь налогов по категориям товаров (например, {'фрукты': 0.07} означает 7% налог на фрукты).

# 11. Функция для проверки совпадения двух наборов данных с учетом
# порядка элементов

def compare_data_sets(set1: iter, set2: iter, check_order: bool = True) -> bool:
    if check_order:
        return set1 == set2
    return sorted(set1) == sorted(set2)


# - set1, set2: Два набора данных для сравнения (могут быть списками,
# кортежами или другими итерируемыми объектами).
# - check_order: Если True, сравнивается и порядок элементов. Если False,
# сравниваются только сами элементы, независимо от порядка.

# 12. Функция для конвертации значений температуры между различными
# системами измерений
def convert_temperature(value: int | float, from_unit: int | float = 'C', to_unit: int | float = 'F') -> float:
    if from_unit == to_unit:
        return value
    if from_unit == 'C' and to_unit == 'F':
        return (value * 9 / 5) + 32
    if from_unit == 'F' and to_unit == 'C':
        return (value - 32) * 5 / 9
    raise ValueError('Invalid units')


# - value: Значение температуры для конвертации.
# - from_unit: Исходная система измерения (например, 'C' для Цельсия или 'F' для Фаренгейта).
# - to_unit: Целевая система измерения.

# 13. Функция для генерации отчета по продажам с возможностью
# сортировки и фильтрации по категории
def generate_sales_report(sales: list[dict[str, any]], category: str = None, sort_by: str = 'total',
                          descending: bool = False) -> list[dict[str, any]]:
    filtered_sales = [sale for sale in sales if category is None or sale['category'] == category]
    return sorted(filtered_sales, key=lambda s: s[sort_by], reverse=descending)


# - sales: Список продаж, где каждая продажа представлена как словарь
# (например, {'item': 'компьютер', 'total': 500, 'category': 'техника'}).
# - category: Категория товаров для фильтрации отчета (например,
# 'техника').
# - sort_by: Поле для сортировки (например, 'total' для сортировки по
# общей сумме).
# - descending: Если True, сортировка будет в убывающем порядке.


def main():
    pass


if __name__ == '__main__':
    main()
