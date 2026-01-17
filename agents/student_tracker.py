import sqlite3

class StudentTracker:
    def __init__(self):
        self.conn = sqlite3.connect("knowledge/courses.db")
        self.cursor = self.conn.cursor()

    def register(self, name, email):
        self.cursor.execute(
            "INSERT INTO students (name, email) VALUES (?, ?)",
            (name, email)
        )
        self.conn.commit()

    def update_progress(self, student_id, domain, completion):
        self.cursor.execute(
            "INSERT INTO progress VALUES (?, ?, ?)",
            (student_id, domain, completion)
        )
        self.conn.commit()
