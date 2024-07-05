import sqlite3

DB_NAME = 'users.db'

# Словарь для хранения ID служебных сообщений
user_message_ids = {}
bot_message_ids = {}

# Хранилище авторизованных админов
authorized_admins = set()

def create_table():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NULL,
                user_id INTEGER NOT NULL
            )
        """)
        conn.commit()

def add_user(username: str, user_id: int):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, user_id) VALUES (?, ?)", (username, user_id))
        conn.commit()

def get_user_id_by_username(username: str) -> int:
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        return result[0] if result else None

def is_user_registered(user_id: int) -> bool:
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM users WHERE user_id = ?", (user_id,))
        return cursor.fetchone() is not None


# Инициализация БД
create_table()
