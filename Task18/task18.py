#YOLOv4 modeli ile insan tespiti uygulaması yapın ve confidence (güven) değerlerini değiştirerek sonuçlar üzerindeki etkileri inceleyin.

import os
import urllib.request
import cv2 as cv
import numpy as np

def nothing(x):
    pass

cfg_path = "yolov4.cfg"
weigths_path = "yolov4.weights"

# Model dosyaları indirme bağlantıları (GitHub'a .weights yüklenmediği için)
weights_url = "https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights"
cfg_url = "https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4.cfg"

# Config dosyası yerelde yoksa otomatik indir
if not os.path.exists(cfg_path):
    print("yolov4.cfg bulunamadı, indiriliyor...")
    urllib.request.urlretrieve(cfg_url, cfg_path)
    print("yolov4.cfg indirildi.")

# Weights dosyası yerelde yoksa otomatik indir
if not os.path.exists(weigths_path):
    print(f"yolov4.weights dosyası bulunamadı. Otomatik olarak indiriliyor...\nIndirme Linki: {weights_url}")
    urllib.request.urlretrieve(weights_url, weigths_path)
    print("yolov4.weights indirmesi tamamlandı.")

net = cv.dnn.readNet(weigths_path, cfg_path)

layer_names = net.getLayerNames()
try:
    output_layers = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]
except:
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

img = cv.imread('image1.jpg')
height, width = img.shape[:2]

print("Yapay zeka fotoğrafı analiz ediyor, lütfen bekleyin...")
blob = cv.dnn.blobFromImage(img, 1/255.0, (832, 832), swapRB=True, crop=False)
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

        if class_id == 0 and confidence > 0.0:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x - w/2)
            y = int(center_y - h/2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

print("Analiz tamamlandı! Arayüz açılıyor...")

window_name = 'YOLOv4 Insan Tespiti'
trackbar_name = 'Guven %'

cv.namedWindow(window_name)
cv.createTrackbar(trackbar_name, window_name, 50, 100, nothing)

while True:
    if cv.getWindowProperty(window_name, cv.WND_PROP_VISIBLE) < 1:
        break

    display_img = img.copy()

    trackbar_val = cv.getTrackbarPos(trackbar_name, window_name)
    if trackbar_val == -1:
        break

    conf_threshold = trackbar_val / 100.0

    indexes = cv.dnn.NMSBoxes(boxes, confidences, conf_threshold, 0.4)

    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            conf = confidences[i]

            cv.rectangle(display_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            label = f"Insan : %{int(conf*100)}"
            (label_width, label_height), _ = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.6, 2)
            cv.rectangle(display_img, (x, y - label_height - 10), (x + label_width, y), (0, 255, 0), cv.FILLED)

            cv.putText(display_img, label, (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    cv.imshow(window_name, display_img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()