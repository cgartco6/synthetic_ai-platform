class AdaptiveDifficulty:
    def adjust(self, student_score):
        if student_score > 85:
            return "increase"
        elif student_score < 50:
            return "decrease"
        return "maintain"

    def apply(self, lesson, level):
        return f"[{level.upper()} LEVEL] {lesson}"
