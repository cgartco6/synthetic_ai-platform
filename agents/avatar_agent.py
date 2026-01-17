class TutorAvatar:
    def __init__(self, name, style):
        self.name = name
        self.style = style

    def respond(self, lesson, question):
        return (
            f"{self.name} ({self.style}): "
            f"Let's understand this step by step.\n"
            f"{lesson}\nAnswering: {question}"
        )
