class EvolutionEngine:
    def __init__(self, memory):
        self.memory = memory

    def evaluate_course(self, course_package):
        score = len(course_package["package"])
        return score

    def evolve(self, domain):
        courses = self.memory.fetch_all()
        relevant = [c for c in courses if c[1] == domain]
        if not relevant:
            return "No evolution needed"

        return f"Course '{domain}' expanded using feedback loops"
