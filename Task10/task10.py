import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü gri tonlamalı oku
img = cv.imread('image.jpg', 0)

# İkili (binary) görüntüye çevir
_, thresh_img = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# 5x5 boyutunda kernel matrisi
kernel = np.ones((5,5), np.uint8)

# Morfolojik işlemler
erosion_result = cv.erode(thresh_img, kernel, iterations=1)
dilation_result = cv.dilate(thresh_img, kernel, iterations=1)
opening_result = cv.morphologyEx(thresh_img, cv.MORPH_OPEN, kernel)

# Görselleştirme
plt.figure(figsize=(18, 12))

plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(thresh_img, cmap='gray')
plt.title('Eşikleme Sonucu')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(erosion_result, cmap='gray')
plt.title('Erozyon Sonucu')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(dilation_result, cmap='gray')
plt.title('Dilatasyon Sonucu')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(opening_result, cmap='gray')
plt.title('Açma İşlemi Sonucu')
plt.axis('off')
plt.subplots_adjust(hspace=0.3)
plt.tight_layout()
plt.show() 
