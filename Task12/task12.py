import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Hata: Kamera açılamadı.")
    exit()

    print("Kamera açıldı. Çıkmak için 'q' tuşuna basın.")


while True:
    ret, frame = cap.read()

    if not ret:
        print("Hata: Görüntü alınamadı.")
        break

    cv.imshow('Canlı Kamera Bağlantısı', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()