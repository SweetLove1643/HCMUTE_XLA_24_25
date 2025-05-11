import os
import streamlit as st
import numpy as np
import cv2
from ultralytics import YOLO

def VehicleRecognization():
    # CSS tông màu tối với độ đặc hiệu cao và căn giữa tiêu đề
    st.markdown("""
        <style>
            /* Tổng thể */
            #vehicle_app-container {
                background-color: #1f2937 !important;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
                font-family: 'Inter', Arial, sans-serif;
            }
            /* Tiêu đề chính */
            .stApp #vehicle_app-container h1[anchor="vehicle_app-title"] {
                color: #60a5fa !important;
                text-align: center !important;
                margin-bottom: 20px;
                font-size: 28px !important;
                font-weight: 600 !important;
                text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
                display: block !important;
                width: 100% !important;
            }
            /* Header */
            .stApp #vehicle_app-container h2[anchor="vehicle_image-section"] {
                color: #d1d5db !important;
                text-align: center !important;
                margin-top: 20px;
                margin-bottom: 15px;
                font-size: 24px !important;
                font-weight: 500 !important;
                display: block !important;
                width: 100% !important;
            }
            /* Subheader */
            .stApp #vehicle_app-container h3[anchor="vehicle_upload-section"],
            .stApp #vehicle_app-container h3[anchor="vehicle_details-section"] {
                color: #d1d5db !important;
                text-align: left !important;
                margin-top: 15px;
                margin-bottom: 10px;
                font-size: 20px !important;
                font-weight: 500 !important;
                display: block !important;
                width: 100% !important;
            }
            /* File uploader */
            .stApp #vehicle_app-container div[data-testid="stFileUploader"] {
                border: 2px dashed #6b7280 !important;
                padding: 15px;
                border-radius: 8px;
                background-color: #374151 !important;
                margin-bottom: 15px;
            }
            .stApp #vehicle_app-container div[data-testid="stFileUploader"] label, 
            .stApp #vehicle_app-container div[data-testid="stFileUploader"] p {
                color: #e5e7eb !important;
                font-size: 16px !important;
                font-weight: 400 !important;
                margin-bottom: 10px;
            }
            /* Button */
            .stApp #vehicle_app-container button[kind="primary"] {
                background-color: #1e40af !important;
                color: #ffffff !important;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                transition: background-color 0.3s;
                font-size: 16px !important;
                font-weight: 500 !important;
            }
            .stApp #vehicle_app-container button[kind="primary"]:hover {
                background-color: #2563eb !important;
            }
            /* Image caption */
            .stApp #vehicle_app-container .stImage > div > img + div {
                font-style: italic;
                color: #d1d5db !important;
                text-align: center !important;
                margin-top: 5px;
                font-size: 14px !important;
                font-weight: 300 !important;
            }
            /* Spinner */
            .stApp #vehicle_app-container .stSpinner > div {
                color: #60a5fa !important;
                font-size: 16px !important;
                font-weight: 400 !important;
            }
            /* Success message */
            .stApp #vehicle_app-container .stAlert > div {
                color: #60a5fa !important;
                font-size: 16px !important;
                font-weight: 400 !important;
                margin-bottom: 15px;
            }
            /* Table */
            .stApp #vehicle_app-container .stTable table {
                background-color: #374151 !important;
                border: 1px solid #6b7280 !important;
                border-radius: 5px;
                color: #ffffff !important;
                font-size: 16px !important;
                font-weight: 400 !important;
            }
            .stApp #vehicle_app-container .stTable th, 
            .stApp #vehicle_app-container .stTable td {
                padding: 10px;
                border-bottom: 1px solid #6b7280 !important;
            }
            /* Container upload và kết quả */
            #vehicle_upload-container, #vehicle_results-container {
                margin-bottom: 20px;
                padding: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Đường dẫn model PT
    model_path = "VehicleRecognization.pt"

    # Danh sách tên lớp
    class_names = ['Bicycle', 'Motor', 'Car', 'BusTruck']

    # Ngưỡng confidence và IoU
    CONF_THRESHOLD = 0.5
    IOU_THRESHOLD = 0.4

    # Giao diện Streamlit
    st.title('🚗 Vehicle Recognization', anchor="vehicle_app-title")
    st.write("Ứng dụng nhận diện phương tiện giao thông")

    # Load model nếu chưa có
    if "LoadVehicleModel" not in st.session_state:
        st.session_state["VehicleModel"] = YOLO(model_path)
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
    st.header("📷 Nhận dạng từ ảnh", anchor="vehicle_image-section")
    
    # Upload ảnh và nút nhận dạng
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("📤 Tải ảnh lên", anchor="vehicle_upload-section")
        img_file_buffer = st.file_uploader("Chọn ảnh", type=["jpg", "jpeg", "png", "bmp"], key="vehicle_main_uploader")
        if img_file_buffer is not None:
            recognize = st.button('🔍 Nhận dạng phương tiện', key="vehicle_recognize_button")
    with col2:
        img_array = None
        if img_file_buffer is not None:
            nparr = np.frombuffer(img_file_buffer.read(), np.uint8)
            img_array = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            display_img = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
            st.image(display_img, caption="Ảnh đã tải lên", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Xử lý nhận dạng
    if img_array is not None and recognize:
        with st.spinner('⏳ Đang nhận dạng...'):
            results = st.session_state["VehicleModel"].predict(
                source=img_array,
                conf=CONF_THRESHOLD,
                iou=IOU_THRESHOLD,
                verbose=False
            )[0]

            processed_img = display_results(img_array, results)
            detection_count = len(results.boxes)

            processed_img_rgb = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
            st.success(f"✅ Đã phát hiện {detection_count} phương tiện.")
            st.image(processed_img_rgb, caption="📍 Kết quả nhận dạng", use_container_width=True)

            # Chi tiết nhận dạng
            if detection_count > 0:
                st.subheader("📋 Chi tiết nhận dạng", anchor="vehicle_details-section")
                data = []
                boxes = results.boxes.xyxy.cpu().numpy()
                confs = results.boxes.conf.cpu().numpy()
                cls_ids = results.boxes.cls.cpu().numpy().astype(int)

                for i in range(detection_count):
                    cls_id = cls_ids[i]
                    cls_name = class_names[cls_id] if cls_id < len(class_names) else f"Loại {cls_id}"
                    conf = confs[i]
                    data.append({"Loại phương tiện": cls_name, "Độ tin cậy": f"{conf:.4f}"})

                st.table(data)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)