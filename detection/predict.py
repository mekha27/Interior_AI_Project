from ultralytics import YOLO
import cv2
from collections import defaultdict

model = YOLO("yolov8n.pt")

def detect_objects(image_path):

    results = model(image_path)[0]

    img = cv2.imread(image_path)

    object_count = defaultdict(int)
    confidence_map = defaultdict(float)

    for box in results.boxes:

        cls_id = int(box.cls[0])
        name = model.names[cls_id]
        conf = float(box.conf[0])

        object_count[name] += 1

        # Keep maximum confidence per object
        confidence_map[name] = max(
            confidence_map[name],
            round(conf, 2)
        )

        # Bounding box visualization
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
        cv2.putText(img, name, (x1,y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    output_path = "output_detection.jpg"
    cv2.imwrite(output_path, img)

    return {
        "message": "Detection completed",
        "detected_objects": dict(object_count),
        "total_objects": sum(object_count.values()),
        "confidence_scores": dict(confidence_map),
        "visualization_image": output_path
    }