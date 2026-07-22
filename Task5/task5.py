import cv2 as cv

img = cv.imread('image.png')

if img is not None:
    x1, y1 = 900, 550
    x2, y2 = 2300, 1400

    roi = img[y1:y2, x1:x2]

    gray_roi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)

    blurred_roi = cv.GaussianBlur(gray_roi, (25, 25), 0)

    last_roi = cv.cvtColor(blurred_roi, cv.COLOR_GRAY2BGR)

    img[y1:y2, x1:x2] = last_roi

    cv.imshow('Modified Image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    cv.imwrite('modified_image.png', img)
    print("Resim başarıyla kaydedildi.")


else:
    print("Resim yüklenemedi.")