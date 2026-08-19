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
    #* framei bgr den hsv ye çevirir

    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 100])
    #*siyah bir renk olmadığı için tüm değerler serbest bırakılmış parlaklık değeri dışında herhangi bir sınırlama bulunmuyor, onu da 60 a sabitledik 

    mask = cv.inRange(hsv_frame, lower_black, upper_black)
    #! koşula uyan pikselleri beyaz, uymayanları siyah yapan bir maske oluşturur

    kernel = np.ones((5, 5), np.uint8)
    mask = cv.erode(mask, kernel, iterations=1)
    mask = cv.dilate(mask, kernel, iterations=1)

    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #! maske üzerindeki beyaz lekelerin etrafından çizgi çeker

    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 1500: #* piksel alanı 1500 ve üzeriyse
            x, y, w, h = cv.boundingRect(cnt) #! şekilsiz nesneyi kapsayacak en küçük dikdörtgeni hesaplar
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) #* hesaplanan dikdörtgeni oluşturur ve yeşile boyar

            center_x = x + w // 2
            center_y = y + h // 2
            cv.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
            #* dikdörtgenin tam merkezini hesaplayıp oraya içi dolu bir daire çizer

            cv.putText(frame, "Siyah Nesne", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv.imshow("Nesne Takibi", frame)
    cv.imshow("Siyah filtresi (maske)", mask)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()