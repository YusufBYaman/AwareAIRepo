import cv2

# Görüntüleri oku ve çevir
img = cv2.imread('image.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Bütünsel matris boyutlarını (shape) karşılaştıralım
print("Orijinal Dizi Boyutu:", img.shape) 
print("Gri Dizi Boyutu:", gray.shape)

# Y=100, X=50 koordinatındaki tek bir pikselin dizisine bakalım
print("Orijinal Piksel (1000, 500):", img[1000, 500]) # Çıktı örneği: [45 102 210]
print("Gri Piksel (1000, 500):", gray[1000, 500])     # Çıktı örneği: 127