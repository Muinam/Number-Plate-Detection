📌 Project Overview

This project is a Real-Time Automatic License Plate Recognition (ALPR) System that detects vehicle number plates from video input and 
extracts the plate text using Optical Character Recognition (OCR).

The system uses a custom-trained YOLOv8 model for license plate detection and Tesseract OCR for text recognition. 
Detected plate numbers are displayed on the video feed and stored with timestamps in an Excel file for record-keeping and analysis.

🎯 Key Features

✅ Real-time license plate detection from video

✅ Custom YOLOv8 model (best.pt) for accurate object detection

✅ OCR-based alphanumeric text extraction

✅ Bounding box annotation on detected plates

✅ Timestamp logging for each detected plate

✅ Excel report generation (detected_number_plates.xlsx)

✅ Processed output video export (output_with_inference.mp4)

✅ Frame-skipping optimization for performance improvement


🛠️ Technologies Used

Python

OpenCV – Video processing & frame handling

YOLOv8 (Ultralytics) – Deep Learning object detection

Tesseract OCR – Text recognition

Pandas – Data storage & Excel export

Datetime – Timestamp generation


⚙️ How the System Works
1️⃣ Model Loading

The custom-trained YOLOv8 model (best.pt) is loaded.

Tesseract OCR path is configured for text extraction.

2️⃣ Video Input

Video file (License Plate Detection Test.mp4) is used as input.

Video properties (width, height, FPS) are captured.

Output video writer is initialized.

3️⃣ Frame Processing

Frames are read one by one.

Frame-skipping technique is applied (processes every 2nd frame) to improve speed.

4️⃣ License Plate Detection

YOLO model detects number plate regions.

Bounding box coordinates are extracted.

5️⃣ OCR Processing

Detected plate region is cropped.

Tesseract OCR extracts text using --psm 7 configuration.

Non-alphanumeric characters are removed.

Cleaned plate number is stored.

6️⃣ Annotation & Logging

Bounding boxes drawn on detected plates.

Plate number displayed on video frame.

Plate number + timestamp stored in list.

7️⃣ Output Generation

Annotated video saved as:

output_with_inference.mp4

All detected plates saved in Excel:

detected_number_plates.xlsx


🚀 Possible Applications

Smart Traffic Monitoring

Parking Management Systems

Toll Collection Systems

Law Enforcement Surveillance

Automated Vehicle Tracking
