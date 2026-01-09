import time

from src.config.config import VIDEOS_PATH, VIDEO_NAME, CAMERA_INDEX, USE_VIDEO, FRAME_WIDTH, FRAME_HEIGHT

from src.utils.fps import Fps
from src.utils.yolo import Yolo
from src.utils.mouse import Mouse
from src.utils.cs_window import CS_Window
from src.utils.yolo_window import YoloWindow
from src.utils.virtual_camera import VirtualCamera

class VideoProcessor:
    def __init__(self):
        self.yolo = Yolo()
        self.mouse = Mouse()
        self.cs_window = CS_Window()
        self.yolo_window = YoloWindow()
        self.camera = VirtualCamera()
        self.fps = Fps()


        # For differente resolutions (in virtual OBS camera and CS2)
        if USE_VIDEO:
            self.camera.capture_video_file()
        else:
            self.camera.capture_virtual_camera()
            self.try_find_cs_window()
            
            cs_width, cs_height  = self.cs_window.get_init_cs_resolution()
            cam_width, cam_height = self.camera.get_vitrual_camera_resolution()
            self.mouse.calculate_resolution_difference_factor(cs_width=cs_width, cs_height=cs_height,
                                                               cam_width=cam_width, cam_height=cam_height)

        self.yolo_window.create_window()

    def try_find_cs_window(self):
        attemt = 0  
        max_attemtps = 3
        while not self.cs_window.find_cs_window():
            attemt += 1
            print(f"CS2 wasn't found\n Attempt: {attemt}")
            if attemt >= max_attemtps:
                raise RuntimeError("Couldn't find CS2 window")
            time.sleep(3)


    def frame_process(self):
        try:
            # in case if obs virtual camera frizzed 
            not_captured_frame_counter = 0
            max_not_captured_frame = 5

            while self.camera.check_if_camera_is_open():
                ret, frame = self.camera.read_frame()
                if not ret:
                    not_captured_frame_counter += 1
                    if not_captured_frame_counter >= max_not_captured_frame:
                        print("Video has ended")
                        break
                    continue

            
                self.yolo.predict(frame)
                result_frame = self.yolo.get_result_frame()

                boxes = self.yolo.get_boxes()
                if len(boxes) > 0 and self.cs_window.is_cs_focused():

                    detection = boxes[0]
                    cs_res = self.cs_window.get_client_cs_window_center()
                    self.mouse.move_mouse_calculations(cs_res[0], cs_res[1], detection[0], detection[1])
                
                
                self.fps.update()

                self.yolo_window.put_fps_on_frame(result_frame, self.fps.get_current_fps_value())
                self.yolo_window.put_allowed_mouse(result_frame, self.mouse.get_is_movement_allowed())
                self.yolo_window.display_frame(result_frame)
        except KeyboardInterrupt:
            print("User stopped program")
        except Exception as e:
            raise RuntimeError(e)
