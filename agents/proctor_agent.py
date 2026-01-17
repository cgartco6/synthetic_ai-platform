import cv2

class ProctorAgent:
    def __init__(self):
        self.detector = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

    def monitor(self):
        cap = cv2.VideoCapture(0)
        violations = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            faces = self.detector.detectMultiScale(frame, 1.3, 5)
            if len(faces) != 1:
                violations += 1

            if violations > 3:
                break

        cap.release()
        return violations
