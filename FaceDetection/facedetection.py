import numpy as np
import cv2
import onnxruntime as ort
import os

# Hàm phát hiện khuôn mặt sử dụng Haar Cascade
def detect_faces_haar(image, cascade_classifier, scale_factor=1.1, min_neighbors=5):
    # Chuyển ảnh sang grayscale (yêu cầu của Haar Cascade)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Phát hiện khuôn mặt
    faces = cascade_classifier.detectMultiScale(
        gray,
        scaleFactor=scale_factor,  # Tỷ lệ thu nhỏ mỗi lần quét
        minNeighbors=min_neighbors,  # Số lượng hàng xóm tối thiểu
        minSize=(30, 30)  # Kích thước tối thiểu của khuôn mặt
    )
    
    boxes = []
    for (x, y, w, h) in faces:
        x1, y1 = x, y
        x2, y2 = x + w, y + h
        boxes.append((x1, y1, x2, y2))
        print(f"Detected face: ({x1}, {y1}, {x2}, {y2})")
    
    return boxes

# Danh sách nhãn
# class_names = ['Đẳng Cửu Dương', 'Hoàng Manh Tường', 'Quân Phan', 'Trịnh Hửu Thọ']
class_names = ['Đang_Cuu_Duong', 'Hoang_Manh_Tuong', 'Quan_Phan', 'Trinh_Huu_Tho']

# 1. Load Haar Cascade Classifier
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
if not os.path.exists(cascade_path):
    raise FileNotFoundError(f"Haar Cascade file not found: {cascade_path}")
face_cascade = cv2.CascadeClassifier(cascade_path)
if face_cascade.empty():
    raise ValueError("Failed to load Haar Cascade classifier")

# 2. Load VGG16 classifier
classifier_path = r"vgg_face_final.onnx"
if not os.path.exists(classifier_path):
    raise FileNotFoundError(f"ONNX file not found: {classifier_path}")
face_classifier = ort.InferenceSession(classifier_path)

# 3. Khởi tạo camera
cap = cv2.VideoCapture(0)  # 0 là camera mặc định
if not cap.isOpened():
    raise ValueError("Cannot open camera")

try:
    # 4. Vòng lặp xử lý khung hình từ camera
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Resize khung hình nếu quá lớn
        max_size = 1280
        if max(frame.shape[:2]) > max_size:
            scale = max_size / max(frame.shape[:2])
            frame = cv2.resize(frame, (int(frame.shape[1] * scale), int(frame.shape[0] * scale)))

        # Phát hiện khuôn mặt bằng Haar Cascade
        boxes = detect_faces_haar(frame, face_cascade, scale_factor=1.1, min_neighbors=5)

        # Lặp qua các bounding box và nhận diện
        for box in boxes:
            x1, y1, x2, y2 = box
            face_crop = frame[y1:y2, x1:x2]
            if face_crop.size == 0 or face_crop.shape[0] < 10 or face_crop.shape[1] < 10:
                print("Skipping small face region")
                continue  # Bỏ qua vùng mặt quá nhỏ

            # Chuẩn bị ảnh cho phân loại
            face_crop = cv2.resize(face_crop, (224, 224))
            face_crop = face_crop[:, :, ::-1]  # BGR -> RGB
            face_crop = face_crop.astype(np.float32) / 255.0
            face_crop = np.expand_dims(face_crop, axis=0)

            # Phân loại khuôn mặt
            inputs = {face_classifier.get_inputs()[0].name: face_crop}
            preds = face_classifier.run(None, inputs)[0]
            label_id = np.argmax(preds)
            label_name = class_names[label_id]
            print(f"Detected: {label_name}, Box: ({x1}, {y1}, {x2}, {y2})")

            # Vẽ bounding box và nhãn
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # Hiển thị khung hình
        cv2.imshow("Face Recognition", frame)

        # Thoát khi nhấn phím 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Giải phóng tài nguyên
    cap.release()
    try:
        cv2.destroyAllWindows()
    except cv2.error as e:
        print("Lỗi khi đóng cửa sổ OpenCV:", e)