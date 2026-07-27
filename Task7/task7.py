#OpenCV kütüphanesindeki Watershed fonksiyonunu kullanarak segmentasyon yapın.

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('image.png')
assert img is not None, "Resim yüklenemedi."

img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


gray_img = cv.medianBlur(gray_img, 7)

ret, thres = cv.threshold(gray_img, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)


kernel = np.ones((3, 3), np.uint8)
opening = cv.morphologyEx(thres, cv.MORPH_OPEN, kernel, iterations=2)

sure_bg = cv.dilate(opening, kernel, iterations=3)

dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)

ret, sure_fg = cv.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)

sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg, sure_fg)

ret, markers = cv.connectedComponents(sure_fg)

markers = markers + 1
markers[unknown == 255] = 0

markers = cv.watershed(img, markers)

img_rgb[markers == -1] = [255, 0, 0]

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