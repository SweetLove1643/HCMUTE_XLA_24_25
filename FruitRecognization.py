import os
import streamlit as st
import numpy as np
import cv2
from ultralytics import YOLO

def FruitRecognization():
    # Đường dẫn model PT
    model_path = "fruitRecognizationModel.pt"

    # Danh sách tên lớp
    class_names = ['sau_rieng', 'tao', 'thanh_long', 'MangCut', 'Chuoi']

    # Ngưỡng confidence và IoU
    CONF_THRESHOLD = 0.5
    IOU_THRESHOLD = 0.4

    # Tiêu đề ứng dụng
    st.title('🍎 Nhận dạng trái cây với YOLOv8')

    # Load model nếu chưa có
    if "LoadModel" not in st.session_state:
        st.session_state["Model"] = YOLO(model_path)
        st.session_state["LoadModel"] = True
        print('⚡ Load model lần đầu')
    else:
        print('✅ Model đã được load trước đó')

    # Hàm hiển thị kết quả
    def display_results(img, results):
        output_img = img.copy()
        boxes = results.boxes.xyxy.cpu().numpy() if hasattr(results.boxes, 'xyxy') else []
        confs = results.boxes.conf.cpu().numpy() if hasattr(results.boxes, 'conf') else []
        cls_ids = results.boxes.cls.cpu().numpy().astype(int) if hasattr(results.boxes, 'cls') else []

        for i, box in enumerate(boxes):
            x1, y1, x2, y2 = map(int, box)
            cls_id = cls_ids[i]
            conf = confs[i]
            cls_name = class_names[cls_id] if cls_id < len(class_names) else f"Class {cls_id}"

            cv2.rectangle(output_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"{cls_name}: {conf:.2f}"

            (label_width, label_height), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            cv2.rectangle(output_img, (x1, y1 - label_height - baseline), (x1 + label_width, y1), (255, 255, 255), cv2.FILLED)
            cv2.putText(output_img, label, (x1, y1 - baseline), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

        return output_img

    # Giao diện chính
    st.header("📷 Nhận dạng từ ảnh")

    # Upload ảnh
    st.subheader("📤 Tải ảnh lên")
    img_file_buffer = st.file_uploader("Chọn ảnh", type=["jpg", "jpeg", "png", "bmp"])
    img_array = None

    if img_file_buffer is not None:
        nparr = np.frombuffer(img_file_buffer.read(), np.uint8)
        img_array = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        display_img = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
        st.image(display_img, caption="Ảnh đã tải lên", use_container_width=True)

    # Nút nhận dạng
    if img_array is not None and st.button('🔍 Nhận dạng trái cây'):
        with st.spinner('⏳ Đang nhận dạng...'):
            results = st.session_state["Model"].predict(
                source=img_array,
                conf=CONF_THRESHOLD,
                iou=IOU_THRESHOLD,
                verbose=False
            )[0]

            processed_img = display_results(img_array, results)
            detection_count = len(results.boxes)

            processed_img_rgb = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
            st.success(f"✅ Đã phát hiện {detection_count} đối tượng.")
            st.image(processed_img_rgb, caption="📍 Kết quả nhận dạng", use_container_width=True)

            # Chi tiết nhận dạng
            if detection_count > 0:
                st.subheader("📋 Chi tiết nhận dạng")
                data = []
                boxes = results.boxes.xyxy.cpu().numpy()
                confs = results.boxes.conf.cpu().numpy()
                cls_ids = results.boxes.cls.cpu().numpy().astype(int)

                for i in range(detection_count):
                    cls_id = cls_ids[i]
                    cls_name = class_names[cls_id] if cls_id < len(class_names) else f"Loại {cls_id}"
                    conf = confs[i]
                    data.append({"Loại trái cây": cls_name, "Độ tin cậy": f"{conf:.4f}"})

                st.table(data)
