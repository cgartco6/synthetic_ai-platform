from core.agent import Agent

class ValidationAgent(Agent):
    def __init__(self):
        super().__init__("Validation", "Quality Control")

    def think(self, content):
        return content

    def act(self, content):
        return {
            "status": "validated",
            "package": content
        }
