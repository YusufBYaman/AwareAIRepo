#YOLOv4 modeli ile gerçek zamanlı kamera görüntülerinden insan tespiti yapın ve FPS değerini ekranın sağ üst köşesine yazdırın.

import os
import urllib.request
import cv2 as cv
import numpy as np
import time

cfg_path = "yolov4.cfg"
weights_path = "yolov4.weights"

# Model dosyaları indirme bağlantıları (GitHub'a .weights yüklenmediği için)
weights_url = "https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights"
cfg_url = "https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4.cfg"

if not os.path.exists(cfg_path):
    print("yolov4.cfg bulunamadı, indiriliyor...")
    urllib.request.urlretrieve(cfg_url, cfg_path)
    print("yolov4.cfg indirildi.")

if not os.path.exists(weights_path):
    print(f"yolov4.weights bulunamadı, indiriliyor...\nLink: {weights_url}")
    urllib.request.urlretrieve(weights_url, weights_path)
    print("yolov4.weights indirildi.")

# OpenCV readNet parametre sırası: (model/weights, config)
net = cv.dnn.readNet(weights_path, cfg_path)

layer_names = net.getLayerNames()
try:
    output_layers = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]
except:
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Hata: Kamera açılmadı!")
    exit()

prev_time = 0

print("YOLOv4 İnsan Tespiti başlatıldı... Çıkmak için 'q' tuşuna basın")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width = frame.shape[:2]

    current_time = time.time()
    fps = 1 / (current_time - prev_time) if (current_time - prev_time) > 0 else 0
    prev_time = current_time

    blob = cv.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers) 

    boxes = []
    confidences = []
    class_ids = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if class_id == 0 and confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            conf = confidences[i]

            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.putText(frame, f"Insan: %{int(conf*100)}", (x, max(y - 10, 15)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    fps_text = f"FPS: {int(fps)}"
    (text_width, text_height), _ = cv.getTextSize(fps_text, cv.FONT_HERSHEY_SIMPLEX, 1, 2)

    x_fps = width - text_width - 20
    y_fps = text_height + 20

    # Gölge ve FPS metni
    cv.putText(frame, fps_text, (x_fps + 2, y_fps + 2), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv.putText(frame, fps_text, (x_fps, y_fps), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv.imshow('YOLOv4 Canli Analiz', frame)

    if cv.getWindowProperty('YOLOv4 Canli Analiz', cv.WND_PROP_VISIBLE) < 1:
        break

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()