import cv2 as cv

img = cv.imread('image.png')

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

if img is not None: 

    cv.imshow('Gray Image', gray_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    cv.imwrite('gray_image.png', gray_img)
    print("Resim başarıyla kaydedildi.")

else: 
    print("Resim yüklenemedi.")