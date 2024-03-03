import cv2

# Открыть камеру
cap = cv2.VideoCapture(0)

# Проверить, открылась ли камера
if not cap.isOpened():
    print("Camera not opened")
    exit()

# Захватить кадр
ret, frame = cap.read()

# Проверить, захвачен ли кадр
if not ret:
    print("Failed to capture frame")
    exit()

# Показать кадр
cv2.imshow("Camera capture", frame)

# Ожидать нажатия клавиши для закрытия окна
cv2.waitKey(0)

# Закрыть камеру и выйти
cap.release()
cv2.destroyAllWindows()
