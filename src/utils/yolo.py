from ultralytics import YOLO 
from src.config.config import *

class Yolo:
    def __init__(self):
        try:
            self.yolo = YOLO(MODEL_PATH)
        except FileNotFoundError:
            raise RuntimeError(f"Model was not found there: {MODEL_PATH}")

    def predict(self, frame):
        return self.yolo.predict(
            source=frame,
            conf=CONFIDENCE,
            verbose=False,
            device=RENDER_DEVICE
        )