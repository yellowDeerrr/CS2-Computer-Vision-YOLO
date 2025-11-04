import cv2 
from config import CAMERA_INDEX, FRAME_WIDTH, FRAME_HEIGHT

class Cv2Utils:
    def __init__(self):
        cv2.namedWindow("Counter Strike 2", cv2.WINDOW_NORMAL)  # Create a resizable window
        cv2.resizeWindow("Counter Strike 2", FRAME_WIDTH, FRAME_HEIGHT)
        self.cam = cv2.VideoCapture(CAMERA_INDEX) 
        
        if not self.cam.isOpened():
            print("❌ Error opening video file")
            return
        
    def isOpened(self):
        return self.cam.isOpened()
    
    def read(self):
        if self.cam is None:
            return False, None
        return self.cam.read()
    
    def release(self):
        if self.cam is not None:
            self.cam.release()
        
    def display_overlay(self, frame, fps, detection_counts):
            # Draw FPS
            cv2.putText(frame, f'FPS: {fps}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Draw detection counts
            y_pos = 70
            for class_name, count in detection_counts.items():
                text = f'{class_name}: {count}'
                cv2.putText(frame, text, (10, y_pos),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
                y_pos += 35
            
            return frame
    