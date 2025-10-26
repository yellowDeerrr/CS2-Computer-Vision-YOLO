# config.py
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Paths
MODEL_PATH = os.getenv("MODEL_PATH", "models/trained/cs2_model5/best.pt")
VIDEOS_PATH = os.getenv("VIDEOS_PATH", "test_media/videos/")
IMAGES_PATH = os.getenv("IMAGES_PATH", "test_media/images/")
OUTPUT_PATH = os.getenv("OUTPUT_PATH", "output/")

UTILS_PATH = os.getenv("UTILS_PATH", "utils/")
SCRIPTS_PATH = os.getenv("SCRIPTS_PATH", "scripts/")

RENDER_DEVICE = os.getenv("RENDER_DEVICE", 0)  # 0 for GPU

# Model parameters
CONFIDENCE = float(os.getenv("CONFIDENCE", 0.4))

# Camera index
CAMERA_INDEX = int(os.getenv("CAMERA_INDEX", 1))