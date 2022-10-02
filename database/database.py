from config import DB_HOST, DB_NAME, DB_USER, DB_PORT, DB_PASSWORD
import psycopg2

class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            port=DB_PORT,
            password=DB_PASSWORD
        )

    def manager(self, sql, *args,
                fetchone: bool = False,
                fetchall: bool = False,
                commit: bool = False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
            return result

    def create_user_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS users(
            telegram_id BIGINT PRIMARY KEY
        )'''
        self.manager(sql, commit=True)

    def insert_telegram_id(self, telegram_id):
        sql = '''INSERT INTO users (telegram_id)
        VALUES (%s)
        ON CONFLICT DO NOTHING'''
        self.manager(sql, telegram_id, commit=True)

    def select_telegram_id(self):
        sql = '''SELECT telegram_id FROM users'''
        return self.manager(sql, fetchall=True)
