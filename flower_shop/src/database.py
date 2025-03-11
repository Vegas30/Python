import psycopg2
import logging


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="flower_db",
            user='postgres',
            password='12345678',
            host='localhost',
            port='5434'
        )

        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            self.conn.commit()
            return True
        except Exception as e:
            logging.error(f"Database error: {str(e)}")
            self.conn.rollback()
            return False
