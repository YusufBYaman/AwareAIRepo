#Thresholding nedir, hangi alanlarda kullanılır araştırın ve bir yaprak resmi üzerinde bu işlemi gerçekleştirin.

import cv2 as cv 
import matplotlib.pyplot as plt

img = cv.imread('image.png')

if img is None:
    print("Resim yüklenemedi.")
else:

    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Convert to grayscale for thresholding

    # Global Thresholding
    ret, th1 = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)
    #! 127 den yukarısını 255 e altını 0 a yuvarlar

    # Otsu's Thresholding
    ret2, th2 = cv.threshold(gray_img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    #! otsu kendisi otomatik olarak bulacağı için 0 yazarız

    # Adaptive Thresholding (Mean)
    th3 = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
    #! her piksel için etrafındaki 11x11 lik alana bakarak ortalama hesaplar, 2 ise c sabitidir (ortalama - c)

    # Adaptive Thresholding (Gaussian)
    th4 = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    #! her piksel için etrafındakş 11x11 lik alana bakarak ortalama hesaplar ama merkezdeki piksellere daha çok ağırlık verir

    titles = ['Original Image', 'Global Thresholding (v=127)', "Otsu's Thresholding", 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [gray_img, th1, th2, th3, th4]

    plt.figure(figsize=(15, 10))
    for i in range(5):
        plt.subplot(2, 3, i + 1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    plt.tight_layout()
    plt.show()
