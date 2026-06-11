from cv2 import VideoCapture, imshow, imwrite, waitKey, destroyAllWindows, resize
import numpy as np
import time

cam = VideoCapture(0)

num_images = 4
cooldown_seconds = 2

slot_x = 20
slot_y = 20
slot_w = 350
slot_h = int(slot_w * 9 / 16)
slot_gap = 20

canvas_w = slot_x + slot_w + 20
canvas_h = slot_y + (num_images * slot_h) + ((num_images - 1) * slot_gap) + 20
canvas = np.ones((canvas_h, canvas_w, 3), dtype=np.uint8) * 255


def center_crop_to_aspect(img, target_w, target_h):
    target_ratio = target_w / target_h
    h, w = img.shape[:2]
    current_ratio = w / h

    if current_ratio > target_ratio:
        new_w = int(h * target_ratio)
        x1 = (w - new_w) // 2
        return img[:, x1:x1 + new_w]

    new_h = int(w / target_ratio)
    y1 = (h - new_h) // 2
    return img[y1:y1 + new_h, :]

captured_frames = []

for i in range(num_images):
    ret, frame = cam.read()
    if not ret:
        print(f"Failed to capture image {i + 1}")
        continue

    while cooldown_seconds > 0:
        print(f"{cooldown_seconds} seconds before photo {i + 1}...")
        time.sleep(1)
        cooldown_seconds -= 1

    captured_frames.append(frame.copy())
    imshow("Captured", frame)
    imwrite(f"captured_image_{i + 1}.jpg", frame)
    cooldown_seconds = 2
    waitKey(300)

if not captured_frames:
    print("No images captured.")
else:
    for i, img in enumerate(captured_frames):
        cropped_img = center_crop_to_aspect(img, slot_w, slot_h)
        resized_img = resize(cropped_img, (slot_w, slot_h))
        y1 = slot_y + i * (slot_h + slot_gap)
        y2 = y1 + slot_h
        x1 = slot_x
        x2 = x1 + slot_w

        if y2 > canvas_h or x2 > canvas_w:
            print(f"Skipping image {i + 1}: slot is out of canvas bounds")
            continue

        canvas[y1:y2, x1:x2] = resized_img

    imshow("Canvas with Images", canvas)
    imwrite("canvas_with_images.jpg", canvas)
    waitKey(0)

destroyAllWindows()

cam.release()