from datetime import datetime
import sqlite3

class CertificationAgent:
    def __init__(self):
        self.conn = sqlite3.connect("knowledge/courses.db")
        self.cursor = self.conn.cursor()

    def issue(self, student_id, domain):
        self.cursor.execute(
            "INSERT INTO certificates VALUES (?, ?, ?)",
            (student_id, domain, datetime.now().isoformat())
        )
        self.conn.commit()
        return f"Certificate issued for {domain}"
