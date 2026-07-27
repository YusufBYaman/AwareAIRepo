#HSV nedir araştırın. Ardından HSV kullanarak bir trackbar yardımıyla videodaki görüntünün HSV değerlerini değiştirin.

import cv2 as cv
import numpy as np

def nothing(x):
    pass

cap = cv.VideoCapture(0)

cv.namedWindow("HSV Ayarları")

cv.createTrackbar("H min, ", "HSV Ayarları", 0, 180, nothing)
cv.createTrackbar("S min, ", "HSV Ayarları", 0, 255, nothing)
cv.createTrackbar("V min, ", "HSV Ayarları", 0, 255, nothing)

cv.createTrackbar("H max, ", "HSV Ayarları", 180, 180, nothing)
cv.createTrackbar("S max, ", "HSV Ayarları", 255, 255, nothing)
cv.createTrackbar("V max, ", "HSV Ayarları", 255, 255, nothing)


print("Kamera açıldı. Çıkmak için 'q' tuşuna basın.")


while True:
    ret, frame = cap.read()

    if not ret:
        print("Hata: Görüntü alınamadı.")
        break

    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    h_min = cv.getTrackbarPos("H min, ", "HSV Ayarları")
    s_min = cv.getTrackbarPos("S min, ", "HSV Ayarları")
    v_min = cv.getTrackbarPos("V min, ", "HSV Ayarları")

    h_max = cv.getTrackbarPos("H max, ", "HSV Ayarları")
    s_max = cv.getTrackbarPos("S max, ", "HSV Ayarları")
    v_max = cv.getTrackbarPos("V max, ", "HSV Ayarları")

    lower_bound = np.array([h_min, s_min, v_min])
    upper_bound = np.array([h_max, s_max, v_max])

    mask = cv.inRange(hsv_frame, lower_bound, upper_bound)

    result = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("Orijinal Kamera", frame)
    cv.imshow("Maske (Siyah-Beyaz)", mask)
    cv.imshow("Filtrelenmiş Sonuç", result)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()