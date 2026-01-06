import cv2
import os
import time
from src.config.config import VIDEOS_PATH, VIDEO_NAME, CAMERA_INDEX, USE_VIDEO, FRAME_WIDTH, FRAME_HEIGHT
from src.utils.fps import Fps
from src.utils.yolo import Yolo

class VideoProcessor:
    def __init__(self):
        self.fps = Fps()
        self.yolo = Yolo()
        self.cam = None
        cv2.namedWindow("Counter Strike 2", cv2.WINDOW_NORMAL) 
        cv2.resizeWindow("Counter Strike 2", FRAME_WIDTH, FRAME_HEIGHT)

        if USE_VIDEO:
            video_path = os.path.join(VIDEOS_PATH, VIDEO_NAME)
            self.capture_video_file(video_path)
        else:
            self.capture_virtual_camera(CAMERA_INDEX)

    def __del__(self):
        self.destroy_windows()


    def capture_video_file(self, video_path):
        self.cam = cv2.VideoCapture(video_path)
        if not self.cam.isOpened():
            raise RuntimeError(f"Cv2 hasn't captured any frame from {video_path}")

    def capture_virtual_camera(self, camera_index):
        self.cam = cv2.VideoCapture(camera_index)
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
                self.cam = cv2.VideoCapture(camera_index)
                attempts += 1
            if not self.cam.isOpened():
                raise RuntimeError(f"Virtual camera hasn't been captured; Index: {camera_index}")


    def frame_process(self):
        try:
            # in case if obs virtual camera frizzed 
            not_captured_frame_counter = 0
            max_not_captured_frame = 5

            while self.cam.isOpened():
                ret, frame = self.cam.read()
                if not ret:
                    not_captured_frame_counter += 1
                    if not_captured_frame_counter >= max_not_captured_frame:
                        print("Video has ended")
                        break
                    continue

                results = self.yolo.predict(frame)

                annoted_frame = results[0].plot()
                
                self.fps.update()
                self.display_fps(self.fps.get_current_fps_value(), annoted_frame)

                cv2.imshow("Counter Strike 2", annoted_frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    raise KeyboardInterrupt
        except KeyboardInterrupt:
            print("User stopped program")
        except Exception as e:
            raise RuntimeError(e)
            

    def display_fps(self, fps_value, frame):
        cv2.putText(frame, f'{fps_value}', (10, 30),
                    cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 255), 2, 10)

    def destroy_windows(self):
        average_fps = self.fps.get_average_fps()
        if average_fps == -1:
            print("Error occured while calculating average fps")
        else:
            print(f"Average FPS: {average_fps}")

        self.cam.release()
        cv2.destroyAllWindows()