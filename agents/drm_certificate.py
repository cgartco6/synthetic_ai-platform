import hashlib
from datetime import datetime

class DRMCertificate:
    def issue(self, student, course):
        payload = f"{student}|{course}|{datetime.utcnow()}"
        signature = hashlib.sha256(payload.encode()).hexdigest()
        return {
            "student": student,
            "course": course,
            "signature": signature
        }

    def verify(self, cert):
        payload = f"{cert['student']}|{cert['course']}"
        return hashlib.sha256(payload.encode()).hexdigest() == cert["signature"]
