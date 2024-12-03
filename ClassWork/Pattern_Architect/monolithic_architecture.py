# Модуль работы с данными
def get_data_from_db():
    # В реальной ситуации это будет запрос к базе данных
    return {"user_id": 1, "name": "John Doe"}


# Модуль бизнес-логики
def process_data(data):
    # Простой процессинг данных (например, добавление возраста)
    data['age'] = 30
    return data


# Модуль пользовательского интерфейса
def display_data(data):
    print(f"User: {data['name']}, Age: {data['age']}")


# Основная программа
def main():
    # Получаем данные из базы данных
    data = get_data_from_db()


    # Обрабатываем данные
    processed_data = process_data(data)


    # Отображаем данные
    display_data(processed_data)


if __name__ == "__main__":
    main()