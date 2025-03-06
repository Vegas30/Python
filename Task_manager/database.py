import psycopg2
from psycopg2 import sql


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname='task_manager',
            user='postgres',
            password='7773',
            host='localhost',
            port='5432'
        )
        self.cur = self.connection.cursor()

    def get_tasks(self):
        # query = sql.SQL("SELECT * FROM {}").format(sql.Identifier('tasks'))
        query = sql.SQL("""
            SELECT * FROM tasks
            JOIN categories ON tasks.category_id = categories.id
        """)
        self.cur.execute(query)
        return self.cur.fetchall()

    def delete_task(self, task_id):
        query = sql.SQL("DELETE FROM tasks WHERE id = %s").format(sql.Identifier('tasks'))
        self.cur.execute(query, (task_id,))
        self.connection.commit()

    def close(self):
        self.cur.close()
        self.connection.close()
