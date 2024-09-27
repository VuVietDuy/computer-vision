import cv2
import numpy as np

class Image:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)
    
    def show_image(self):
        cv2.imshow('Original Image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def show_gray_image(self):
        gray_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Grayscale Image', gray_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def split_color_channels(self):
        b, g, r = cv2.split(self.image)
        cv2.imshow('Blue Channel', b)
        cv2.imshow('Green Channel', g)
        cv2.imshow('Red Channel', r)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

class Video:
    def __init__(self, video_path):
        self.video_path = video_path
        self.video = cv2.VideoCapture(video_path)
    
    def show_video(self):
        while True:
            ret, frame = self.video.read()
            if not ret:
                break
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.video.release()
        cv2.destroyAllWindows()

class Camera:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
    def show_webcam(self):
        while True:
            ret, frame = self.camera.read()
            if not ret:
                break
            cv2.imshow('Webcam', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.camera.release()
        cv2.destroyAllWindows()

def show_img():
    img = cv2.imread("image.jpg", cv2.COLOR_BGR2RGBA)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def resize_image():
    img = cv2.imread("image.jpg")
    resized_img = cv2.resize(img, (100, 100))
    cv2.imshow("Resized Image", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def shift_image():
    img = cv2.imread("image.jpg")
    M = np.float32([[1, 0, 100], 
                    [0, 1, 50]])
    shifted_image  = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    cv2.imshow('Shifted Image', shifted_image )
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# shift_image()

def cap_video():
    video = cv2.VideoCapture(0)
    while True:
        ret, frame = video.read()
        if not ret:
            break
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("cap_video_image.png", frame)
            break
    video.release()
    cv2.destroyAllWindows()

def shear_image():
    img = cv2.imread("image.jpg")
    shear_matrix = np.float32([[1, 0.5, 0], 
                    [0.5, 1, 0]])
    sheared_image   = cv2.warpAffine(img, shear_matrix, (img.shape[1], img.shape[0]))
    cv2.imshow('Shifted Image', sheared_image  )
    cv2.waitKey(0)
    cv2.destroyAllWindows()

shear_image()

# img = cv2.imread("image.jpg")
# resized_img = cv2.resize(img, (100, 80))
# cv2.imwrite("output_image.jpg", resized_img)