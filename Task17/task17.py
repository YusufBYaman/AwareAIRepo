import cv2 as cv
import numpy as np
import os
import urllib.request

cfg_path = "yolov3-face.cfg"
weights_path = "yolov3-face.weights"

if not os.path.exists(weights_path):
    print("Ağırlık dosyası (yolov3-face.weights) bulunamadı. İndiriliyor...")
    url = "https://files.kde.org/digikam/facesengine/dnnface/yolov3-wider_16000.weights"
    urllib.request.urlretrieve(url, weights_path)
    print("İndirme tamamlandı.")

net = cv.dnn.readNetFromDarknet(cfg_path, weights_path)

layer_names = net.getLayerNames() #! ağdaki tüm katmanları alıyoruz 
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()] 
#! sonuç döndürenleri eleyiyoruz / flatten ile pythonun okuyabileceği hale getiriyoruz

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Kamera açılamadı.")
    exit()

print("YOLOv3 Yüz Algılama Başlatıldı. Çıkmak için 'q' tuşuna basın.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kare alınamadı. Çıkılıyor...")
        break

    height, width, channels = frame.shape

    blob = cv.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    #* Binary Large Object
    #* pikseller 0-255 arasında değer alır, doğru çalışması için 0-1 aralığında olması gerkir.
    #* swapRB, bgr den rgb ye çeviri kırmızı ile mavinin yerini değiştirir.

    net.setInput(blob)
    #* hazırladığımız blobu ağa veriyoruz

    outs = net.forward(output_layers) 
    #* hesaplamaları yapar ve 3 farklı katmana göre değer bulur.

    boxes = []
    confidences = []
    class_ids = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv.dnn.NMSBoxes(boxes, confidences, score_threshold=0.5, nms_threshold=0.4)
    #* Güven skoru %50 altı olanları eler ve kalan iç içe geçmiş kutulara bakar eğer %40 oranında örtüşüyorsa bunların aynı yüz olduğunu anlar.
    #* Güven skoru en yüksek olanı asıl kutu seçer ve diğerlerini siler.

    if len(indexes) > 0: #! Asıl kutuların bulunduğu indeks listesini kontrol ediyoruz
        for i in np.array(indexes).flatten(): #! hepsini okunabilir bir listeye çevirip kutu boyutunu, sınıf idsini ve güven skorunu alıyoruz
            x, y, w, h = boxes[i]
            label = str(class_ids[i])
            confidence = confidences[i]

            #! Bu bilgilerle kutuları oluşturuyoruz
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.putText(frame, f"{label} {confidence:.2f}", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv.imshow("YOLOv3 Yüz Tespiti", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows() 