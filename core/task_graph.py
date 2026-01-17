import networkx as nx

class TaskGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_task(self, task_name, depends_on=None):
        self.graph.add_node(task_name)
        if depends_on:
            for dep in depends_on:
                self.graph.add_edge(dep, task_name)

    def execution_order(self):
        return list(nx.topological_sort(self.graph))
