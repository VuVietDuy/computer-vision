import cv2
import os

def load_images_from_folder(folder):
    images = []
    print(os.listdir(folder))
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images

def resize_images(folder, width, height):
    images = load_images_from_folder(folder)
    resized_images = []
    for img in images:
        resized_img = cv2.resize(img, (width, height))
        resized_images.append(resized_img)
    return resized_images

def save_resized_images(folder, resized_images):
    if not os.path.exists(folder):
        os.makedirs(folder)
    for i, img in enumerate(resized_images):
        cv2.imwrite(os.path.join(folder, f'resized_image_{i+1}.jpg'), img)
    
resize_images = resize_images("./images", 250, 250)
save_resized_images("./resized_images", resize_images)