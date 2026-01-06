from ultralytics import YOLO

if __name__ == '__main__':
    # Load pretrained model
    print("Loading YOLOv10n model...")
    model = YOLO('weights/yolov10n.pt')
    
    # Train on your CS2 dataset
    print("Starting training on GPU...")
    results = model.train(
        data='dataset/data.yaml',
        epochs=100,
        imgsz=640,
        batch=16,
        device=0,
        project='runs/train',
        name='cs2_model',
        patience=50,
        save=True,
        plots=True
    )
    
    print("Training complete!")
    print(f"Best model saved to: runs/train/cs2_model/weights/best.pt")