from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Run detection
    results = model(frame)

    # Draw results
    annotated_frame = results[0].plot()

    cv2.imshow("Missile Detection System", annotated_frame)

    # Exit on Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()