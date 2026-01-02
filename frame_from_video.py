import cv2
import os

video_path = "4.mp4"
output_dir = "frames"

os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
frame_id = 0

def get_new_filename(path):
    """ถ้ามีไฟล์อยู่แล้ว จะสร้างชื่อใหม่อัตโนมัติ"""
    if not os.path.exists(path):
        return path

    base, ext = os.path.splitext(path)
    i = 1
    while True:
        new_path = f"{base}_{i}{ext}"
        if not os.path.exists(new_path):
            return new_path
        i += 1

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_id % 5 == 0:
        filename = f"{output_dir}/frame_{frame_id:05d}.jpg"
        filename = get_new_filename(filename)
        cv2.imwrite(filename, frame)

    frame_id += 1

cap.release()
print("Save finished!")
