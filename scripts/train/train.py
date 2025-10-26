from ultralytics import YOLO

# Load pretrained model
print("Loading YOLOv10n model...")
model = YOLO('weights/yolov10n.pt')

# Train on your CS2 dataset
print("Starting training...")
results = model.train(
    data='dataset/data.yaml',
    epochs=100,
    imgsz=640,
    batch=16,
    device='cpu',  # Changed from device=0 to device='cpu'
    project='runs/train',
    name='cs2_model',
    patience=50,
    save=True,
    plots=True
)

print("Training complete!")
print(f"Best model saved to: runs/train/cs2_model/weights/best.pt")