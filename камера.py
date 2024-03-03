import cv2
cap = cv2.VideoCapture(0)
while True:
    cv2.imshow('frame', "frame")
    # Этот шаг должен быть, в противном случае изображение не может быть отображено
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 # Когда все завершено, отпустите захват
cap.release()
cv2.destroyAllWindows()
print("ты лох хуйли закрывае")
