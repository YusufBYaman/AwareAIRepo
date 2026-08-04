# YOLOv5 Sigara ve Telefon Tespiti (Smoke & Phone Detection) Model Raporu

Bu proje, YOLOv5 mimarisi kullanılarak görüntüler üzerinde gerçek zamanlı "Sigara" (Cigarette) ve "Telefon" (Phone) tespiti yapmak amacıyla eğitilmiştir. Bu dökümanda modelin eğitim çıktıları, başarı metrikleri ve grafiklerinin yorumlaması yer almaktadır.

---

## 1. Temel Performans Metrikleri ve Anlamları

Modelin ne kadar iyi öğrendiğini anlamak için aşağıdaki temel kavramları bilmek gerekir:

* **Precision (Hassasiyet - P):** Modelin "Bu bir telefondur" dediği nesnelerin yüzde kaçı *gerçekten* telefondur? Yüksek hassasiyet, modelin **yanlış alarm (False Positive)** verme oranının düşük olduğunu gösterir.
* **Recall (Duyarlılık - R):** Gerçekte var olan telefonların yüzde kaçını model bulabildi? Yüksek duyarlılık, modelin nesneleri **gözden kaçırma (False Negative)** oranının düşük olduğunu gösterir.
* **mAP@.50 (Mean Average Precision):** %50 örtüşme (IoU) eşiğinde modelin genel doğruluk performansıdır. Nesne tespiti modellerinde en çok referans alınan temel başarı kriteridir.
* **F1 Score (F1 Skoru):** Precision ve Recall değerlerinin harmonik ortalamasıdır. Bir modelin hem yanlış alarmları önlemesi hem de nesneleri gözden kaçırmaması arasındaki **en iyi dengeyi** ifade eder. Maksimum değeri 1.0'dır.

---

## 2. Model Eğitim Sonuçlarının Yorumlanması

Eğitim sonucunda elde edilen verilere göre model performansı şu şekildedir:

| Sınıf (Class) | Görüntü Sayısı | Nesne Sayısı | Precision (P) | Recall (R) | mAP@.50 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Tümü (all)** | 631 | 988 | **0.868** | **0.793** | **0.842** |
| **Telefon (phone)** | 631 | 737 | 0.913 | 0.869 | 0.908 |
| **Sigara (cigarette)**| 631 | 251 | 0.822 | 0.717 | 0.776 |

### Sonuçların Analizi:
1. **Genel Başarı (mAP: %84.2):** Model, genel nesne tespitinde oldukça yüksek bir performans göstermiştir.
2. **Telefon Tespiti:** Telefon sınıfında mAP değeri **%90.8** gibi çok başarılı bir seviyededir. Model telefonu kolayca ayırt edebilmekte ve çok az hata yapmaktadır.
3. **Sigara Tespiti:** Sigara sınıfında mAP değeri **%77.6**'dır. Sigara, piksel olarak küçük ve el/yüz ile sık sık örtüşen (occlusion) bir nesne olduğu için tespit edilmesi telefona kıyasla daha zordur. Ancak %82.2 Hassasiyet (Precision) oranı, modelin "sigara" dediği şeylerin çoğunlukla gerçekten sigara olduğunu kanıtlamaktadır.

---

## 3. Grafikler ve Çıktıların İncelenmesi

Eğitim klasörü (`runs/train/smoke_phone_model`) içinde yer alan grafiklerin yorumlanması aşağıdadır:

### A. F1 Eğrisi (`F1_curve.png`)
Bu grafik, Güven Eşiği (Confidence Threshold) ile F1 Skoru arasındaki ilişkiyi gösterir.
* Eğrinin tepe (pik) yaptığı nokta, modelin **en verimli çalıştığı** güven eşiğidir.
* *Öneri:* Canlı test (inference) yaparken kod içerisindeki `model.conf` değerini (şu an 0.5 olarak ayarlı), F1 eğrisinin zirve yaptığı değere ayarlamak (örn: 0.45 - 0.55 arası) modelin dengesini maksimize edecektir.

### B. Hata Matrisi (`confusion_matrix.png`)
Modelin hangi nesneyi neyle karıştırdığını gösterir.
* **Köşegen (Diagonal) Kareler:** Koyu renkli olmaları beklenir. Modelin doğru tahmin ettiği (True Positive) durumları gösterir.
* **Arka Plan (Background) Hataları:** "Background FN" sütunu, modelin orada bir nesne olmasına rağmen bulamadığı (gözden kaçırdığı) durumları ifade eder. Sigara sınıfı için bu değerin telefon sınıfına göre biraz daha yüksek olması muhtemeldir.

### C. Eğitim Sonuçları (`results.png`)
Bu grafik setinde 100 epoch boyunca kayıp (loss) değerlerinin düşüşü ve mAP değerlerinin yükselişi izlenir.
* **Box Loss & Objectness Loss:** Eğitim boyunca (train ve val grafikleri) istikrarlı bir şekilde aşağı inmiş olmalıdır.
* *Analiz:* Eğer val (doğrulama) grafikleri bir noktadan sonra düşmeyi bırakıp tekrar yükselmeye (U harfi çizmeye) başladıysa **Overfitting (Aşırı Öğrenme)** yaşanmış demektir. Neyse ki `best.pt` ağırlığı, algoritma tarafından overfitting yaşanmadan önceki en iyi anda otomatik olarak kaydedilmiştir.

---

## 4. Gelecek Geliştirmeler (İyileştirme Önerileri)

Sigara sınıfındaki (%77.6) doğruluk oranını telefon seviyesine (%90+) çıkarmak için yapılabilecekler:
* **Veri Artırma (Data Augmentation):** Sigaranın elde, ağızda ve farklı ışık koşullarında olduğu daha fazla fotoğraf eklenebilir.
* **Kırpma ve Yakınlaştırma:** Küçük nesneler için veri setine yakın çekim / crop yapılmış görseller dahil edilebilir.
* **Arkaplan (Negative) Görselleri:** Modelin kalem, parmak veya beyaz objeleri sigara sanmaması için içinde insan olan ama sigara *olmayan* negatif görseller veri setine eklenebilir.