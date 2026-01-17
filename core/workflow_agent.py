from core.agent import Agent

class WorkflowAgent(Agent):
    def __init__(self):
        super().__init__("Workflow", "Task Ordering")

    def think(self, modules):
        return modules

    def act(self, modules):
        return [{"module": m, "status": "ready"} for m in modules]
