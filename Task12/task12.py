import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Hata: Kamera açılamadı.")
    exit()

    print("Nesne takibi başladı. Çıkmak için 'q' tuşuna basın.")


while True:
    ret, frame = cap.read()

    if not ret:
        print("Hata: Görüntü alınamadı.")
        break

    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 60])

    mask = cv.inRange(hsv_frame, lower_black, upper_black)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv.erode(mask, kernel, iterations=1)
    mask = cv.dilate(mask, kernel, iterations=1)

    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 1500:
            x, y, w, h = cv.boundingRect(cnt)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            center_x = x + w // 2
            center_y = y + h // 2
            cv.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

            cv.putText(frame, "Siyah Nesne", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv.imshow("Nesne Takibi", frame)
    cv.imshow("Siyah filtresi (maske)", mask)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()