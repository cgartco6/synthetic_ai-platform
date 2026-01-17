import cv2
import time

class ProctorAgent:
    def monitor(self, duration=60):
        cap = cv2.VideoCapture(0)
        start = time.time()
        events = []

        while time.time() - start < duration:
            ret, frame = cap.read()
            if not ret:
                events.append("Camera lost")
                break

        cap.release()
        return events
