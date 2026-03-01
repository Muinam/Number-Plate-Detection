import cv2
import pytesseract
import pandas as pd
from ultralytics import YOLO
from datetime import datetime

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Load YOLO model
model = YOLO('best.pt')

# Webcam input
cap = cv2.VideoCapture('License Plate Detection Test.mp4')  # 0 is default webcam

# Optional: Save video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) or 30  # default to 30 if can't read

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_with_inference.mp4', fourcc, fps, (width, height))

detected_plates = []
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_count += 1

    # Speed optimization (skip odd frames)
    if frame_count % 2 != 0:
        cv2.imshow("Webcam Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        out.write(frame)
        continue

    results = model(frame)

    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()
        for box in boxes:
            x1, y1, x2, y2 = map(int, box)
            plate_img = frame[y1:y2, x1:x2]

            ocr_text = pytesseract.image_to_string(plate_img, config='--psm 7')
            plate_number = ''.join(char for char in ocr_text if char.isalnum())

            if plate_number:
                detected_plates.append({
                    'plate_number': plate_number,
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, plate_number, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Show live frame with boxes and text
    cv2.imshow("Webcam Feed", frame)

    # Save frame to video file (optional)
    out.write(frame)

    # Exit condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
out.release()
cv2.destroyAllWindows()

# Save to Excel
df = pd.DataFrame(detected_plates)
df.to_excel('detected_number_plates.xlsx', index=False)

print("✅ Live detection complete. Excel and video saved.")
