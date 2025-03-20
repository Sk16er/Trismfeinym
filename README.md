# Trismfeinym: Real-Time Object Detection using YOLO and OpenCV
# [TRISMFEINYM](https://github.com/Sk16er/Trismfeinym)
# ![image](https://github.com/user-attachments/assets/daeeefa2-edd8-4ebe-914e-89d06f370894)


Welcome to **Trismfeinym**! This project implements real-time object detection using the YOLO (You Only Look Once) model with OpenCV and Flask. Achieve high accuracy for various object detection tasks using state-of-the-art YOLO technology.

## 🚀 Features
- Real-time object detection with YOLO
- High accuracy with the latest YOLO model
- Efficient video frame processing using OpenCV
- Web-based UI using Flask
- Customizable detection classes

---

## 🛠️ Installation
Follow these steps to set up the project on your local machine:

### Prerequisites
Make sure you have Python 3.9 or above installed.

### Step 1: Clone the Repository
```bash
git clone https://github.com/Sk16er/Trismfeinym.git
cd Trismfeinym
```

### Step 2: Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Download YOLO Model
Ensure you have the YOLOv8 model from Ultralytics. You can download it using:
```bash
pip install ultralytics
```

---

## 🚦 Usage

### Run the Application
```bash
python app.py
```

### Access the App
Navigate to `http://localhost:5000` in your browser.

### Upload and Detect
- Upload an image or provide a video feed.
- Perform real-time object detection.
- Visualize detected objects with bounding boxes and labels.

---

## ⚙️ Configuration
You can adjust parameters like model type, confidence threshold, and object classes by modifying `config.py`.

Example Configuration:
```python
MODEL_PATH = 'yolov8n.pt'  # Path to YOLO model
CONFIDENCE_THRESHOLD = 0.5
```

---

## 🧪 Testing
You can run tests to ensure everything is working correctly:
```bash
pytest
```

---

## 🛎️ Troubleshooting
- Ensure your camera is accessible and drivers are installed.
- Verify all dependencies are installed using `pip freeze`.
- If the model isn’t loading, confirm the path in `config.py`.
- to install the commands here is the commands.
  ``` python
  pip install Flask opencv-python-headless torch ultralytics


---

## 📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## 🙌 Acknowledgements
- [YOLO by Ultralytics](https://github.com/ultralytics/ultralytics)
- [OpenCV](https://opencv.org/)
- Flask for the web application

---

## 📧 Contact
For any inquiries or issues, please open an issue on the GitHub repo or contact me at [shushankpawar664@gmail.com].

Happy detecting! 🕵️‍♂️

