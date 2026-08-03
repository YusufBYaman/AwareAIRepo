#Kare içine alınan bu alanı önce griye dönüştürün, ardından bu alanı bulanıklaştırın. Bu işlemlerin gerçek hayatta nerelerde kullanıldığını araştırın.

import cv2 as cv

img = cv.imread('image.png')

if img is not None:
    x1, y1 = 900, 550
    x2, y2 = 2300, 1400

    roi = img[y1:y2, x1:x2]

    hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv_roi)
    blurred_v = cv.GaussianBlur(v, (25, 25), 0)

    merged_hsv = cv.merge([h, s, blurred_v])

    final_roi = cv.cvtColor(merged_hsv, cv.COLOR_HSV2BGR)

    img[y1:y2, x1:x2] = final_roi

    cv.imshow('Modified Image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    cv.imwrite('modified_image.png', img)
    print("Resim başarıyla kaydedildi.")


else:
    print("Resim yüklenemedi.")