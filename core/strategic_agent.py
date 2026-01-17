from core.agent import Agent

class StrategicAgent(Agent):
    def __init__(self):
        super().__init__("Strategic", "Domain Decomposition")

    def think(self, domain):
        return f"Break {domain} into mastery modules"

    def act(self, thought):
        return [
            "Foundations",
            "Intermediate Concepts",
            "Advanced Systems",
            "Practical Applications",
            "Assessment"
        ]
