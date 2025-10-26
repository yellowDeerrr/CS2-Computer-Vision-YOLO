import time

class FPSCounter:
    """Calculate and track FPS"""
    
    def __init__(self):
        self.fps_time = time.time()
        self.fps_counter = 0
        self.fps_display = 0
    
    def update(self):
        """Update FPS counter"""
        self.fps_counter += 1
        
        # Update FPS display every second
        if time.time() - self.fps_time > 1:
            self.fps_display = self.fps_counter
            self.fps_counter = 0
            self.fps_time = time.time()
    
    def get_fps(self):
        """Get current FPS"""
        return self.fps_display
    
    def reset(self):
        """Reset FPS counter"""
        self.fps_time = time.time()
        self.fps_counter = 0
        self.fps_display = 0