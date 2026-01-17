from core.agent import Agent

class ContentAgent(Agent):
    def __init__(self):
        super().__init__("Content", "Lesson Generator")

    def think(self, syllabus):
        return syllabus

    def act(self, syllabus):
        lessons = []
        for s in syllabus:
            lessons.append({
                "title": s,
                "content": f"Full detailed lesson for {s}"
            })
        return lessons
