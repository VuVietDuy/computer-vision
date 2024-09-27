import cv2

img = cv2.imread("image.jpg")
dest = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

b, g, r = cv2.split(img)

rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mimg = cv2.merge((b, g, r))

cv2.imshow("Merged", mimg)
cv2.imshow("HSV", dest)
cv2.imshow("Red", r)
cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("RGB", rgb_image)
cv2.imshow("Grayscale", gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()