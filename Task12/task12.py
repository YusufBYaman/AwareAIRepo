#OpenCV kullanarak bilgisayarınızdaki kameraya erişin ve görüntüyü bir pencere üzerinde gösterin.

import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Hata: Kamera açılamadı!")
    exit()

print("Kamera açıldı. Çıkmak için klavyeden 'q' tuşuna basın.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Hata: Kameradan görüntü alınamadı!")
        break

    cv.imshow('Canli Kamera Baglantisi', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()