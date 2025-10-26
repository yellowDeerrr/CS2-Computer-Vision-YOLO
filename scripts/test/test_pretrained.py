# import cv2
# import numpy as np
# from ultralytics import YOLO

# # Load YOLOv10 model
# model = YOLO('weights/yolov10n.pt')

# # Path to the video file
# video_path = 'test_video.mp4'
# cap = cv2.VideoCapture(video_path)

# while cap.isOpened():
# 	ret, frame = cap.read()
# 	if not ret:
# 		break

# 	# Perform object detection
# 	results = model(frame)

# 	# Draw bounding boxes
# 	for result in results:
# 		boxes = result['boxes']
# 		for box in boxes:
# 			x1, y1, x2, y2 = box['coords']
# 			label = box['label']
# 			confidence = box['confidence']
# 			cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
# 			cv2.putText(frame, f'{label} {confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# 	# Display the frame
# 	cv2.imshow('YOLOv10 Object Detection', frame)
# 	if cv2.waitKey(1) & 0xFF == ord('q'):
# 		break

# cap.release()
# cv2.destroyAllWindows()


# from ultralytics import YOLO

# # Load a pre-trained YOLOv10n model
# model = YOLO("runs/train/cs2_model5/weights/best.pt")

# # Perform object detection on an image
# results = model("dataset/test/images/semi-auto-Counter-Strike 2_1713641310.032938.png")

# # Display the results
# results[0].show()



# from ultralytics import YOLO

# print("Loading YOLOv10n model...")
# model = YOLO('weights/yolov10n.pt')

# # Test on entire test folder
# print("\nRunning predictions on test set...")

# results = model.predict(
# 	# source='dataset/test/images/13.jpg',
# 	source='test.png',
# 	conf=0.25,
# 	save=True,
# 	project='runs/detect',
# 	name='python_test',
# 	exist_ok=True
# )

# print(f"\n✅ Detection complete!")
# print(f"📁 Images with detections saved to: runs/detect/python_test/")

# # Summary
# total_images = len(results)
# total_detections = sum(len(r.boxes) for r in results)
# print(f"\n📊 Summary:")
# print(f"   Images processed: {total_images}")
# print(f"   Total detections: {total_detections}")

# # Show detections for each image
# for i, result in enumerate(results):
# 	if len(result.boxes) > 0:
# 		print(f"\n   Image {i+1}:")
# 		for box in result.boxes:
# 			cls = int(box.cls[0])
# 			conf = float(box.conf[0])
# 			class_name = model.names[cls]
# 			print(f"      - {class_name}: {conf:.2%}")