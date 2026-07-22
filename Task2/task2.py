import cv2 as cv

img = cv.imread('image.png')

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray Image', gray_img)
cv.waitKey(0)
cv.destroyAllWindows()
