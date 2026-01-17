from core.agent import Agent

class TeachingAgent(Agent):
    def __init__(self):
        super().__init__("Teacher", "Instruction Delivery")

    def think(self, content):
        return content

    def act(self, content):
        return f"Teaching session generated for {len(content)} items"
