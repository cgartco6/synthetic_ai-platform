import sqlite3

class Memory:
    def __init__(self):
        self.conn = sqlite3.connect("knowledge/courses.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY,
            domain TEXT,
            content TEXT
        )
        """)
        self.conn.commit()

    def save(self, domain, content):
        self.cursor.execute(
            "INSERT INTO courses (domain, content) VALUES (?, ?)",
            (domain, content)
        )
        self.conn.commit()

    def fetch_all(self):
        return self.cursor.execute("SELECT * FROM courses").fetchall()
