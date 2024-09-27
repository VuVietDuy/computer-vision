# Intensity Adjustment
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class Image:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv.imread(image_path)
    
    def resize(self, width, height ):
        resized_image = cv.resize(self.image, (width, height), interpolation=cv.INTER_AREA)
        self.image = resized_image
        self.display([{"name": "Resized Image", "image": resized_image}])

    
    def display(self, images):
        for i in images:
            cv.imshow(i["name"], i["image"])
        cv.waitKey(0)
        cv.destroyAllWindows()


    def intensity(self):
        img = cv.resize(self.image, None,  fx=0.2, fy=0.2, interpolation=cv.INTER_CUBIC)
        M = np.ones(img.shape, dtype='uint8') * 40
        print(M)

        brighter = cv.add(img, M)
        darker = cv.subtract(img, M)

        cv.imshow('Original Image', img)
        cv.imshow('Brighter Image', brighter)
        cv.imshow('Darker Image', darker)
        cv.waitKey(0)
        cv.destroyAllWindows()

    # intensity()

    def threshold(self):
        img = cv.imread(self.image_path, cv.IMREAD_GRAYSCALE)
        img = cv.resize(img, None, fx=0.2, fy=0.2, interpolation=cv.INTER_CUBIC)
        ret,thresh = cv.threshold(img,127,255,cv.THRESH_BINARY)
        cv.imshow("Threshold", thresh)
        cv.waitKey(0)
        cv.destroyAllWindows()

    # threshold()

    # Histogram Equalization

    def histogram_equalization(self):
        img = cv.imread(self.image_path, cv.IMREAD_GRAYSCALE)
        img = cv.resize(img, None, fx=0.2, fy=0.2, interpolation=cv.INTER_CUBIC)
        equ = cv.equalizeHist(img)
        hist, bins = np.histogram(equ.flatten(), 256, [0, 256])
        cdf = hist.cumsum()
        cdf_normalize = cdf * float(hist.max() / cdf.max())
        plt.plot(cdf_normalize, color='b')
        plt.hist(equ.flatten(), color='b')

        cv.imshow('Original Image', img)
        cv.imshow('Equalized Image', equ)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def sobel(self):
        img = cv.imread(self.image_path, cv.IMREAD_GRAYSCALE)
        img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
        sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
        sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
        res = cv.add(sobelx, sobely)
        self.display([{"name": "Original img", "image": img},{"name": "Sobel X", "image": res}])
    
    def laplacian(self):
        img = cv.imread(self.image_path, cv.IMREAD_GRAYSCALE)
        laplacian = cv.Laplacian(img, cv.CV_64F)
        self.display([{"name": "Original img", "image": img},{"name": "Laplacian", "image": laplacian}])

    def average(self): # Box blur
        img = cv.resize(self.image, None, fx=0.3, fy=0.3, interpolation=cv.INTER_CUBIC)
        avg = cv.blur(img, (5, 5))
        self.display([{"name": "Original img", "image": img},{"name": "Average", "image": avg}])
        
    def gaussian(self):
        img = cv.resize(self.image, None, fx=0.3, fy=0.3, interpolation=cv.INTER_CUBIC)
        gaussian = cv.GaussianBlur(img, (5, 5), 0)
        self.display([{"name": "Original img", "image": img},{"name": "Gaussian", "image": gaussian}])

    def median(self):
        img = cv.resize(self.image, None, fx=0.3, fy=0.3, interpolation=cv.INTER_CUBIC)
        median = cv.medianBlur(img, 5)
        self.display([{"name": "Original img", "image": img},{"name": "Median", "image": median}])
    
img = Image('cv.jpg')
img.histogram_equalization()

# img = cv.imread('guitar.jpg')
# fi = cv.resize(img, (300, 300), cv.INTER_AREA)
# se = cv.resize(fi, (300, 300), cv.INTER_CUBIC)
# th = cv.resize(fi, (300, 300), cv.INTER_LINEAR)
# cv.imshow("original", img)
# cv.imshow("AREA",fi)
# cv.imshow("CUBIC", se)
# cv.imshow("LINEAR", th)
# cv.waitKey(0)

# cv.destroyAllWindows()