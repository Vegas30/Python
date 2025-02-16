# WareHouse_Management/operations/file_operations.py
import csv
import json
from typing import AnyStr

"""Модуль для работы с файлами"""


def save_items_to_file(items: list[dict], file_path: str) -> None:
    """Функция сохраняет список товаров в файл JSON"""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(items, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ошибка при сохранении в файл: {e}")


def load_items_from_file(file_path: str) -> list[dict]:
    """Функция загружает список товаров из файла JSON"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Файл не найден. Создайте новый список товаров.")
        return []
    except json.JSONDecodeError:
        print("Ошибка чтения файла: некорректный формат JSON.")
        return []

def export_items_to_csv(items: list[dict], csv_file: str) -> str:
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
        return "Данные успешно экспортированы в warehouse.csv."
    except Exception as e:
        return f"Ошибка при экспорте в operations: {e}"


def import_items_from_json(json_file: str) -> list[dict] | str:
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


