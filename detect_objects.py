from ultralytics import YOLO
import cv2
import json
import os

model = YOLO('yolov8n.pt')
image_path = "sample.jpeg"
image = cv2.imread(image_path)
results = model(image)
output_data = []

for i, detection in enumerate(results[0].boxes):
    object_name = results[0].names[int(detection.cls)]
    bbox = detection.xyxy[0].tolist()
    sub_object_name = "Helmet" if object_name == "person" else "Tire" if object_name == "car" else "Unknown"
    sub_bbox = [bbox[0] + 10, bbox[1] + 10, bbox[2] - 10, bbox[3] - 10]
    
    entry = {
        "object": object_name,
        "id": i + 1,
        "bbox": [round(coord, 2) for coord in bbox],
        "subobject": {
            "object": sub_object_name,
            "id": i + 1,
            "bbox": [round(coord, 2) for coord in sub_bbox]
        }
    }
    output_data.append(entry)

    x1, y1, x2, y2 = map(int, sub_bbox)
    sub_object_image = image[y1:y2, x1:x2]
    sub_object_folder = "sub_objects"
    os.makedirs(sub_object_folder, exist_ok=True)
    sub_object_image_path = os.path.join(sub_object_folder, f"{sub_object_name}_{i + 1}.jpg")
    cv2.imwrite(sub_object_image_path, sub_object_image)

output_file = "output.json"
with open(output_file, "w") as f:
    json.dump(output_data, f, indent=4)

scale_percent = 26
width = int(results[0].orig_img.shape[1] * scale_percent / 100)
height = int(results[0].orig_img.shape[0] * scale_percent / 100)
dim = (width, height)
annotated_frame = results[0].plot()
resized_frame = cv2.resize(annotated_frame, dim, interpolation=cv2.INTER_AREA)

cv2.imshow("Detections", resized_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
