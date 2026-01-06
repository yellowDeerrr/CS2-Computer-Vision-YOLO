import time
from collections import deque
from src.config.config import FPS_VALUES_DEQUE_SIZE, UPDATE_FPS_DELAY, ROUND_FPS_DIGITS

class Fps:
    def __init__(self):
        self.update_delay = UPDATE_FPS_DELAY

        self.current_time = time.time()

        self.last_current_fps_update_time = time.time()
        self.fps_updates = 0

        self.total_fps = 0
        self.current_fps_value = 0

        self.last_frame_time = time.time()

        self.fps_values = deque(maxlen=FPS_VALUES_DEQUE_SIZE)

    def get_current_fps_value(self):
        return self.current_fps_value
    
    def update(self):
        self.current_time = time.time()
        
        self.fps_values.append(1 / (self.current_time  - self.last_frame_time))
        self.last_frame_time = self.current_time 

        if self.current_time - self.last_current_fps_update_time >= self.update_delay:
            self.update_current_fps()
            

    def update_current_fps(self):
        self.current_fps_value = round(sum(self.fps_values) / len(self.fps_values), ROUND_FPS_DIGITS) 

        self.fps_updates += 1
        self.total_fps += self.current_fps_value
        self.last_current_fps_update_time = self.current_time
            

    # Average fps calculating by all previously received
    def get_average_fps(self):
        if self.fps_updates != 0:
            return round(self.total_fps / self.fps_updates, 1)
        else:
            return -1