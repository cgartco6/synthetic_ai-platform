from agents.voice_teacher import VoiceTeacher

class VideoGenerator:
    def __init__(self):
        self.voice = VoiceTeacher()

    def generate(self, lesson_text):
        script = f"Lesson Script:\n{lesson_text}"
        self.voice.speak(lesson_text)
        return script
