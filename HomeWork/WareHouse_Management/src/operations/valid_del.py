def validate_item_data(item):
    """
    Проверяет корректность данных товара.

    :param item: словарь с данными товара
    :return: True, если данные корректны, иначе строка с сообщением об ошибке
    """
    required_keys = ["item_id", "name", "category", "quantity", "price", "tags", "locations"]

    # Проверка наличия всех обязательных ключей
    for key in required_keys:
        if key not in item:
            return f"Ошибка: отсутствует обязательное поле '{key}'."

    # Проверка типа данных
    if not isinstance(item["item_id"], str):
        return "Ошибка: 'item_id' должен быть строкой."
    if not isinstance(item["name"], str):
        return "Ошибка: 'name' должен быть строкой."
    if not isinstance(item["category"], str):
        return "Ошибка: 'category' должен быть строкой."
    if not isinstance(item["quantity"], int) or item["quantity"] < 0:
        return "Ошибка: 'quantity' должен быть неотрицательным целым числом."
    if not isinstance(item["price"], (int, float)) or item["price"] < 0:
        return "Ошибка: 'price' должен быть неотрицательным числом."
    if not isinstance(item["tags"], list) or not all(isinstance(tag, str) for tag in item["tags"]):
        return "Ошибка: 'tags' должен быть списком строк."
    if not isinstance(item["locations"], list) or not all(isinstance(loc, str) for loc in item["locations"]):
        return "Ошибка: 'locations' должен быть списком строк."

    # Дополнительные проверки
    if not item["name"].strip():
        return "Ошибка: 'name' не может быть пустой строкой."
    if not item["category"].strip():
        return "Ошибка: 'category' не может быть пустой строкой."
    if not item["tags"]:
        return "Ошибка: 'tags' не может быть пустым списком."
    if not item["locations"]:
        return "Ошибка: 'locations' не может быть пустым списком."

    return True
