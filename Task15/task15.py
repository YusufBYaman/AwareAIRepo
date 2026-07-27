#Video üzerinde renk tespiti yapan bir uygulama geliştirin.

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Hata: Kamera açılamadı.")
    exit()

print("Kamera Açıldı. Canlı renk takibi yapılıyor. Çıkmak için 'q' tuşuna basın.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Hata: Görüntü alınamadı.")
        break

    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])

    mask = cv.inRange(hsv_frame, lower_blue, upper_blue)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv.contourArea(cnt)

        if area > 500:
            x, y, w, h = cv.boundingRect(cnt)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.putText(frame, "Mavi Nesne", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv.imshow("Canlı Renk Takibi", frame)
    cv.imshow("Uygulanan Maske", mask)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()