#CNN mimarisi nedir araştırın. 

CNN (Evrişimli Sinir Ağı) Nedir?
CNN, özellikle görüntü ve video verilerini analiz etmek, nesneleri tanımak ve sınıflandırmak için tasarlanmış oldukça güçlü bir derin öğrenme (deep learning) algoritmasıdır. İnsan beynindeki görsel korteksin çalışma prensibinden ilham alarak geliştirilmiştir.

Klasik yapay sinir ağları (ANN), bir görüntüyü tek boyutlu uzun bir sayı dizisine dönüştürerek okur. Bu durum pikseller arasındaki uzamsal ilişkilerin (hangi pikselin hangisinin yanında veya üstünde olduğunun) kaybolmasına yol açar. CNN ise görüntünün iki boyutlu yapısını korur. Bu sayede bir kedi fotoğrafındaki "kulak", "göz" veya "kuyruk" gibi formları bölgesel olarak çok daha başarılı bir şekilde tespit eder.

CNN Mimarisinin Temel Katmanları
Bir CNN modeli arka arkaya dizilmiş belirli görevleri olan katmanlardan (layers) oluşur. İşlem sürecini şu 4 ana katman yönetir:

1. Evrişim Katmanı (Convolutional Layer): Mimarinin kalbidir. Orijinal görüntünün üzerinde Filtre (Kernel) adı verilen küçük matrisler piksel piksel gezdirilir. Bu filtreler görüntüdeki kenarları, dikey/yatay çizgileri, köşeleri ve dokuları tespit etmek (feature extraction) için kullanılır. Bir dedektifin büyüteçle resmin üzerinde adım adım gezinerek ipuçları aramasına benzer.

2. Aktivasyon Katmanı (Genellikle ReLU): Evrişim işleminden çıkan matematiksel sonuçlara doğrusal olmayan bir yapı katar. En çok kullanılan aktivasyon fonksiyonu olan ReLU (Rectified Linear Unit), elde edilen değerlerdeki negatif sayıları sıfıra eşitler. Bu, modelin öğrenme hızını ve performansını inanılmaz derecede artırır.

3. Havuzlama/Ortaklama Katmanı (Pooling Layer): Görüntünün özniteliklerini kaybetmeden boyutunu (genişlik ve yüksekliğini) küçültür. En yaygın olanı Max Pooling'dir; örneğin 2x2'lik bir piksel grubuna bakar ve sadece en yüksek değeri (en belirgin olan özelliği) bir sonraki adıma taşır. İşlem yükünü azaltır ve modelin ezber yapmasını (overfitting) engeller.

4. Tam Bağlantılı Katman (Fully Connected / Dense Layer): Önceki katmanlardan elde edilen özellik haritaları (matrisler) düzleştirilerek (flattening) tek boyutlu uzun bir listeye dönüştürülür. Bu katman, çıkarılan tüm özellikleri değerlendirip nihai bir oylama yapar ve sınıflandırma sonucunu üretir (Örneğin: "Bu görüntü %92 ihtimalle bir araba").

Evrişim (Convolution), Aktivasyon ve Havuzlama (Pooling) adımları, ağın derinliğine göre arka arkaya defalarca kez tekrarlanabilir. İlk katmanlar basit çizgileri öğrenirken, derinlere indikçe model yüzleri, arabaları veya karmaşık nesneleri tanımayı öğrenir.