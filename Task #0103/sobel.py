import cv2

img = cv2.imread("cv.jpg")
img = cv2.resize(img, (600, 800))

sobelx = cv2.Sobel(img,cv2.CV_64F, 1, 0, ksize=5)

cv2.imshow("Sobel X", sobelx)

sobely = cv2.Sobel(img,cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow("Sobel Y", sobely)

sobel = cv2.Sobel(img,cv2.CV_64F, 1, 1, ksize=5)

cv2.imshow("Sobel", sobel)


cv2.waitKey(0)
cv2.destroyAllWindows()
