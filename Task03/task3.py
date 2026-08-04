import cv2 as cv

img = cv.imread('image.png')

if img is not None:
    resized = cv.resize(img, (800, 600))
    cv.imwrite('resized_image.png', resized)

    cropped = img[500:2000, 800:2300]
    cv.imwrite('cropped_image.png', cropped) 

    cv.waitKey(0)
    cv.destroyAllWindows() 
else: 
    print("Resim yüklenemedi.")