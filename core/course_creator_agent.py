from core.agent import Agent

class CourseCreatorAgent(Agent):
    def __init__(self):
        super().__init__("CourseCreator", "Syllabus Builder")

    def think(self, workflow):
        return workflow

    def act(self, workflow):
        return [
            f"{step['module']} syllabus with objectives and outcomes"
            for step in workflow
        ]
