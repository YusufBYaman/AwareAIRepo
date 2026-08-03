#OpenCV kütüphanesindeki Watershed fonksiyonunu kullanarak segmentasyon yapın.

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('image.png')

img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


gray_img = cv.medianBlur(gray_img, 7)

ret, thres = cv.threshold(gray_img, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
#* ret otsu thresholdun hesapladığı ideal eşikleme değerini alır, thres ise siyah beyaza çevrilmiş bir fotoğraf

kernel = np.ones((3, 3), np.uint8) # kernel piksel piksel tarayan araç
opening = cv.morphologyEx(thres, cv.MORPH_OPEN, kernel, iterations=2) #* önce törpüler sonra şişirir

sure_bg = cv.dilate(opening, kernel, iterations=3)
#* dilate beyaz kısımları şişirir

dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
#! Nesnenin arkaplana(siyaha) olan uzaklık haritası, örneğin bir karenin kenarları 1 birim uzaktadır gri olur merkeze gittikçe beyaz parlaklığı artar

ret, sure_fg = cv.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0) 
#! sadece maksimum mesafenin yarısından yukarıysa siyah altındaysa beyaz yap.

sure_fg = np.uint8(sure_fg) #* dist_transformdan sonra değerler ondalıklı sayıya dönüştü bunu 8 bite çeviriyoruz (0-255)
unknown = cv.subtract(sure_bg, sure_fg) #* arkaplandan, önplanı çıkarıyoruz ve emin olunmayan bir kısım kalıyor elimizde

ret, markers = cv.connectedComponents(sure_fg) #* ekranda ayrı olan beyaz nesneleri işaretler. ret, kaç farklı nesne var onun sayısı (arkaplanı da ekler +1)
#* markers ise 0 dan başlayarak her nesneye atadığı id numarlarını taşıyan matrisdir (0 ı arkaplana verir)
markers = markers + 1 #* sıfır olan alanları dolduracağı için arkaplanı korumaya aldık
markers[unknown == 255] = 0 #* belirgin olmayan her yeri sıfır yap

markers = cv.watershed(img, markers) #* hem orjinal resme hem de filtrelediğimiz kısma bakarak çizgileri çizer

img_rgb[markers == -1] = [255, 0, 0] #* çizgileri kırmızıya boyar

titles = ['Original Image', 'Thresholded Image', 'Morphological Opening', 'Sure Background', 
          'Distance Transform', 'Sure Foreground', 'Unknown Region', 'Watershed Result']


images = [cv.cvtColor(img, cv.COLOR_BGR2RGB), thres, opening, sure_bg, 
          dist_transform, sure_fg, unknown, img_rgb]

plt.figure(figsize=(15, 10))
for i in range(8):
    plt.subplot(2, 4, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.tight_layout()
plt.show()