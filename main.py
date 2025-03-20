import cv2
from ultralytics import YOLO

def main():
    # Load the YOLOv8 model
    model = YOLO('yolov8n.pt')  # nano modal

    # Open a connection to the webcam (0 is the default camera) in case you have many change that to 1,2 
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break

        # Perform object detection
        results = model(frame)

        
        annotated_frame = results[0].plot()

        
        cv2.imshow('YOLOv8 Object Detection', annotated_frame)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()