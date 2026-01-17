from core.agent import Agent

class AssessmentAgent(Agent):
    def __init__(self):
        super().__init__("Assessment", "Evaluation Designer")

    def think(self, lessons):
        return lessons

    def act(self, lessons):
        return [
            f"Exam for {lesson['title']}"
            for lesson in lessons
        ]
