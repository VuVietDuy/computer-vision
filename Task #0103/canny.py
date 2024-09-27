import cv2

img = cv2.imread("cv.jpg")

img = cv2.resize(img, (600, 800))

canny_img = cv2.Canny(img, 100, 200)

cv2.imshow("CANNY IMG", canny_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
