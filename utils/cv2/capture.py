import cv2
from utils.cv2.detector import Detector
from utils.fps_counter import FPSCounter
from utils.cv2.cv2 import Cv2Utils

def cv2_process():

    detector = Detector()
    fps_counter = FPSCounter()
    cam = Cv2Utils()

    while cam.isOpened():
        ret, frame = cam.read()
        if not ret:
            print("⚠️ Failed to read frame or video ended.")
            break

        results = detector.detect(frame)
        print("\n\n\n##############################\n\n\n\n\n\n\n\n\n")
        
        annotated_frame = results[0].plot()
        print("Annoted: " + str(annotated_frame))
        print("\n\n\n----------------\n\n\n")
        
        detection_counts = detector.get_detection_counts(results)
        print("Detection counts: " + str(detection_counts))
        # Update FPS
        fps_counter.update()
        
        # Draw overlay (FPS and detection counts)
        annotated_frame = cam.display_overlay(
            annotated_frame, 
            fps_counter.get_fps(), 
            detection_counts
        )

        cv2.imshow("Counter Strike 2", annotated_frame)

        # Quit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

