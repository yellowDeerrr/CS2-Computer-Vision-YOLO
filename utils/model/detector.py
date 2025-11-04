from ultralytics import YOLO
from config import CONFIDENCE, MODEL_PATH, RENDER_DEVICE




class Detector:
    """Handle CS2 enemy detection using YOLO"""
    
    def __init__(self, model_path=MODEL_PATH, conf_threshold=CONFIDENCE, device=RENDER_DEVICE):

        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold
        self.device = device
            
        print(f"✓ Model loaded successfully on {device}")
    
    def detect(self, frame, verbose=False):
        results = self.model.predict(
            source=frame,
            conf=self.conf_threshold,
            verbose=verbose,
            device=self.device
        )

        return results
    
    def get_detection_counts(self, results):
        detections = results[0].boxes
        detection_counts = {}
        
        for box in detections:
            cls_id = int(box.cls[0])
            class_name = self.model.names[cls_id]
            detection_counts[class_name] = detection_counts.get(class_name, 0) + 1
        
        return detection_counts
    
    def get_positions(self, results):
        detections = results[0].boxes

        for box in detections:
            cls_id = int(box.cls[0])
            class_name = self.model.names[cls_id]
            bbox = box.xyxy[0].tolist()  # [x1, y1, x2, y2]
            print(f"Class: {class_name}, BBox: {bbox}")
        
    
                # Implement shooting logic here
    # def get_detection_details(self, results):
    #     detections = results[0].boxes
    #     details = []
        
    #     for box in detections:
    #         cls_id = int(box.cls[0])
    #         conf = float(box.conf[0])
    #         bbox = box.xyxy[0].tolist()  # [x1, y1, x2, y2]
            
    #         details.append({
    #             'class_id': cls_id,
    #             'class_name': self.model.names[cls_id],
    #             'confidence': conf,
    #             'bbox': bbox
    #         })
        
    #     return details
    
    