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
        return [f"Клиент: {client['name']}, возраст: {client['age']}" for client in clients if
                client['age'] >= min_age and tag in client['tags']]
    except KeyError as e:
        print(f"Ошибка отсутствует ключ с таким клиентом - {e}")
        return []


def extract_emails(clients: list[dict]) -> list[str]:
    """

    :param clients:
    :return:
    """
    return [
        f"Клиент: {client['name']} - {client['email']}" if 'email' in client else f"Клиент: {client['name']} - email отсутствует"
        for client in clients]

    # return list(map(lambda x: f"Клиент: {x['name']} - {x['email']}" if 'email' in x else f"Клиент: {x['name']} - email отсутствует", clients))


def group_by_tag(clients: list[dict]) -> dict[str, list[str]]:
    """
    Группирует клиентов по тегам
    :param clients: Список клиентов
    :return: Словарь, где ключ - это тегб а значение - список клиентов с
    """
    try:
        tag_groups = {}
        for client in clients:
            for tag in client['tags']:
                if tag not in tag_groups:
                    tag_groups[tag] = []
                tag_groups[tag].append(client['name'])
        return tag_groups
    except KeyError as e:
        print("Ошибка ключ не найден.", e)


def average_age_by_tag(clients: list[dict]) -> dict[str, float]:
    """

    :param clients:
    :return:
    """
    try:
        tag_total = {}
        tag_count = {}

        for client in clients:
            for tag in client['tags']:
                tag_total[tag] = tag_total.get(tag, 0) + client['age']
                tag_count[tag] = tag_count.get(tag, 0) + 1
        return {tag: round(tag_total[tag] / tag_count[tag]) for tag in tag_total}
    except KeyError as e:
        print("Ключ не найден", e)
    except ZeroDivisionError as e:
        print("Ошибка деления на ноль", e)


def transform_client_data(clients: list[dict]) -> list[set[str,int]]:
    pass


def generate_report():
    pass
