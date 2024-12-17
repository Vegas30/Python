# WareHouse_Management/operations/ware_operations.py

from operations.file_operations import save_items_to_file


def add_item(items: list[dict], item: dict, file_path: str):
    if any(existing_item['name'] == item['name'] for existing_item in items):
        return "Ошибка: товар с таким названием уже существует."
    items.append(item)
    save_items_to_file(items, file_path)
    return "Товар успешно добавлен."


def remove_item(items, item_name, file_path):
    for i, item in enumerate(items):
        if item['name'] == item_name:
            del items[i]
            save_items_to_file(items, file_path)
            return "Товар успешно удален."
    return "Ошибка: товар с таким названием не найден."


def filter_items_by_category_and_tags(items, category, tags, output_file):
    if not category:
        return "Ошибка: категория не указана."
    filtered_items = [item for item in items if item['category'] == category and item['tags'] == tags]
    if not filtered_items:
        return "Ошибка: не найдено товаров с указанной категорией и тегами."
    save_items_to_file(filtered_items, output_file)
    return filtered_items


def find_items_by_location(items, location, output_file):
    found_items = [item for item in items if location in item['locations']]
    save_items_to_file(found_items, output_file)
    return found_items


def update_item_quantity(items, item_name, quantity, file_path):
    if quantity < 0:
        return "Ошибка: количество не может быть отрицательным."
    for item in items:
        if item['name'] == item_name:
            item['quantity'] = quantity
            save_items_to_file(items, file_path)
            return "Количество товара успешно обновлено."
    return f"Ошибка: товар с таким названием {item_name} не найден."
