import cv2
import os
import json

# Khởi tạo các biến để lưu điểm bắt đầu, kết thúc và nhãn
drawing = False
start_point = (-1, -1)
end_point = (-1, -1)
label = ""
label_dict = {'c': 'car', 'h': 'human', 'b': 'building'}
image_counter = 1  # Đếm số lượng ảnh đã chụp
output_folder = 'roi_img'
labels = []

# Hàm callback xử lý sự kiện chuột
def draw_rectangle(event, x, y, flags, param):
    global start_point, end_point, drawing, label, image_counter

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            end_point = (x, y)
            img_copy = img.copy()
            cv2.rectangle(img_copy, start_point, end_point, (0, 255, 0), 2)
            cv2.imshow('Image', img_copy)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)
        cv2.rectangle(img, start_point, end_point, (0, 255, 0), 2)

        # Hiển thị lựa chọn nhãn dựa trên phím bấm
        key = cv2.waitKey(0)  # Dừng cho đến khi nhấn phím

        if key in [ord('c'), ord('h'), ord('b')]:
            label = label_dict[chr(key)]
            save_roi(start_point, end_point, label)
            save_label(start_point, end_point, label)
            cv2.putText(img, label, (start_point[0], start_point[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            cv2.imshow('Image', img)


def save_label(start_point, end_point, label):
    global image_counter
    x1, y1 = start_point
    x2, y2 = end_point
    data = {
        "image": f'roi_image{image_counter}.png',
        "label": label,
        "coordinates": {
            "top_left": (min(x1, x2), min(y1, y2)),
            "bottom_right": (max(x1, x2), max(y1, y2))
        }
    }
    labels.append(data)

    # Lưu thông tin vào file JSON
    with open(f'{output_folder}/labels.json', 'w') as json_file:
        json.dump(labels, json_file, indent=4)
    print(f"Nhãn '{label}' đã được lưu cho ROI.")

def save_roi(start_point, end_point, label):
    global image_counter

    x1, y1 = start_point
    x2, y2 = end_point

    # Tạo roi từ các điểm
    roi = img[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)]

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    filename = os.path.join(output_folder, f'{label}_{image_counter}.png')
    image_counter += 1  # Tăng bộ đếm sau mỗi lần lưu

    print(f"Saving ROI from {start_point} to {end_point} as {filename}")
    
    if cv2.imwrite(filename, roi):
        print(f"Image saved successfully: {filename}")
    else:
        print(f"Failed to save image: {filename}")

# Đọc ảnh đầu vào
img = cv2.imread('city.jpg')

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_rectangle)

# Vòng lặp chính hiển thị ảnh
while True:
    cv2.imshow('Image', img)

    key = cv2.waitKey(1)
    if key == 27:  # Phím ESC để thoát
        save_path = 'output_image.jpg' 
        cv2.imwrite(save_path, img)
        print(f"Hình ảnh đã được lưu tại: {save_path}")
        break

cv2.destroyAllWindows()
