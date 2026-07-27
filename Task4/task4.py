#Resmin belirli bir kısmını sarı renkli bir çerçeveyle kare veya dikdörtgen içine alın. Bu alanın içini doldurun.

import cv2 as cv

img = cv.imread('image.png')

if img is not None:

    x1, y1 = 800, 500
    x2, y2 = 2300, 2000

    color= (0, 0, 255)  

    cv.rectangle(img, (x1, y1), (x2, y2), color, -1)

    cv.imshow('Image with Rectangle', img)

    cv.waitKey(0)
    cv.destroyAllWindows()

    cv.imwrite('modified_image.png', img)

else:
    print("Resim yüklenemedi.")