#OpenCV’nin flip metodunu deneyin ve ne işe yaradığını açıklayın.

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('image.jpg')
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

flip_horizontal = cv.flip(img_rgb, 1)
#! Yatay çevirme yapar (aynalama)
flip_vertical = cv.flip(img_rgb, 0)
#! Dikey çevirme yapar
flip_both = cv.flip(img_rgb, -1)
#! hem yatay hem dikey çevirme yapar

plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.imshow(img_rgb)
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(flip_horizontal)
plt.title('Yatay Çevirme (flipCode = 1)')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(flip_vertical)
plt.title('Dikey Çevirme (flipCode = 0)')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(flip_both)
plt.title('Hem Yatay Hem Dikey (flipCode = -1)')
plt.axis('off')

plt.tight_layout()
plt.show()