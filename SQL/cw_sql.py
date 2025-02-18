import psycopg2
from psycopg2 import sql
from datetime import datetime


# Устанавливаем соединение с базой данных
def connect_to_db():
   try:
       conn = psycopg2.connect(
           dbname="Python_41",
           user="postgres",
           password="12345678",
           host="localhost",
           port="5434"
       )
       return conn
   except Exception as e:
       print(f"Ошибка при подключении к базе данных: {e}")
       return None


# Создание таблиц
def create_tables():
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           cur.execute("""
           CREATE TABLE IF NOT EXISTS books (
               id SERIAL PRIMARY KEY,
               title VARCHAR(255) NOT NULL,  -- Название книги не может быть пустым
               author VARCHAR(255) NOT NULL,  -- Автор не может быть пустым
               genre VARCHAR(100) NOT NULL,  -- Жанр не может быть пустым
               available_count INT CHECK (available_count >= 0) DEFAULT 0,  -- Количество экземпляров книги не может быть отрицательным, значение по умолчанию 0
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Время добавления книги
               updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Время последнего обновления книги
           );


           CREATE TABLE IF NOT EXISTS readers (
               id SERIAL PRIMARY KEY,
               name VARCHAR(255) NOT NULL,  -- Имя читателя не может быть пустым
               email VARCHAR(255) UNIQUE NOT NULL,  -- Email читателя уникален и не может быть пустым
               phone VARCHAR(20),
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Время добавления читателя
           );


           CREATE TABLE IF NOT EXISTS orders (
               id SERIAL PRIMARY KEY,
               reader_id INT,
               book_id INT,
               order_date DATE DEFAULT CURRENT_DATE,  -- Дата заказа по умолчанию - текущая дата
               return_date DATE,
               FOREIGN KEY(reader_id) REFERENCES readers(id)
                   ON DELETE CASCADE ON UPDATE CASCADE,
               FOREIGN KEY(book_id) REFERENCES books(id)
                   ON DELETE CASCADE ON UPDATE CASCADE,
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Время добавления заказа
           );
           """)
           conn.commit()
           print("Таблицы успешно созданы.")
       except Exception as e:
           print(f"Ошибка при создании таблиц: {e}")
       finally:
           cur.close()
           conn.close()




# Добавление книги
def add_book(title, author, genre, available_count):
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           cur.execute("""
           INSERT INTO books (title, author, genre, available_count)
           VALUES (%s, %s, %s, %s)
           """, (title, author, genre, available_count))
           conn.commit()
           print("Книга добавлена.")
       except Exception as e:
           print(f"Ошибка при добавлении книги: {e}")
       finally:
           cur.close()
           conn.close()


# Поиск книг
def search_books(query):
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           query = f"%{query}%"
           cur.execute("""
           SELECT title, author, genre, available_count
           FROM books
           WHERE title ILIKE %s OR author ILIKE %s OR genre ILIKE %s
           """, (query, query, query))
           books = cur.fetchall()
           if books:
               for book in books:
                   print(f"Название: {book[0]}, Автор: {book[1]}, Жанр: {book[2]}, Доступно: {book[3]}")
           else:
               print("Книги не найдены.")
       except Exception as e:
           print(f"Ошибка при поиске книг: {e}")
       finally:
           cur.close()
           conn.close()


# Вывод всех книг
def show_all_books():
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           cur.execute("SELECT * FROM books")
           books = cur.fetchall()
           if books:
               print("Список всех книг в библиотеке:")
               for book in books:
                   print(f"ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}, Жанр: {book[3]}, Доступно: {book[4]}")
           else:
               print("В библиотеке нет книг.")
       except Exception as e:
           print(f"Ошибка при выводе всех книг: {e}")
       finally:
           cur.close()
           conn.close()


# Вывод всех читателей
def show_all_readers():
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           cur.execute("SELECT * FROM readers")
           readers = cur.fetchall()
           if readers:
               print("Список всех читателей:")
               for reader in readers:
                   print(f"ID: {reader[0]}, Имя: {reader[1]}, Email: {reader[2]}, Телефон: {reader[3]}")
           else:
               print("Нет зарегистрированных читателей.")
       except Exception as e:
           print(f"Ошибка при выводе всех читателей: {e}")
       finally:
           cur.close()
           conn.close()


# Удаление книги по ID
def delete_book(book_id):
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           cur.execute("DELETE FROM books WHERE id = %s", (book_id,))
           conn.commit()
           print(f"Книга с ID {book_id} удалена.")
       except Exception as e:
           print(f"Ошибка при удалении книги: {e}")
       finally:
           cur.close()
           conn.close()


# Удаление читателя по ID
def delete_reader(reader_id):
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           cur.execute("DELETE FROM readers WHERE id = %s", (reader_id,))
           conn.commit()
           print(f"Читатель с ID {reader_id} удален.")
       except Exception as e:
           print(f"Ошибка при удалении читателя: {e}")
       finally:
           cur.close()
           conn.close()


# Просмотр всех заказов
def view_all_orders():
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           cur.execute("""
           SELECT o.id, r.name, b.title, o.order_date, o.return_date
           FROM orders o
           JOIN readers r ON o.reader_id = r.id
           JOIN books b ON o.book_id = b.id
           """)
           orders = cur.fetchall()
           if orders:
               for order in orders:
                   print(f"ID заказа: {order[0]}, Читатель: {order[1]}, Книга: {order[2]}, Дата заказа: {order[3]}, Дата возврата: {order[4]}")
           else:
               print("Нет активных заказов.")
       except Exception as e:
           print(f"Ошибка при просмотре заказов: {e}")
       finally:
           cur.close()
           conn.close()


# Просмотр просроченных заказов
def view_overdue_orders():
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           cur.execute("""
           SELECT o.id, r.name, b.title, o.order_date, o.return_date
           FROM orders o
           JOIN readers r ON o.reader_id = r.id
           JOIN books b ON o.book_id = b.id
           WHERE o.return_date < CURRENT_DATE AND o.return_date IS NOT NULL
           """)
           overdue_orders = cur.fetchall()
           if overdue_orders:
               print("Просроченные заказы:")
               for order in overdue_orders:
                   print(f"ID заказа: {order[0]}, Читатель: {order[1]}, Книга: {order[2]}, Дата заказа: {order[3]}, Дата возврата: {order[4]}")
           else:
               print("Нет просроченных заказов.")
       except Exception as e:
           print(f"Ошибка при просмотре просроченных заказов: {e}")
       finally:
           cur.close()
           conn.close()


# Обновление данных книги (например, количества экземпляров)
def update_book_count(book_id, new_count):
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           cur.execute("""
           UPDATE books
           SET available_count = %s
           WHERE id = %s
           """, (new_count, book_id))
           conn.commit()
           print(f"Количество экземпляров книги с ID {book_id} обновлено.")
       except Exception as e:
           print(f"Ошибка при обновлении количества экземпляров: {e}")
       finally:
           cur.close()
           conn.close()


# Пример использования:
# 1. Создание таблиц
create_tables()


# # 2. Добавление книги
# add_book("Python для начинающих", "Иван Иванов", "Программирование", 5)


# # 3. Вывод всех книг
show_all_books()
#
# # 4. Удаление книги
#delete_book(1)
#
# # 5. Просмотр всех заказов
view_all_orders()
#
# # 6. Просмотр просроченных заказов
view_overdue_orders()
#
# # 7. Обновление количества экземпляров книги
update_book_count(2, 10)

