#OpenCV kullanarak bilgisayarınızdaki kameraya erişin ve görüntüyü bir pencere üzerinde gösterin.

import cv2 as cv

cap = cv.VideoCapture(0)
#* 0 parametresi varsayılan kamerayı temsil eder

if not cap.isOpened():
    print("Hata: Kamera açılamadı!")
    exit()

print("Kamera açıldı. Çıkmak için klavyeden 'q' tuşuna basın.")

while True:
    ret, frame = cap.read()
    #* ret, true false değerini alır, frame ise okunan fotoğrafın numpy matrisidir.
    frame = cv.flip(frame, 1)
    #aynalama

    if not ret:
        print("Hata: Kameradan görüntü alınamadı!")
        break

    cv.imshow('Canli Kamera Baglantisi', frame)
    #görüntüyü gösterir

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    #* basılan tuşun q olup olmadığını kontrol eder, ekran güncellenmesi için 1ms süre tanır ve 0xFF ile klavye tuş kodlarının fazla bit üretebilme ihtimaline karşı maskeleme yapar


cap.release()
#kamerayı bırakır
cv.destroyAllWindows()
#tüm cv2 pencerelerini kapatır