# Snap-Scan: Object Detection with YOLOv8

This project demonstrates object detection using the YOLOv8 model. The program detects objects in an input image, identifies sub-objects (e.g., helmets for people, tires for cars, etc.), and saves the results, including cropped sub-object images and annotated visuals.

---

## Features

- Detect objects in an image using YOLOv8.
- Identify sub-objects for specific detected objects:
  - Helmet for "person"
  - Tire for "car"
  - "Unknown" for other objects
- Save annotated images with bounding boxes.
- Generate a JSON file containing object and sub-object details.
- Save cropped images of detected sub-objects.

---

## Folder Structure

ENV/
├── Include/
├── Lib/
├── Scripts/
├── share/
├── sub_objects/             # Cropped sub-object images are saved here
├── annotated_sample.jpg     # Annotated image with bounding boxes
├── detect_objects.py        # Main Python script for object detection
├── output.json              # JSON file with object and sub-object details
├── README.md                # Project documentation
├── sample.jpeg              # Input image for object detection
├── yolov8n.pt               # Pre-trained YOLOv8 model weights


---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd <repository_directory>

2. **Setup the Python Environment**
  ```bash
    python -m venv ENV
    source ENV/Scripts/activate  # On Windows
    source ENV/bin/activate      # On macOS/Linux
    pip install -r requirements.txt
  ```
3. **Place Input Image**
   Replace ```sample.jpeg``` with your input image.

## Usage

1. Run the Script
```bash
python detect_objects.py
```

2. Results
   a. Annotated Image: ```annotated_sample.jpg```
   b. JSON Output: ```output.json```
   c. Cropped Sub-Objects: Saved in the ```sub_objects/``` folder.

## Sample JSON Output
```json
[
    {
        "object": "person",
        "id": 1,
        "bbox": [50.34, 100.56, 200.45, 300.67],
        "subobject": {
            "object": "Helmet",
            "id": 1,
            "bbox": [60.34, 110.56, 190.45, 290.67]
        }
    }
]
```

## Notes
1. The yolov8n.pt model is pre-trained on the COCO dataset.
2. Sub-object detection is simulated and depends on predefined rules.
3. The JSON output includes bounding box coordinates for both objects and sub-objects.

## Acknowledgments
1. Ultralytics YOLO
2. COCO Dataset
