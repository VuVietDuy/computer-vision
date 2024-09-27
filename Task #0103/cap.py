import cv2
import os
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')
# Các biến toàn cục
start_point = None
end_point = None
selecting_roi = False
image_counter = 1  # Đếm số lượng ảnh đã chụp
output_folder = 'mouse_capture/ROI_img'
label_dict = {'e': 'eye', 'f': 'finger', 'm' : 'mouth', 'n' : 'nose'}  # Danh sách các nhãn
labels = []  # Danh sách lưu nhãn và thông tin các đối tượng

def mouse_callback(event, x, y, flags, param):
    global start_point, end_point, selecting_roi

    if event == cv2.EVENT_LBUTTONDOWN: 
        start_point = (x, y)
        selecting_roi = True

    elif event == cv2.EVENT_MOUSEMOVE and selecting_roi:
        end_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        end_point = (x, y)
        selecting_roi = False

def save_roi(start_point, end_point):
    global cap, image_counter
    # Đọc lại khung hình để trích xuất ROI
    ret, frame = cap.read()
    if not ret:
        print("Lỗi: Không thể đọc khung hình.")
        return

    # Trích xuất ROI dựa trên tọa độ đã chọn
    x1, y1 = start_point
    x2, y2 = end_point
    roi = frame[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)]
    
    # Tạo tên tệp dựa trên số lượng ảnh đã chụp
    filename = f'{output_folder}/roi_image{image_counter}.png'
    
    # Lưu ROI thành tệp
    cv2.imwrite(filename, roi)
    print(f"Ảnh ROI đã được lưu với tên {filename}.")

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

def main():
    global cap, image_counter

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(output_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_counter += 1

    # Khởi tạo webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Lỗi: Không thể mở webcam.")
        return

    cv2.namedWindow('Video Stream')
    cv2.setMouseCallback('Video Stream', mouse_callback)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Lỗi: Không thể đọc khung hình.")
            break

        # Hiển thị khung hình và ROI đang chọn
        if start_point and end_point:
            cv2.rectangle(frame, start_point, end_point, (0, 255, 0), 2)

        cv2.imshow('Video Stream', frame)

        key = cv2.waitKey(1)

        if key == 27:  # Phím ESC để thoát
            break
        elif key in [ord('e'), ord('f'), ord('m'), ord('n')]:  # Gán nhãn khi nhấn các phím tương ứng
            label = label_dict[chr(key)]
            save_roi(start_point, end_point)  # Lưu vùng ảnh
            save_label(start_point, end_point, label)  # Lưu nhãn và tọa độ
            image_counter += 1
    cap.release()
    cv2.destroyAllWindows()

main()