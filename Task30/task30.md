# TEKNİK RAPOR: Vision Transformers (ViT) Çalışma Prensibi ve Mimarisi

**Tarih:** 4 Ağustos 2026  
**Konu:** Vision Transformers (ViT) Sisteminin İncelenmesi ve Çalışma Dinamikleri

---

## 1. Yönetici Özeti
Vision Transformer (ViT), doğal dil işleme (NLP) alanında devrim yaratan Transformer mimarisinin, bilgisayarlı görü (computer vision) görevlerine doğrudan ve başarıyla uygulandığı yenilikçi bir modeldir. Geleneksel Evrişimli Sinir Ağlarının (CNN) aksine, ViT görselleri piksellerden oluşan bir matris olarak değil, ardışık "yamalar" (patches) dizisi olarak işler. Bu rapor, ViT'in temel çalışma prensibini, mimari bileşenlerini ve geleneksel sistemlere göre avantaj/dezavantajlarını teknik bir perspektifle ele almaktadır.

---

## 2. Giriş ve Arka Plan
Bilgisayarlı görü alanında uzun yıllar boyunca Evrişimli Sinir Ağları (CNN) standart olarak kabul edilmiştir. CNN'ler, görüntüdeki bölgesel özellikleri (kenarlar, dokular) öğrenmek için "tümevarımsal ön yargılara" (inductive bias) sahiptir. 2020 yılında Google araştırmacıları (Dosovitskiy ve ark.) tarafından tanıtılan **Vision Transformer**, görüntü işlemeyi kelime işlemeye (NLP) benzer bir dizi (sequence) problemi olarak ele almış ve büyük veri setlerinde CNN'leri geride bırakan veya onlarla yarışan sonuçlar elde etmiştir.

---

## 3. ViT Çalışma Prensibi ve Adımları

ViT mimarisi, bir görseli analiz ederken sıralı, matematiksel ve dönüştürücü birkaç temel adımdan geçer. Sistemin baştan sona veri akışı şu şekildedir:

### 3.1. Yamalara Bölme (Patch Extraction)
Transformer modelleri yapıları gereği 1 boyutlu (1D) dizilerle (sequence) çalışır. 2 boyutlu (2D) bir görseli bu modele besleyebilmek için görsel, sabit boyutlu alt ızgaralara (yamalara) bölünür.
* Örneğin, **224x224** piksel boyutunda bir görsel, **16x16** boyutlarında yamalara ayrılır.
* Bu işlem sonucunda (224 / 16) x (224 / 16) = **196** adet yama elde edilir. Tıpkı NLP'deki bir cümledeki kelimeler gibi, bu yamalar görselin "kelimelerini" oluşturur.

### 3.2. Doğrusal İzdüşüm (Linear Projection / Patch Embedding)
Elde edilen her bir 16x16 yama, düzleştirilerek (flatten) tek boyutlu bir vektör haline getirilir. Daha sonra, modelin anlayabileceği sabit bir vektör boyutuna (örneğin 768 boyutlu bir uzaya) getirilmek üzere öğrenilebilir bir doğrusal dönüşümden (linear projection) geçirilir. Bu işleme **Patch Embedding** denir.

### 3.3. Sınıflandırma Jetonu Ekleme (Learnable [CLS] Token)
NLP alanındaki BERT modelinden ilham alınarak, yama dizisinin en başına özel bir sınıflandırma jetonu (token) eklenir. Bu token, Transformer ağının tüm katmanlarından geçerken diğer tüm yamalardan bilgi toplar. Ağın en sonunda, sadece bu token'ın taşıdığı bilgi kullanılarak görselin nihai sınıflandırması (Örn: "Bu bir kedi") yapılır.

### 3.4. Konum Kodlaması (Positional Encoding)
Transformer mimarisi, yamaları aynı anda (paralel) işler; yani hangi yamanın görselin neresinden (sağ üst, sol alt vb.) geldiğini doğal olarak bilemez. Bunu çözmek için her bir yama vektörüne, o yamanın görseldeki konumunu belirten matematiksel bir **Konum Kodlaması** eklenir. 

### 3.5. Transformer Kodlayıcı (Transformer Encoder)
Dizi haline gelmiş ve konum bilgisi eklenmiş yamalar, üst üste binmiş çoklu Transformer Encoder katmanlarına sokulur. Bu katmanların kalbinde **Çok Başlı Öz-Dikkat (Multi-Head Self-Attention)** mekanizması yatar:
* **Öz-Dikkat Mekanizması:** Model, görselin bir yamasını incelerken, aynı anda diğer tüm yamalarla olan ilişkisini hesaplar. Örneğin, model bir "köpek kulağı" yamasına bakarken, eş zamanlı olarak "köpek burnu" ve "tüyler" yamalarına "dikkat kesilir". Bu sayede görselin bağlamı tümüyle (global olarak) kavranır.
* Encoder ayrıca beslemeli sinir ağları (MLP/Feed Forward) ve katman normalizasyonu (Layer Norm) içerir.

### 3.6. Sınıflandırma Başlığı (Classification Head)
Son Encoder katmanından çıkan veriler arasından, en başta eklediğimiz [CLS] token'ının çıktısı alınır. Bu çıktı, çok katmanlı bir algılayıcıdan (MLP) geçirilerek görselin hangi sınıfa ait olduğuna dair bir olasılık dağılımına dönüştürülür.

---

## 4. CNN ve ViT Karşılaştırması

| Özellik | CNN (Evrişimli Sinir Ağları) | ViT (Vision Transformers) |
| :--- | :--- | :--- |
| **Görüş Alanı (Receptive Field)** | Lokaldir. Katmanlar ilerledikçe büyür. Başlangıçta sadece yakın pikselleri görür. | Globaldir. Öz-dikkat mekanizması sayesinde daha ilk katmanda bile tüm görselin bağlamını algılar. |
| **Ön Yargı (Inductive Bias)** | Yüksektir. Kaydırma bağımsızlığı (translation invariance) ve yerel yapıların varlığını varsayar. | Düşüktür. Görselin doğasına dair baştan bir varsayım yapmaz, kuralları sıfırdan öğrenir. |
| **Veri İhtiyacı** | Düşük/Orta ölçekli verilerle bile kolayca eğitilebilir. | Kendi kurallarını sıfırdan bulduğu için **çok büyük** veri setlerine (örn. JFT-300M, ImageNet-21k) ihtiyaç duyar. |

---

## 5. Değerlendirme ve Sonuç

Vision Transformers (ViT), pikselleri yerel filtrelere hapsetmek yerine tüm görseli "dikkat" (attention) mekanizmalarıyla değerlendirerek bilgisayarlı görüde bir paradigma değişimi yaratmıştır.

**Avantajları:**
* Yeterli veri ile eğitildiğinde sınıflandırma görevlerinde state-of-the-art (en son teknoloji) performansı gösterir.
* Global bağlamı anlama yeteneği çok yüksektir, görselin farklı uçlarındaki nesneler arasındaki ilişkiyi ilk katmandan itibaren kurabilir.

**Dezavantajları:**
* Hesaplama maliyeti oldukça yüksektir (görsel boyutu veya yama sayısı arttıkça maliyet karesel olarak artar).
* Küçük ölçekli veri setlerinde CNN'lerin gerisinde kalır, çünkü öğrenmeyi yönlendirecek mimari bir ön yargıya (bias) sahip değildir.

Özetle; veri ve işlem gücü problemleri çözüldüğünde ViT mimarisi, esnekliği ve kapasitesi sayesinde geleceğin otonom sistemlerinden tıbbi görüntülemeye kadar pek çok alanda standart araç olma potansiyelini taşımaktadır.