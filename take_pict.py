import cv2

# 0 is usually the built-in webcam; 1 or 2 is typically the USB webcam
cam_index = int(input("Choose 0 for internal webcam or 1 for USB webcam and press Enter: "))
cam = cv2.VideoCapture(cam_index)

if not cam.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'S' to save and 'Q' to quit")

while True:
    ret, frame = cam.read()
    if not ret:
        break

    cv2.imshow('Webcam Feed', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite(f'captured_photo_{cam_index}.jpg', frame)
        print("Photo saved!")
    elif key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()