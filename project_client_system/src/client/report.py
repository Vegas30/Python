# src/client/report.py
def transform_client_data(clients: list[dict]) -> list[tuple[str, int]]:
    """"

    :param clients:
    :return:
    """
    # return [(client['name'], client['age']) for client in clients]
    transformed = []
    for client in clients:
        try:
            name = client['name']
            age = client['age']
            transformed.append((name, age))
        except KeyError:
            continue
    return transformed


def generate_report(clients: list[dict]) -> str:
    """
    Генерирует отчет о клиентах.


    :param clients: Список клиентов.
    :return: Строка отчета с информацией о каждом клиенте.
    """
    report_lines = []
    for client in clients:
        try:
            name = client['name']
            age = client['age']
            report_lines.append(f"Клиент: {name}, Возраст: {age}")
        except KeyError:
            report_lines.append("Некорректные данные клиента.")
    return "\n".join(report_lines)
