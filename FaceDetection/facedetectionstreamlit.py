import streamlit as st
import numpy as np
import cv2
import onnxruntime as ort
import os
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import av

# Hàm phát hiện khuôn mặt sử dụng Haar Cascade
def detect_faces_haar(image, cascade_classifier, scale_factor=1.1, min_neighbors=5):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = cascade_classifier.detectMultiScale(
        gray,
        scaleFactor=scale_factor,
        minNeighbors=min_neighbors,
        minSize=(30, 30)
    )
    boxes = []
    for (x, y, w, h) in faces:
        x1, y1 = x, y
        x2, y2 = x + w, y + h
        boxes.append((x1, y1, x2, y2))
    return boxes

# Danh sách nhãn
class_names = ['Đẳng Cửu Dương', 'Hoàng Manh Tường', 'Quân Phan', 'Trịnh Hửu Thọ']

# Lớp xử lý video cho streamlit-webrtc
class FaceRecognitionProcessor(VideoProcessorBase):
    def __init__(self):
        # Load Haar Cascade
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        if not os.path.exists(cascade_path):
            raise FileNotFoundError(f"Haar Cascade file not found: {cascade_path}")
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        if self.face_cascade.empty():
            raise ValueError("Failed to load Haar Cascade classifier")

        # Load VGG16 classifier
        classifier_path = r"F:\Study\Projects\HK6\XLA\Project\FaceDetection\vgg_face_final.onnx"
        if not os.path.exists(classifier_path):
            raise FileNotFoundError(f"ONNX file not found: {classifier_path}")
        self.face_classifier = ort.InferenceSession(classifier_path)

    def recv(self, frame):
        # Chuyển đổi frame từ av.VideoFrame sang numpy array
        img = frame.to_ndarray(format="bgr24")

        # Resize khung hình nếu quá lớn
        max_size = 1280
        if max(img.shape[:2]) > max_size:
            scale = max_size / max(img.shape[:2])
            img = cv2.resize(img, (int(img.shape[1] * scale), int(img.shape[0] * scale)))

        # Phát hiện khuôn mặt
        boxes = detect_faces_haar(img, self.face_cascade, scale_factor=1.1, min_neighbors=5)

        # Nhận diện khuôn mặt
        for box in boxes:
            x1, y1, x2, y2 = box
            face_crop = img[y1:y2, x1:x2]
            if face_crop.size == 0 or face_crop.shape[0] < 10 or face_crop.shape[1] < 10:
                continue

            # Chuẩn bị ảnh cho phân loại
            face_crop = cv2.resize(face_crop, (224, 224))
            face_crop = face_crop[:, :, ::-1]  # BGR -> RGB
            face_crop = face_crop.astype(np.float32) / 255.0
            face_crop = np.expand_dims(face_crop, axis=0)

            # Phân loại khuôn mặt
            inputs = {self.face_classifier.get_inputs()[0].name: face_crop}
            preds = self.face_classifier.run(None, inputs)[0]
            label_id = np.argmax(preds)
            label_name = class_names[label_id]

            # Vẽ bounding box và nhãn
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, label_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # Chuyển đổi lại thành av.VideoFrame
        return av.VideoFrame.from_ndarray(img, format="bgr24")

# Giao diện Streamlit
st.title("Face Recognition with Webcam")
st.write("Ứng dụng nhận diện khuôn mặt sử dụng Haar Cascade và VGG16")

# Khởi tạo webcam stream
webrtc_streamer(
    key="face-recognition",
    video_processor_factory=FaceRecognitionProcessor,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)

st.write("Nhấn 'Stop' để dừng webcam hoặc đóng ứng dụng.")