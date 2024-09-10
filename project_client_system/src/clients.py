# src/clients.py

def filter_clients(clients: list[dict], min_age: int, tag: str):
    """
    Фильтрует клиентов по минимальному возрасту и наличию определенного тега

    :param clients: Список клиентов, каждый клиент представлен словарем
    :param min_age: Минимальный возраст для фильтрации
    :param tag: Тег, который должен быть у клиента
    :return:
    """
    if min_age <= 0:
        raise ValueError("Возраст должен быть больше нуля")

    try:
        return [f"Клиент: {client['name']}, возраст: {client['age']}" for client in clients if client['age'] >= min_age and tag in client['tags']]
    except KeyError as e:
        print(f"Ошибка отсутствует ключ с таким клиентом - {e}")
        return []


def extract_emails():
    pass


def group_by_tag():
    pass


def average_age_by_tag():
    pass


def transform_client_data():
    pass


def generate_report():
    pass