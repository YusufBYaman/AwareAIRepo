import cv2
import torch
import time

model_path = "best_fp16.engine"

try:
    print("TensorRT destekli özel model yükleniyor...")
    # TensorRT motoru yüklenirken ekran kartı (device='0') zorunludur
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=False, device='0')
except Exception as e:
    print(f"Model yüklenirken hata oluştu: {e}")
    print("Varsayılan 'yolov5s.pt' modeli yükleniyor...")
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Güven eşiği
model.conf = 0.5

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera açılamadı.")
    exit()

print("YOLOv5 TensorRT Nesne Algılama Başlatıldı. Çıkmak için 'q' tuşuna basın.")

prev_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kare alınamadı. Çıkılıyor...")
        break

    # Kamerayı ayna görüntüsüne çevirme
    frame = cv2.flip(frame, 1)
    
    # DÜZELTME: cv2.resize KULLANMIYORUZ! 
    # YOLOv5 arka planda oranları bozmadan kendisi 640'a uyduracaktır.

    # Model tahmini (OpenCV BGR renk formatı verir, YOLOv5 AutoShape bunu otomatik anlar ve RGB'ye çevirir)
    results = model(frame)

    # Tespitleri DataFrame olarak al
    detections = results.pandas().xyxy[0]

    for index, row in detections.iterrows():
        x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
        
        confidence = row['confidence']
        class_id = int(row['class'])
        name = row['name'] 

        if confidence > 0.5:
            # Kutucuğu çiz
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Etiketi ve güven skorunu yazdır
            label = f"{name} {confidence:.2f}"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # FPS Hesaplama
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    # FPS metnini yazdır
    fps_text = f"FPS: {int(fps)}"
    # Çözünürlük kameranın orijinal çözünürlüğünde kaldığı için dinamik FPS konumu belirleyelim
    h, w, _ = frame.shape
    # cv2.putText(frame, fps_text, (w - 150, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("YOLOv5 TensorRT Canli Tespit", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()