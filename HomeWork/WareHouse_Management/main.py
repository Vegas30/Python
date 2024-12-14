# WareHouse_Management/main.py
from operations.operations_file import load_items_from_file, save_items_to_file
import csv
import json

FILE_PATH = "data/warehouse.json"


def load_items():
    """Загружает товары из файла JSON"""
    return load_items_from_file(FILE_PATH) or []


def add_item(items, item, file_path):
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
    return "Ошибка: товар с таким названием не найден."


def export_items_to_csv(items, csv_file):
    try:
        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'category', 'quantity', 'price', 'tags', 'locations'])
            for item in items:
                writer.writerow([
                    item['name'],
                    item['category'],
                    item['quantity'],
                    item['price'],
                    ','.join(item['tags']),
                    ' '.join(item['locations'])
                ])
        return "Данные успешно экспортированы в operations."
    except Exception as e:
        return f"Ошибка при экспорте в operations: {e}"


def import_items_from_json(json_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            items = json.load(f)
            for item in items:
                if not all(key in item for key in ['name', 'category', 'quantity', 'price', 'tags', 'locations']):
                    raise ValueError("Некорректная структура данных.")
            return items
    except FileNotFoundError:
        return "Ошибка: файл не найден."
    except json.JSONDecodeError:
        return "Ошибка: некорректный формат JSON."
    except ValueError as e:
        return f"Ошибка: {e}"


def generate_warehouse_report(items, report_file):
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            for item in items:
                if not item['locations']:
                    raise ValueError(f"У товара '{item['name']}' отсутствуют местоположения.")
                f.write(
                    f"Товар: {item['name']}, Количество: {item['quantity']}, Местоположения: {', '.join(item['locations'])}\n")
        return "Отчет успешно создан."
    except Exception as e:
        return f"Ошибка при создании отчета: {e}"


def main():
    """Консольное приложение для управления складом товаров."""

    items = load_items()

    new_item = {
        "name": "Table",
        "category": "Furniture",
        "quantity": 8,
        "price": 150.50,
        "tags": ["office", "sale"],
        "locations": ["C1", "C2"]
    }

    print(add_item(items, new_item, file_path))
    print(remove_item(items, "Chair", file_path))
    print(filter_items_by_category_and_tags(items, "Furniture", ["sale"], "filtered_items.json"))
    print(find_items_by_location(items, "A1", "items_at_location.json"))
    print(update_item_quantity(items, "Laptop", 12, file_path))
    print(export_items_to_csv(items, "warehouse.csv"))
    print(import_items_from_json("import_data.json"))
    print(generate_warehouse_report(items, "warehouse_report.txt"))

    while True:
        print("\nПРИОЛЖЕНИЕ ПО УПРАВЛЕНИЮ СКЛАДОМ ТОВАРОВ")
        print("-" * 40)
        print("Выберите действие:")
        print("1. Добавление товара.")
        print("2. Удаление товара.")
        print("3. Фильтрация товара по категории и тегам.")
        print("4. Поиск товара по местоположению товара на складе.")
        print("5. Изменение количества товара.")
        print("6. Экспорт данных о товарах в CVS файл.")
        print("7. Импорт данных о товарах из JSON файла.")
        print("8. Генерация отчета о товарах на складе.")

        choice = input("Введите номер действия: ")
        if choice == "1":
            new_item = {
                "name": input("Введите наименование товара, например Table: "),
                "category": input("Введите категорию товара, например Furniture: "),
                "quantity": int(input("Введите количество товара в виде целого числа, например 8: ")),
                "price": round(float(input("Введите цену товара, например 150.50: ")), 2),
                "tags": set(input("Введите метки товара (tags) через запятую, например office, sale: ").split(', ')),
                "locations": ["C1", "C2"]
            }


# Пример использования
if __name__ == "__main__":
    main()
