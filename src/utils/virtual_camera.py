import cv2
import time
import os

from src.config.config import CAMERA_INDEX, VIDEO_NAME, VIDEOS_PATH

class VirtualCamera:
    def __init__(self):
        self.cam = None

    def __del__(self):
        if self.cam is not None:
            self.cam.release()

    def capture_video_file(self):
        video_path = os.path.join(VIDEOS_PATH, VIDEO_NAME)

        self.cam = cv2.VideoCapture(video_path)
        if not self.cam.isOpened():
            raise RuntimeError(f"Cv2 hasn't captured any frame from {video_path}")

    def capture_virtual_camera(self):
        self.cam = cv2.VideoCapture(CAMERA_INDEX)
        if not self.cam.isOpened():
            attempts = 0
            max_attempts = 3
            delay_attempt = 2

            while not self.cam.isOpened():
                if attempts >= max_attempts:
                    break
                print(f"Cv2 hasn't captured any frame from Virtual Camera (Attempt {attempts})\n"
                        "Trying capture...")
                time.sleep(delay_attempt)                    
                self.cam = cv2.VideoCapture(CAMERA_INDEX)
                attempts += 1
            if not self.cam.isOpened():
                raise RuntimeError(f"Virtual camera hasn't been captured; Index: {CAMERA_INDEX}")
            
    def check_if_camera_is_open(self):
        return self.cam.isOpened()

    def read_frame(self):
        return self.cam.read()
    
    def get_vitrual_camera_resolution(self):
        return int(self.cam.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT))