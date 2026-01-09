from ultralytics import YOLO 
from src.config.config import *

class Yolo:
    def __init__(self):
        try:
            self.yolo = YOLO(MODEL_PATH)
            self.results = None
        except FileNotFoundError:
            raise RuntimeError(f"Model was not found there: {MODEL_PATH}")

    def predict(self, frame):
        self.results = self.yolo.predict(
            source=frame,
            conf=CONFIDENCE,
            verbose=False,
            device=RENDER_DEVICE
        )
    
    def get_result_frame(self):
        return self.results[0].plot()
    
    def get_boxes(self):
        # return self.results[0].boxes.xywh
        return self.results[0].boxes.xywh

        # return self.results[0].boxes.xyxyn