# Multispektral ve Hiperspektral Kameralar: Çalışma Mantığı ve Teknik Detaylar

Multispektral ve hiperspektral kameralar, insan gözünün algılayamadığı ışık dalga boylarını yakalayarak nesnelerin fiziksel ve kimyasal özellikleri hakkında derinlemesine bilgi sunan gelişmiş görüntüleme teknolojileridir. Her ikisi de elektromanyetik spektrumu kullanarak çalışır, ancak veriyi işleme detayları ve kapasiteleri bakımından birbirlerinden ayrılırlar.

Bu kameraların gücü, fiziğin temel kurallarından biri olan **Elektromanyetik Spektrum** ve **Spektral İmza (Spectral Signature)** kavramlarına dayanır. Doğadaki her nesne ışığı farklı dalga boylarında emer veya yansıtır. Geleneksel kameralar bu imzanın sadece Kırmızı, Yeşil ve Mavi kısmını görürken, bu özel kameralar imzanın görünmeyen kritik kısımlarını da okur.

---

## 1. Multispektral Kameralar ve Çalışma Mantığı

Multispektral görüntüleme, ışığı belirli, geniş ve birbirinden ayrık dalga boyu bantlarına bölerek çalışır. Genellikle 3 ile 15 arasında değişen sayıda bağımsız bant yakalarlar.

* **Donanımsal Çalışma Prensibi:** Sensörlerin önünde, ışığın sadece belirli dalga boylarının geçmesine izin veren Girişim Filtreleri (Interference Filters) bulunur. Bazı sistemlerde tek lens ve prizmalar, dronlarda ise yan yana dizilmiş farklı lens-sensör çiftleri kullanılır.
* **Kritik Bantlar:** Klasik RGB bantlarına ek olarak Kırmızı Kenar (Red-Edge, 700-740 nm) ve Yakın Kızılötesi (NIR, 750-1000 nm) bantları yoğun olarak kullanılır.
* **Veri Çıktısı:** Her bant için ayrı bir 2 boyutlu görüntü (katman) oluşturulur. Bu katmanlar üst üste bindirilerek analiz yapılır.
* **Matematiksel Analiz (NDVI):** Sağlıklı bitkiler kırmızı ışığı emer, NIR ışığını ise yansıtır. Bu iki bandın matematiksel oranı bize bitki sağlığını gösteren Normalize Edilmiş Fark Bitki İndeksini (NDVI) verir:

> **NDVI = (NIR - Kırmızı) / (NIR + Kırmızı)**

---

## 2. Hiperspektral Kameralar ve Çalışma Mantığı

Hiperspektral görüntüleme, multispektral teknolojisinin çok daha gelişmiş versiyonudur. Ayrık ve geniş bantlar yerine, birbirine bitişik ve çok dar (örn. 1-2 nanometre genişliğinde) yüzlerce dalga boyunu aynı anda yakalar.

* **Donanımsal Çalışma Prensibi:** Işık lense girdikten sonra bir Kırınım Ağı (Diffraction Grating) veya özel prizmalara çarpar. Bu elemanlar ışığı kesintisiz bir spektruma böler.
* **Tarama Yöntemleri (Pushbroom):** Genellikle "Satır Tarama" adı verilen bir yöntem kullanırlar. Kamera veya nesne hareket halindeyken, sensör dünyayı satır satır süpürür ve her bir piksel satırı için kırılan ışık kaydedilir.
* **Sinyal-Gürültü Oranı (SNR) Problemi:** Işık çok dar dilimlere ayrıldığı için sensördeki her bir piksele çok az foton düşer. Bu sebeple yüksek kaliteli merceklere, güçlü ışık kaynaklarına ve termal gürültüyü önleyecek soğutma sistemlerine ihtiyaç duyarlar.
* **Veri Çıktısı (Veri Küpü):** Elde edilen veri 3 boyutludur. X ve Y eksenleri nesnenin fiziksel koordinatlarını, Z ekseni ise o pikseldeki yüzlerce dalga boyu grafiğini (spektral imzayı) temsil eder.

---

## İki Teknoloji Arasındaki Temel Farklar

| Özellik | Multispektral Kameralar | Hiperspektral Kameralar |
| :--- | :--- | :--- |
| **Bant Sayısı** | Genellikle 3 ila 15 bant arası. | Yüzlerce veya binlerce bant. |
| **Bant Aralığı** | Geniş ve birbirinden ayrık (boşluklu). | Çok dar ve kesintisiz (bitişik). |
| **Spektral İmza** | Nesnelerin genel kategorilerini belirler (Örn: "Bitki"). | Nesnelerin tam türünü ve içeriğini belirler (Örn: "Susuz bitki"). |
| **Veri Boyutu** | Düşük / Orta (İşlenmesi ve depolanması kolaydır). | Çok Yüksek (Büyük veri depolama ve güçlü işlemci gerektirir). |
| **Maliyet** | Görece uygun fiyatlıdır, dronlara kolayca entegre edilir. | Oldukça pahalı ve donanımsal olarak karmaşık sistemlerdir. |

---

## Endüstriyel ve Bilimsel Kullanım Örnekleri

| Teknoloji | İleri Düzey Uygulama Örnekleri |
| :--- | :--- |
| **Multispektral** | **Kıyı Batimetrisi:** Su altı derinliğini ve yosun dağılımını uydulardan haritalama.<br>**Ormancılık:** Orman yangınlarında küllerin altındaki aktif közleri termal/IR bant ile tespit etme. |
| **Hiperspektral** | **Tıbbi Görüntüleme:** Açık beyin ameliyatlarında sağlıklı doku ile tümörlü doku arasındaki kimyasal farkı gerçek zamanlı gösterme.<br>**Atık Ayrıştırma:** Bantta hızla akan farklı tür siyah plastikleri (PET, PVC, PE) polimer yapılarına göre ayırt etme. |



Kısaca,

Multispektral Kameralar: Işığı 3 ila 15 civarında geniş ve birbirinden ayrı banda böler. Nesnelerin genel kategorisini (Örn: "Bu bir bitkidir") belirler. Daha uygun fiyatlıdır ve verisini işlemek kolaydır.

Hiperspektral Kameralar: Işığı birbirine bitişik yüzlerce veya binlerce dar banda böler. Nesnelerin kimyasal içeriğini ve tam türünü (Örn: "Bu bitki susuz kalmış" veya "Bu hücre kanserli") parmak izi gibi tespit eder. Çok pahalıdır ve işlenmesi zor, devasa boyutta veri üretir.