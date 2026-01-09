from dotenv import load_dotenv
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ENV_PATH = os.path.join(PROJECT_DIR, ".env")

# Load environment ONCE at module level
load_dotenv(ENV_PATH)

# Paths
MODEL_PATH = os.path.join(PROJECT_DIR, os.getenv("MODEL_PATH", "models/best.pt"))
VIDEOS_PATH = os.path.join(PROJECT_DIR, os.getenv("VIDEOS_PATH", "test_media"))
VIDEO_NAME = os.path.join(VIDEOS_PATH, os.getenv("VIDEO_NAME", "cs_menu.mp4"))

# YOLO
RENDER_DEVICE = os.getenv("RENDER_DEVICE", 0)
CONFIDENCE = float(os.getenv("CONFIDENCE", 0.4))

# Camera
CAMERA_INDEX = int(os.getenv("CAMERA_INDEX", 1))

#Window
FRAME_WIDTH = int(os.getenv("FRAME_WIDTH", 640))
FRAME_HEIGHT = int(os.getenv("FRAME_HEIGHT", 480))

# FPS Counter
UPDATE_FPS_DELAY = float(os.getenv("UPDATE_FPS_DELAY", 0.1))
FPS_VALUES_DEQUE_SIZE = int(os.getenv("FPS_VALUES_DEQUE_SIZE", 10))
ROUND_FPS_DIGITS = int(os.getenv("ROUND_FPS_DIGITS", 2))

# Debug
USE_VIDEO = os.getenv("USE_VIDEO", "0").lower() in ["true", "1", "yes", "on"]