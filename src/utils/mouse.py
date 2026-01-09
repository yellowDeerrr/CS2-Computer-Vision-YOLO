import ctypes
from pynput import keyboard

import win32gui as wgui

class Mouse:
    def __init__(self):
        self.move_allowed = False
        
        self.scale_x = 1
        self.scale_y = 1
        
        self.listener = keyboard.Listener(on_press=self.caps_lock_press)
        self.listener.start()
    
    def __del__(self):
        self.listener.stop()

    def calculate_resolution_difference_factor(self, cs_width, cs_height, cam_width, cam_height):
        self.scale_x = cs_width / cam_width
        self.scale_y = cs_height / cam_height

    def caps_lock_press(self, key):
        if key == keyboard.Key.caps_lock:
            self.move_allowed = not self.move_allowed

    def get_mouse_position(self):
        return wgui.GetCursorPos()
    
    def get_is_movement_allowed(self):
        return self.move_allowed
    
    def move_mouse_calculations(self, x_cs_center, y_cs_center, x_detection_center, y_detection_center):
        self.move_mouse_to(x_detection_center - x_cs_center, y_detection_center - y_cs_center)
    
    def move_mouse_to(self, x: int, y: int):
        if self.move_allowed:
            ctypes.windll.user32.mouse_event(0x0001, int(x), int(y), 0, 0)

