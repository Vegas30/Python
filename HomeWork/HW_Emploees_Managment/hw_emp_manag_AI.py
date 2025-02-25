import psycopg2
from psycopg2 import sql

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="Emploees_management_AI",
            user="postgres",
            password="7773",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return None

def create_tables():
    conn = connect_to_db()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute("""
            CREATE TABLE IF NOT EXISTS departments (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                created_at DATE DEFAULT CURRENT_DATE
            );

            CREATE TABLE IF NOT EXISTS employees (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                phone VARCHAR(20),
                department_id INT REFERENCES departments(id) ON DELETE CASCADE,
                hired_at DATE DEFAULT CURRENT_DATE
            );

            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                description TEXT,
                status VARCHAR(50) CHECK (status IN ('Создана', 'В процессе', 'Завершена')) DEFAULT 'Создана',
                assigned_to INT REFERENCES employees(id),
                created_at DATE DEFAULT CURRENT_DATE,
                due_date DATE CHECK (due_date >= created_at)
            );
            """)
            conn.commit()
            print("Таблицы успешно созданы.")
        except Exception as e:
            print(f"Ошибка при создании таблиц: {e}")
        finally:
            cur.close()
            conn.close()

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
            print(f"Сотрудник {name} добавлен.")
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

def update_task_status(task_id, new_status):
    conn = connect_to_db()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute("SELECT due_date FROM tasks WHERE id = %s", (task_id,))
            due_date = cur.fetchone()[0]
            if new_status == 'Завершена' and due_date > datetime.now().date():
                print("Невозможно обновить статус на 'Завершена', так как задача еще не должна быть выполнена.")
                return
            cur.execute("""
            UPDATE tasks
            SET status = %s
            WHERE id = %s
            """, (new_status, task_id))
            conn.commit()
            print(f"Статус задачи с ID {task_id} обновлен на '{new_status}'.")
        except Exception as e:
            print(f"Ошибка при обновлении статуса задачи: {e}")
        finally:
            cur.close()
            conn.close()


def show_employees_with_tasks():
    conn = connect_to_db()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute("""
            SELECT e.name, t.title, t.status, t.due_date
            FROM employees e
            JOIN tasks t ON e.id = t.assigned_to
            """)
            employees_tasks = cur.fetchall()
            if employees_tasks:
                print("Сотрудники и их задачи:")
                for emp_task in employees_tasks:
                    print(f"{emp_task[0]} - {emp_task[1]} (Статус: {emp_task[2]}, Дата выполнения: {emp_task[3]})")
            else:
                print("Нет задач для отображения.")
        except Exception as e:
            print(f"Ошибка при выводе сотрудников и их задач: {e}")
        finally:
            cur.close()
            conn.close()


connect_to_db()
# Create tables
create_tables()

# Add employees
add_employee("Иван Иванов", "ivan@example.com", "1234567890", 1)
add_employee("Мария Петрова", "maria@example.com", "0987654321", 2)

# Create tasks
create_task("Маркетинг нового продукта", "Описание задачи", "Создана", 1, "2025-06-01")
create_task("Разработка нового сайта", "Описание задачи", "Создана", 2, "2025-05-01")

# Show employees with their tasks
show_employees_with_tasks()

# Update task status
update_task_status(1, "Завершена")

# Show employees with their tasks again
show_employees_with_tasks()