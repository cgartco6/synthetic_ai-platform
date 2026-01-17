from moviepy.editor import TextClip, AudioFileClip, CompositeVideoClip
import os
import pyttsx3

class VideoGenerator:
    def __init__(self, out_dir="videos"):
        self.out_dir = out_dir
        os.makedirs(out_dir, exist_ok=True)
        self.tts = pyttsx3.init()

    def _tts(self, text, audio_path):
        self.tts.save_to_file(text, audio_path)
        self.tts.runAndWait()

    def generate(self, lesson_title, lesson_text):
        audio_path = f"{self.out_dir}/{lesson_title}.wav"
        video_path = f"{self.out_dir}/{lesson_title}.mp4"

        self._tts(lesson_text, audio_path)
        audio = AudioFileClip(audio_path)

        text_clip = TextClip(
            lesson_text[:300],
            fontsize=42,
            size=(1280, 720),
            method="caption",
            color="white",
            bg_color="black"
        ).set_duration(audio.duration)

        video = CompositeVideoClip([text_clip]).set_audio(audio)
        video.write_videofile(video_path, fps=24)

        return video_path
