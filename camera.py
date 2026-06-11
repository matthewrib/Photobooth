from cv2 import VideoCapture, imshow, imwrite, waitKey, destroyAllWindows, resize
import numpy as np
import time

cam = VideoCapture(0)

num_images = 4
cooldown_seconds = 2

canvas_h, canvas_w = 1800, 600 
canvas = np.ones((canvas_h, canvas_w, 3), dtype=np.uint8) * 255

slot_x = 20
slot_y = 20
slot_w = 600
slot_h = 450
slot_gap = 20

captured_frames = []

for i in range(num_images):
    if i > 0:
        print(f"Waiting {cooldown_seconds} seconds before photo {i + 1}...")
        time.sleep(cooldown_seconds)

    ret, frame = cam.read()
    if not ret:
        print(f"Failed to capture image {i + 1}")
        continue

    captured_frames.append(frame.copy())
    imshow("Captured", frame)
    imwrite(f"captured_image_{i + 1}.jpg", frame)
    waitKey(300)

if not captured_frames:
    print("No images captured.")
else:
    for i, img in enumerate(captured_frames):
        resized_img = resize(img, (slot_w, slot_h))
        y1 = slot_y + i * (slot_h + slot_gap)
        y2 = y1 + slot_h
        x1 = slot_x
        x2 = x1 + slot_w
        canvas[y1:y2, x1:x2] = resized_img

    imshow("Canvas with Images", canvas)
    imwrite("canvas_with_images.jpg", canvas)
    waitKey(0)

destroyAllWindows()

cam.release()