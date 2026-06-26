import sqlite3

DB_NAME = "meeting.db"


def get_db_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS meetings (
            id TEXT PRIMARY KEY,
            title TEXT,
            date TEXT,
            start_time TEXT,
            duration TEXT,
            notes TEXT,
            participants TEXT
        )
    """)
    conn.commit()
    conn.close()
