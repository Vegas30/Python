import psycopg2
from psycopg2 import sql
from datetime import datetime


# Устанавливаем соединение с базой данных
def connect_to_db():
   try:
       conn = psycopg2.connect(
           dbname="Employees_management",
           user="postgres",
           password="7773",
           host="localhost",
           port="5432"
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
           CREATE TABLE IF NOT EXISTS departments (
               id SERIAL PRIMARY KEY, -- уникальный идентификатор отдела (первичный ключ).
               name VARCHAR(255) NOT NULL,  -- название отдела (например, "Маркетинг", "Разработка", "HR").
               created_at DATE DEFAULT CURRENT_DATE  -- дата добавления отдела (по умолчанию — текущая дата).
           );


           CREATE TABLE IF NOT EXISTS employees (
               id SERIAL PRIMARY KEY, -- уникальный идентификатор сотрудника (первичный ключ).
               name VARCHAR(255) NOT NULL,  -- Имя сотрудника не может быть пустым
               email VARCHAR(255) UNIQUE NOT NULL,  -- Email сотрудника уникален и не может быть пустым
               phone VARCHAR(20), -- номер телефона сотрудника.
               department_id INT, -- идентификатор отдела, к которому относится сотрудник.
               FOREIGN KEY(department_id) REFERENCES departments(id) ON DELETE CASCADE ON UPDATE CASCADE, -- внешний ключ, ссылающийся на departments, чтобы указать, к какому отделу относится сотрудник.
               hired_at DATE DEFAULT CURRENT_DATE  -- дата найма сотрудника.
           );


           CREATE TABLE IF NOT EXISTS tasks (
               id SERIAL PRIMARY KEY, -- уникальный идентификатор задачи (первичный ключ).
               title VARCHAR(255) NOT NULL,  -- название задачи.
               description TEXT, -- описание задачи.
               status VARCHAR(50) CHECK (status IN ('Создана', 'В процессе', 'Завершена')) DEFAULT 'Создана',  -- статус задачи (например, "Создана", "В процессе", "Завершена").
               assigned_to INT, -- идентификатор сотрудника, которому назначена задача.
               FOREIGN KEY(assigned_to) REFERENCES employees(id), -- внешний ключ, ссылающийся на сотрудника, которому назначена задача.
               created_at DATE DEFAULT CURRENT_DATE,  -- дата создания задачи.
               due_date DATE CHECK (due_date >= created_at)  -- дата выполнения задачи.
           );
           """)
           conn.commit()
           print("Таблицы успешно созданы.")
       except Exception as e:
           print(f"Ошибка при создании таблиц: {e}")
       finally:
           cur.close()
           conn.close()




# Добавление сотрудника
def add_employee(name, email, phone, department_id):
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           cur.execute("""
           INSERT INTO employees (name, email, phone, department_id)
           VALUES (%s, %s, %s, %s)
           """, (name, email, phone, department_id))
           conn.commit()
           print("Сотрудник добавлен.")
       except Exception as e:
           print(f"Ошибка при добавлении сотрудника: {e}")
       finally:
           cur.close()
           conn.close()

def create_task(title, description, status, assigned_to, due_date):
    conn = connect_to_db()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute("""
            INSERT INTO tasks (title, description, status, assigned_to, due_date)
            VALUES (%s, %s, %s, %s, %s)
            """, (title, description, status, assigned_to, due_date))
            conn.commit()
            print(f"Задача '{title}' добавлена для сотрудника с ID {assigned_to}.")
        except Exception as e:
            print(f"Ошибка при добавлении задачи: {e}")
        finally:
            cur.close()
            conn.close()

# Поиск сотрудника
def search_employees(query):
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           query = f"%{query}%"
           cur.execute("""
           SELECT name, email, phone, department_id
           FROM employees
           WHERE name ILIKE %s OR email ILIKE %s OR phone ILIKE %s
           """, (query, query, query))
           employees = cur.fetchall()
           if employees:
               for employee in employees:
                   print(f"Имя: {employee[0]}, email: {employee[1]}, phone: {employee[2]}, department_id: {employee[3]}")
           else:
               print("Сотрудники не найдены.")
       except Exception as e:
           print(f"Ошибка при поиске сотрудников: {e}")
       finally:
           cur.close()
           conn.close()


# Вывод всех сотрудников
def show_all_employees():
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           cur.execute("SELECT * FROM employees")
           employees = cur.fetchall()
           if employees:
               print("Список всех сотрудников:")
               for employee in employees:
                   print(f"ID: {employee[0]}, Имя: {employee[1]}, email: {employee[2]}, phone: {employee[3]}, департамент: {employee[4]}")
           else:
               print("Нет сотрудников.")
       except Exception as e:
           print(f"Ошибка при выводе всех сотрудников: {e}")
       finally:
           cur.close()
           conn.close()


# Вывод всех задач
def show_all_tasks():
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           cur.execute("SELECT * FROM tasks")
           tasks = cur.fetchall()
           if tasks:
               print("Список всех задач:")
               for task in tasks:
                   print(f"ID: {task[0]}, Название: {task[1]}, Описание: {task[2]}, Статус: {task[3]}, Назначена: {task[4]}, Дата создания: {task[5]}, Дата выполнения: {task[6]}")
           else:
               print("Нет задач.")
       except Exception as e:
           print(f"Ошибка при выводе всех задач: {e}")
       finally:
           cur.close()
           conn.close()


# Удаление сотрудника по ID
def delete_employee(employee_id):
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           cur.execute("DELETE FROM employees WHERE id = %s", (employee_id,))
           conn.commit()
           print(f"Сотрудник с ID {employee_id} удален(а).")
       except Exception as e:
           print(f"Ошибка при удалении сотрудника: {e}")
       finally:
           cur.close()
           conn.close()


# Удаление задачи по ID
def delete_task(task_id):
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
           conn.commit()
           print(f"Задача с ID {task_id} удалена.")
       except Exception as e:
           print(f"Ошибка при удалении задачи: {e}")
       finally:
           cur.close()
           conn.close()


# Просмотр всех заказов
def show_employees_with_tasks():
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           cur.execute("""
           SELECT e.id, e.name, e.department_id, t.title, t.description, t.status, t.assigned_to, t.created_at, t.due_date
           FROM employees e
           JOIN tasks t ON e.id = t.assigned_to
           """)
           employees = cur.fetchall()
           if employees:
               for employee in employees:
                   print(f"ID сотрудника: {employee[0]}, Имя: {employee[1]}, department_id: {employee[2]}, Название задачи: {employee[3]}, Описание: {employee[4]}, Статус: {employee[5]}, Назначена: {employee[6]}, Дата создания: {employee[7]}, Дата выполнения: {employee[8]}")
           else:
               print("Нет активных задач.")
       except Exception as e:
           print(f"Ошибка при просмотре заказов: {e}")
       finally:
           cur.close()
           conn.close()


# Просмотр просроченных заказов
# def view_overdue_orders():
#    conn = connect_to_db()
#    if conn:
#        cur = conn.cursor()
#        try:
#            cur.execute("""
#            SELECT o.id, r.name, b.title, o.order_date, o.return_date
#            FROM orders o
#            JOIN readers r ON o.reader_id = r.id
#            JOIN books b ON o.book_id = b.id
#            WHERE o.return_date < CURRENT_DATE AND o.return_date IS NOT NULL
#            """)
#            overdue_orders = cur.fetchall()
#            if overdue_orders:
#                print("Просроченные заказы:")
#                for order in overdue_orders:
#                    print(f"ID заказа: {order[0]}, Читатель: {order[1]}, Книга: {order[2]}, Дата заказа: {order[3]}, Дата возврата: {order[4]}")
#            else:
#                print("Нет просроченных заказов.")
#        except Exception as e:
#            print(f"Ошибка при просмотре просроченных заказов: {e}")
#        finally:
#            cur.close()
#            conn.close()


# Обновление данных книги (например, количества экземпляров)
def update_task_status(task_id, new_status):
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           cur.execute("""
           SELECT due_date FROM tasks WHERE id = %s
           """, (task_id,))
           due_date = cur.fetchone()[0]
           if new_status == "Завершена" and due_date > datetime.now().date():
               print("Невозможно обновить статус на 'Завершена', так как дата завершения еще не наступила.")
               return
           cur.execute("""
           UPDATE tasks
           SET status = %s
           WHERE id = %s
           """, (new_status, task_id))
           conn.commit()
           print(f"Статус задачи с ID {task_id} обновлен.")
       except Exception as e:
           print(f"Ошибка при обновлении статуса задачи: {e}")
       finally:
           cur.close()
           conn.close()

def update_task_due_date(task_id, new_date):
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           cur.execute("""
           UPDATE tasks
           SET due_date = %s
           WHERE id = %s
           """, (new_date, task_id))
           conn.commit()
           print(f"Дата выполнения задачи с ID {task_id} обновлен.")
       except Exception as e:
           print(f"Ошибка при обновлении даты выполнения задачи: {e}")
       finally:
           cur.close()
           conn.close()

def update_task_assigned_to(task_id, new_employee_id):
    conn = connect_to_db()
    if conn:
         cur = conn.cursor()
         try:
              cur.execute("""
              UPDATE tasks
              SET assigned_to = %s
              WHERE id = %s
              """, (new_employee_id, task_id))
              conn.commit()
              print(f"Сотрудник, назначенный на задачу с ID {task_id}, обновлен.")
         except Exception as e:
              print(f"Ошибка при обновлении сотрудника, назначенного на задачу: {e}")
         finally:
              cur.close()
              conn.close()

def update_task_created_at(task_id, new_date):
   conn = connect_to_db()
   if conn:
       cur = conn.cursor()
       try:
           cur.execute("""
           UPDATE tasks
           SET created_at = %s
           WHERE id = %s
           """, (new_date, task_id))
           conn.commit()
           print(f"Дата создания задачи с ID {task_id} обновлен.")
       except Exception as e:
           print(f"Ошибка при обновлении даты создания задачи: {e}")
       finally:
           cur.close()
           conn.close()




# Пример использования:
connect_to_db()

# 1. Создание таблиц
# create_tables()

# 2. Добавление сотрудника
# add_employee("Иван Иванов", "ivan@gmail.com", "1234567890", 1)
# add_employee("Мария Петрова", "maria@example.com", "0987654321", 2)

# 3. Добавление задачи
# create_task("Маркетинг нового продукта", "Описание задачи", "Создана", 1, "2025-06-01")
# create_task("Разработка нового сайта", "Описание задачи", "Создана", 2, "2025-05-01")

# 4. Показать сотрудников и их задачи
# show_employees_with_tasks()

# 5. Update task status
update_task_status(1, "Завершена")

# 6. Показать сотрудников и их задачи еще раз
# show_employees_with_tasks()