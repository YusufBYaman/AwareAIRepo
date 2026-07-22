import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
img = cv2.resize(img, (1920, 1080)) 

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)

gray_float = np.float32(gray)
dst = cv2.cornerHarris(gray_float, 2, 3, 0.04)
dst = cv2.dilate(dst, None)

img_corners = img_rgb.copy()
img_corners[dst > 0.01 * dst.max()] = [255, 0, 0]

plt.figure(figsize=(15, 5)) 

plt.subplot(1, 3, 1) 
plt.imshow(img_rgb)
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 3, 2) 
plt.imshow(edges, cmap='gray') 
plt.title('Kenar Tespiti (Canny)')
plt.axis('off')

plt.subplot(1, 3, 3) 
plt.imshow(img_corners)
plt.title('Köşe Tespiti (Harris)')
plt.axis('off')

plt.tight_layout()
plt.show()