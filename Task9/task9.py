import cv2

img = cv2.imread('image.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("Orijinal Dizi Boyutu:", img.shape) 
print("Gri Dizi Boyutu:", gray.shape)

print("Orijinal Piksel (1000, 500):", img[1000, 500]) 
print("Gri Piksel (1000, 500):", gray[1000, 500])