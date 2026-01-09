import cv2
from src.config.config import FRAME_HEIGHT, FRAME_WIDTH

class YoloWindow:
    def __del__(self):
        cv2.destroyAllWindows()

    def create_window(self):
        cv2.namedWindow("YOLO", cv2.WINDOW_NORMAL) 
        cv2.resizeWindow("YOLO", FRAME_WIDTH, FRAME_HEIGHT)

    def put_fps_on_frame(self, frame, fps_value):
        cv2.putText(frame, f'{fps_value}', (10, 30),
                    cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 255), 2, 10)
        
    def display_frame(self, frame):
        cv2.imshow("YOLO", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            raise KeyboardInterrupt
    
    def put_allowed_mouse(self, frame, value: bool):
        if value:
            cv2.putText(frame, "Allowed", (10, 50),
                    cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 0), 2, 10)
        else:
            cv2.putText(frame, "Not Allowed", (10, 50),
                    cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 255), 2, 10)