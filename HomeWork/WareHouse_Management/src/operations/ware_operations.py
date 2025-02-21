# WareHouse_Management/src/operations/ware_operations.py

"""Модуль для работы с товарами на складе. """


def generate_unique_item_id(items: list[dict]) -> str:
    """
    Генерирует уникальный ID для товара.

    :param items: Список существующих товаров.
    :type items: list[dict]
    :return: Уникальный ID для нового товара.
    :rtype: str
    """
    item_ids = [item['item_id'] for item in items]
    new_item_id = str(max(map(int, item_ids)) + 1) if item_ids else '1'
    return new_item_id


def add_item(items: list[dict], item: dict) -> None:
    """
    Добавляет новый товар в список товаров.

    :param items: Список существующих товаров.
    :type items: list[dict]
    :param item: Новый товар для добавления.
    :type item: dict
    """
    items.append(item)


def remove_item(items: list[dict], item_id: str) -> bool:
    """
    Удаляет товар из списка по его ID.

    :param items: Список существующих товаров.
    :type items: list[dict]
    :param item_id: ID товара для удаления.
    :type item_id: str
    :return: True, если товар был удален, иначе False.
    :rtype: bool
    """
    for index, item in enumerate(items):
        if item['item_id'] == item_id:
            del items[index]
            # save_items_to_file(items, file_path)
            return True  # "Товар успешно удален."
    return False  # "Ошибка: товар с таким названием не найден."


def filter_items_by_category_and_tags(items: list[dict], category: str, tags: set[str]) -> list[dict] | str:
    """
    Фильтрует товары по категории и тегам. Возвращает список товаров, которые принадлежат указанной категории и содержат хотя бы один из указанных тегов.

    :param items: Список существующих товаров.
    :type items: list[dict]
    :param category: Категория для фильтрации.
    :type category: str
    :param tags: Множество тегов для фильтрации.
    :type tags: set[str]
    :return: Список отфильтрованных товаров или сообщение об ошибке.
    :rtype: list[dict] | str
    """
    if not category:
        return "Ошибка: категория не указана."
    try:
        filtered_items = [item for item in items if (item['category']).lower() == category and set(item['tags']).intersection(tags)]
    except Exception as e:
        return f"Ошибка: {e}"

    return filtered_items


def find_items_by_location(items: list[dict], location: str) -> list[dict]:
    """
    Находит товары по их местоположению.

    :param items: Список существующих товаров.
    :type items: list[dict]
    :param location: Местоположение для поиска.
    :type location: str
    :return: Список товаров, найденных по указанному местоположению.
    :rtype: list[dict]
    """
    found_items = [item for item in items if location in item['locations']]
    # save_items_to_file(found_items, output_file)
    return found_items


def update_item_quantity(items: list[dict], item_name: str, quantity: int) -> bool:
    """
    Обновляет количество товара.

    :param items: Список существующих товаров.
    :type items: list[dict]
    :param item_name: Наименование товара для обновления.
    :type item_name: str
    :param quantity: Новое количество товара.
    :type quantity: int
    :return: True, если количество было обновлено, иначе False.
    :rtype: bool
    """
    for item in items:
        if item['name'] == item_name:
            item['quantity'] = quantity
            # save_items_to_file(items, file_path)
            return True  # "Количество товара успешно обновлено."
    return False  # f"Ошибка: товар с таким названием {item_name} не найден."


def generate_warehouse_report(items: list[dict], report_file: str) -> bool | str:
    """
    Генерирует отчет о товарах на складе.

    :param items: Список существующих товаров.
    :type items: list[dict]
    :param report_file: Путь к файлу отчета.
    :type report_file: str
    :return: Сообщение о результате генерации отчета.
    :rtype: bool | str
    """
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            for item in items:
                if not item['locations']:
                    raise ValueError(f"У товара '{item['name']}' отсутствуют местоположения.")
                f.write(
                    f"ID Товара: {item['item_id']}, Название товара: {item['name']}, Количество: {item['quantity']}, Местоположения: {', '.join(item['locations'])}\n")
        return True
    except Exception as e:
        print(f"Ошибка при создании отчета: {e}")
