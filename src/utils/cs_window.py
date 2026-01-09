import win32gui as wgui

class CS_Window:
    def __init__(self):
        self.hwnd = None
        self.cs_width, self.cs_height = self.get_fresh_cs_resolution()

        self.center_wight = self.cs_width / 2
        self.center_height = self.cs_height / 2

    def find_cs_window(self):
        def callback (hwnd, title):
            if wgui.IsWindowVisible(hwnd):
                win_title = wgui.GetWindowText(hwnd)
                if title.lower() == win_title.lower():
                    self.hwnd = hwnd
            return True
    
        self.hwnd = None
        wgui.EnumWindows(callback, "Counter-Strike 2")
        return self.hwnd is not None
        
    def is_cs_focused(self):
        foreground_title = wgui.GetWindowText(wgui.GetForegroundWindow())
        return "counter-strike 2" in foreground_title.lower()
    

    def get_fresh_cs_resolution(self):
        if not self.find_cs_window():
            return None
        
        rect = wgui.GetClientRect(self.hwnd)
        client_width = rect[2]
        client_height = rect[3]
        return client_width, client_height
    
    def get_init_cs_resolution(self):
        return self.cs_width, self.cs_height
    
    def get_screen_cs_window_center(self):
        client_width, client_height = self.get_init_cs_resolution()
        
        return wgui.ClientToScreen(self.hwnd, (int(client_width / 2), int(client_height / 2)))
    
    def get_client_cs_window_center(self):
        return self.center_wight, self.center_height
