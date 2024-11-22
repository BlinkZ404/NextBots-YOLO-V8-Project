import serial
import cv2
import logging
import time
import os
from ultralytics import YOLO

# Suppress unnecessary logging
cv2.imshow = lambda *args: None
os.environ["QT_XCB_GL_INTEGRATION"] = "none"
for name in logging.root.manager.loggerDict:
    t_logger = logging.getLogger(name)
    t_logger.setLevel(logging.CRITICAL)
    
# Initialize Arduino
port = '/dev/ttyACM0'
arduino = serial.Serial(port, 9600, timeout=1)

def send_command(command):
    """Send a command to Arduino."""
    arduino.write(command.encode())
    print(f"Sent: {command}")
    
# Movement Functions
def handle_triangle():
    send_command('w')
    time.sleep(0.5)
    send_command('d')
    time.sleep(0.30)
    send_command('w')
    time.sleep(0.5)
    send_command('t')
    print("Triangle path completed.")

def handle_square():
    send_command('w')
    time.sleep(0.5)
    send_command('d')
    time.sleep(0.34)
    send_command('w')
    time.sleep(0.5)
    send_command('d')
    time.sleep(0.34)
    send_command('w')
    time.sleep(0.5)
    send_command('d')
    time.sleep(0.34)
    send_command('w')
    time.sleep(0.5)
    send_command('t')
    print("Square path completed.")
    
def handle_cycle():
    send_command('d')
    time.sleep(2)  # Move forward while simulating a circle
    send_command('a')
    time.sleep(2)
    send_command('t')
    print("Circle path completed.")

def handle_right_loop():
    send_command('w')
    time.sleep(0.5)
    send_command('d')
    time.sleep(0.35)
    send_command('w')
    time.sleep(0.3)
    send_command('d')
    time.sleep(0.35)
    send_command('w')
    time.sleep(0.5)
    send_command('t')
    print("Right loop path completed.")
    
def handle_left_loop():
    send_command('w')
    time.sleep(0.5)
    send_command('d')
    time.sleep(0.35)
    send_command('w')
    time.sleep(0.3)
    send_command('d')
    time.sleep(0.35)
    send_command('w')
    time.sleep(0.5)
    send_command('t')
    print("Left loop path completed.")

def handle_stop():
    send_command('t')
    print("Robot stopped.")
    
def handle_up():
    send_command('w')  # Move forward
    time.sleep(0.5)
    send_command('t')
    print("Moved forward.")

def handle_down():
    send_command('s')  # Move backward
    time.sleep(0.5)
    send_command('t')
    print("Moved backward.")
    
def handle_right():
    send_command('d')  # Rotate or move right
    time.sleep(0.30)
    send_command('t')
    print("Moved right.")

def handle_left():
    send_command('a')  # Rotate or move left
    time.sleep(0.30)
    send_command('t')
    print("Moved left.")
    
# YOLO Model Configuration
imageSize = 640
confidenceThreshold = 0.60
weightPath = '/home/serpent/Desktop/panzer/Result[B8E500]/weights/best.pt'
inputSource = cv2.VideoCapture(0)
model = YOLO(weightPath)
processing = False
last_command_time = 0
cooldown = 3

# Main Execution Loop
if __name__ == '__main__':
    try:
        while inputSource.isOpened():
            success, frame = inputSource.read()
            if success:
                current_time = time.time()  # Get the current time
                
                if not processing:  # Only proceed if not processing a command
                    results = model(source=frame, imgsz=imageSize, conf=confidenceThreshold, stream=False, show=False)
                    annotated_frame = results[0].plot()
                    cv2.imshow("Stream", annotated_frame)

                    for r in results:
                        if r.boxes.cls.numel() == 0:
                            print('No Detections!')
                            handle_stop()
                        else:
                            for i, cls in enumerate(r.boxes.cls):
                                class_names = r.names[int(cls)]
                                class_confidence = r.boxes.conf[i].item() * 100
                                print(f"Detected: {class_names} | Confidence: {class_confidence:.1f}%")
                                                                
                                # Handle each class with its corresponding function
                                if current_time - last_command_time >= cooldown:  # Check cooldown
                                    if class_names == "triangle":
                                        processing = True
                                        handle_triangle()
                                        processing = False
                                    elif class_names == "square":
                                        processing = True
                                        handle_square()
                                        processing = False
                                    elif class_names == "cycle":
                                        processing = True
                                        handle_cycle()
                                        processing = False
                                    elif class_names == "right_loop":
                                        processing = True
                                        handle_right_loop()
                                        processing = False
                                    elif class_names == "left_loop":
                                        processing = True
                                        handle_left_loop()
                                        processing = False
                                    elif class_names == "stop":
                                        processing = True
                                        handle_stop()
                                        processing = False
                                    elif class_names == "up":
                                        processing = True
                                        handle_up()
                                        processing = False
                                    elif class_names == "down":
                                        processing = True
                                        handle_down()
                                        processing = False
                                    elif class_names == "right":
                                        processing = True
                                        handle_right()
                                        processing = False
                                    elif class_names == "left":
                                        processing = True
                                        handle_left()
                                        processing = False
                                    
                                    # Update the last command timestamp
                                    last_command_time = current_time

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            else:
                break
    finally:
        arduino.close()
        inputSource.release()
        cv2.destroyAllWindows()
