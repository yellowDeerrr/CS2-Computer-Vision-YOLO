import ctypes
from pynput import keyboard

import win32gui as wgui

class Mouse:
    def __init__(self):
        self.move_allowed = False
        
        self.scale_x = 1
        self.scale_y = 1
        
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
    
    def __del__(self):
        self.listener.stop()

    def calculate_resolution_difference_factor(self, cs_width, cs_height, cam_width, cam_height):
        self.scale_x = cs_width / cam_width
        self.scale_y = cs_height / cam_height

    def on_press(self, key):
        if key == keyboard.Key.caps_lock:
            self.move_allowed = not self.move_allowed


    def get_mouse_position(self):
        return wgui.GetCursorPos()
    
    def get_is_movement_allowed(self):
        return self.move_allowed
    
    def move_mouse_to_box_center(self, x_cs_center, y_cs_center, x_detection_center, y_detection_center):
        if self.move_allowed and self.is_cs_focused():
            ctypes.windll.user32.mouse_event(0x0001,
                                              int(x_detection_center * self.scale_x - x_cs_center),
                                              int(y_detection_center * self.scale_y - y_cs_center),
                                                0, 0)

    def is_cs_focused(self):
        foreground_title = wgui.GetWindowText(wgui.GetForegroundWindow())
        return "counter-strike 2" in foreground_title.lower()

