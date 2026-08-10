import cv2
import torch
import time  # FPS hesaplamak için eklendi

model_path = "best.pt"

# DÜZELTME 1: try-except bloğu doğru şekilde kuruldu.
try:
    print("Özel model yükleniyor...")
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=False)
except Exception as e:
    print(f"Özel model yüklenirken hata oluştu veya dosya bulunamadı: {e}")
    print("Varsayılan 'yolov5s.pt' modeli yükleniyor...")
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Güven eşiği (Confidence Threshold)
model.conf = 0.5

# Kamera akışını başlatma
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera açılmadı.")
    exit()

print("YOLOv5 Nesne Algılama Başlatıldı. Çıkmak için 'q' tuşuna basın.")

# FPS hesabı için önceki zamanı tutacağımız değişken
prev_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kare alınamadı. Çıkılıyor...")
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (640, 640))
    
    # Model tahmini
    results = model(frame)

    # Tespit edilen nesneleri Pandas Dataframe olarak alıyoruz
    detections = results.pandas().xyxy[0]

    # Her bir tespit için döngü oluşturuyoruz
    for index, row in detections.iterrows():
        # Koordinatları alıyoruz (x_min, y_min, x_max, y_max)
        x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
        
        confidence = row['confidence']
        class_id = int(row['class'])
        name = row['name'] # Sınıfın metin karşılığı

        if confidence > 0.5:
            # Kutucuğu çiz (Sol üst ve sağ alt köşeler)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Etiketi ve güven skorunu yazdır
            label = f"{name} {confidence:.2f}"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # ---- FPS HESAPLAMA VE YAZDIRMA ----
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    # FPS metnini oluştur (Tam sayıya yuvarlayarak)
    fps_text = f"FPS: {int(fps)}"
    
    # Sağ üst köşeye yazdır (Genişlik 640 olduğu için x=500, y=40 uygun olacaktır)
    cv2.putText(frame, fps_text, (500, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    # -----------------------------------

    cv2.imshow("YOLOv5 Nesne Tespiti", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()