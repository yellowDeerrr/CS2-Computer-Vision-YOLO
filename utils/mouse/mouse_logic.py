from config import FRAME_WIDTH, FRAME_HEIGHT
import pyautogui
import time

# AUTO_SHOOT = False  # rather apply auto shoot or press button to shoot
# SHOOT_HOTKEY = 58  # 58 = CAPS-LOCK
# CHANGE_TEAM_HOTKEY = "ctrl+t"
# is_key_pressed = False  # to track shoot key state
shoot_conf = (0.8, 0.7)  # minimum required conf for detection to shoot (head, body)
# min_assist_dist = 300 # minimum required distance of crosshair to target for mouse move (assist)
# min_shoot_dist = 50 # minimum required distance of crosshair to target for mouse click (shoot)

def shootIfPossible(results):
    global is_key_pressed

    detections = results[0].boxes

    for box in detections:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        
        print(box.xyxy[0].tolist())

        x1, y1, x2, y2 = map(float, box.xyxy[0])  # top-left (x1,y1), bottom-right (x2,y2)

        if (cls_id == 1 or cls_id == 3) and conf >= shoot_conf[0]:
            print(f"Shooting at head with confidence {conf}")
            # Implement shooting logic here
        elif (cls_id == 0 or cls_id == 2) and conf >= shoot_conf[1]:
            print(f"Shooting at body with confidence {conf}")

        move_mouse_to_box(x1, y1, x2, y2)

def move_mouse_to_box(x1, y1, x2, y2):
    x_center = (x1 + x2) / 2
    y_center = (y1 + y2) / 2

    x_mouse = FRAME_WIDTH / 2
    y_mouse = FRAME_HEIGHT / 2
    
    
    # crosshair in 640x360
    # for example target in
    # 1) 200x300
    # 2) 720x400

    move_x = 0
    move_y = 0
    
    if x_center - x_mouse >= 5:
        move_x = -2
    elif x_center - x_mouse <= -5:
        move_x = 2

    if y_center - y_mouse >= 5:
        move_y = -2
    elif y_center - y_mouse <= -5:
        move_y = 2

    pyautogui.moveRel(int(move_x + x_mouse), int(move_y + y_mouse))
    time.sleep(0.01)  # small delay for smooth movement

    