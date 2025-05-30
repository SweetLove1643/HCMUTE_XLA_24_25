import streamlit as st
import numpy as np
import cv2
import os
from PIL import Image
from Chapter03 import *



def Chapter3StreamlitUI():
    # Thêm CSS để tùy chỉnh giao diện
    st.markdown("""
    <style>
    /* Tùy chỉnh giao diện tổng thể */
    body {
        font-family: 'Poppins', sans-serif;
        background-color: #1a1a1a;
        margin: 0;
        padding: 30px;
    }

    /* Tùy chỉnh tiêu đề chính */
    h1 {
        color: #00e676;
        text-align: center;
        font-size: 3.2em;
        text-shadow: 0 0 8px rgba(0, 230, 118, 0.5);
        margin-bottom: 40px;
    }

    /* Tùy chỉnh tiêu đề phụ */
    h3 {
        color: #e0e0e0;
        font-size: 1.7em;
        margin-top: 20px;
        margin-bottom: 12px;
    }

    /* Tùy chỉnh file uploader */
    .stFileUploader > div > div {
        background-color: #333333;
        border: 1px solid #00e676;
        border-radius: 6px;
        padding: 15px;
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    .stFileUploader > div > div:hover {
        background-color: #4a4a4a;
        box-shadow: 0 0 10px rgba(0, 230, 118, 0.5);
    }

    /* Tùy chỉnh checkbox */
    .stCheckbox > label {
        color: #e0e0e0;
        font-weight: 600;
        margin-bottom: 20px;
    }

    /* Tùy chỉnh ảnh */
    .stImage > img {
        border: 2px solid #00e676;
        border-radius: 6px;
        box-shadow: 0 0 10px rgba(0, 230, 118, 0.3);
        margin: 15px 0;
        transition: filter 0.3s ease;
    }
    .stImage > img:hover {
        filter: brightness(1.1);
    }


    /* Tùy chỉnh thông báo thành công */
    .stSuccess {
        background-color: #00e676;
        color: #1a1a1a;
        border: 1px solid #00e676;
        border-radius: 6px;
        padding: 12px;
        margin-bottom: 20px;
    }

    /* Tùy chỉnh khoảng cách giữa các cột */
    .stColumns > div {
        padding: 25px;
    }

    /* Tùy chỉnh expander */
    .stExpander {
        background-color: #2c2c2c;
        border: 1px solid #FF3333;
        border-radius: 8px;
        box-shadow: 0 0 8px rgba(0, 230, 118, 0.3);
    }
    .stExpander > div > div {
        color: #e0e0e0;
    }

    /* Tùy chỉnh nút */
    .stButton > button {
        background-color: #00e676;
        color: #1a1a1a;
        border: 1px solid #00e676;
        border-radius: 6px;
        padding: 10px 20px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #4a4a4a;
        box-shadow: 0 0 10px rgba(0, 230, 118, 0.5);
    }


    /* Tải phông chữ Poppins */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
    </style>
    """, unsafe_allow_html=True)

    # Giao diện Streamlit
    st.title("Ứng dụng Xử lý Ảnh", anchor="basic_app-title")

    # Danh sách kỹ thuật xử lý
    processing_options = [
        "Negative Image (Đảo ngược cường độ ánh sáng)",
        "Logarit Image (Tăng độ tương phản)",
        "Power Image (Điều chỉnh độ tương phản)",
        "Piecewise Linear (Điều chỉnh độ sáng)",
        "Histogram (Phân tích đặc tính và độ sáng)",
        "Histogram Equalization (Cân bằng sáng)",
        "Histogram Equalization (Color) (Cân bằng sáng cho ảnh màu)",
        "Local Histogram (Cân bằng sáng cục bộ)",
        "Histogram Statistics (Thống kê đặc trưng)",
        "Box Filter (Custom) (Lọc trung bình)",
        "Box Filter (OpenCV)",
        "Threshold (Phân ngưỡng)",
        "Median Filter (Lọc trung vị)",
        "Sharpen (Tăng nét)",
        "Gradient"
    ]

    # Điều khiển trong khu vực chính
    with st.container():
        with st.expander("Cài đặt Xử lý Ảnh", expanded=True):
            selected_option = st.selectbox(
                "Chọn kỹ thuật xử lý",
                processing_options,
                key="basic_processing_selectbox"
            )
            if selected_option:
                st.success(f"Đã chọn kỹ thuật: {selected_option}")
            use_sample_image = st.checkbox(
                "Sử dụng ảnh mẫu",
                value=False,
                key="basic_sample_image_checkbox"
            )

            # Tải ảnh mẫu hoặc ảnh chính
            sample_image_file = None
            if use_sample_image:
                sample_image_file = st.file_uploader(
                    "Chọn ảnh mẫu",
                    type=["png", "jpg", "jpeg", "bmp"],
                    key="basic_sample_uploader"
                )
                if sample_image_file:
                    st.success("Đã chọn ảnh mẫu!")
                else:
                    st.warning("Vui lòng tải ảnh mẫu!")
            
            image_file = None
            if not use_sample_image:
                image_file = st.file_uploader(
                    "Tải ảnh lên",
                    type=["png", "jpg", "jpeg", "bmp"],
                    key="basic_main_uploader"
                )
        
        st.markdown('<div id="basic_settings-container"></div>', unsafe_allow_html=True)

    # Xử lý và hiển thị ảnh
    if image_file or sample_image_file:
        
        def process_image(image):
            image_array = np.array(image)
            if len(image_array.shape) == 3:
                if selected_option == "Histogram Equalization (Color)":
                    imgin = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
                else:
                    imgin = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
            else:
                imgin = image_array

            # Hiển thị ảnh gốc và ảnh đã xử lý
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Ảnh Gốc", anchor="basic_original-image")
                st.image(image, use_container_width=True)
            
            with col2:
                st.subheader("Ảnh Đã Xử Lý", anchor="basic_processed-image")
                if selected_option == "Negative Image (Đảo ngược cường độ ánh sáng)":
                    imgout = Negative(imgin)
                elif selected_option == "Logarit Image (Tăng độ tương phản)":
                    imgout = Logarit(imgin)
                elif selected_option == "Power Image (Điều chỉnh độ tương phản)":
                    imgout = Power(imgin)
                elif selected_option == "Piecewise Linear (Điều chỉnh độ sáng)":
                    imgout = PiecewiseLinear(imgin)
                elif selected_option == "Histogram (Phân tích đặc tính và độ sáng)":
                    imgout = Histogram(imgin)
                elif selected_option == "Histogram Equalization (Cân bằng sáng)":
                    imgout = HistEqual(imgin)
                elif selected_option == "Histogram Equalization (Color) (Cân bằng sáng cho ảnh màu)":
                    imgout = HistEqualColor(image_array)
                elif selected_option == "Local Histogram (Cân bằng sáng cục bộ)":
                    imgout = LocalHist(imgin)
                elif selected_option == "Histogram Statistics (Thống kê đặc trưng)":
                    imgout = HistStat(imgin)
                elif selected_option == "Box Filter (Custom) (Lọc trung bình)":
                    imgout = MyBoxFilter(imgin)
                elif selected_option == "Box Filter (OpenCV)":
                    imgout = BoxFilter(imgin)
                elif selected_option == "Threshold (Phân ngưỡng)":
                    imgout = Threshold(imgin)
                elif selected_option == "Median Filter (Lọc trung vị)":
                    imgout = MedianFilter(imgin)
                elif selected_option == "Sharpen (Tăng nét)":
                    imgout = Sharpen(image_array)
                elif selected_option == "Gradient":
                    imgout = Gradient(imgin)
                
                st.image(imgout, use_container_width=True, channels="BGR" if selected_option == "Histogram Equalization (Color)" else "GRAY")

        # Tải ảnh
        if image_file:
            image = Image.open(image_file)
            process_image(image)
        else:
            if sample_image_file:
                image = Image.open(sample_image_file)
                process_image(image)
            else:
                st.warning("Vui lòng tải ảnh lên hoặc chọn sử dụng ảnh mẫu!")

    else:
        st.warning("Vui lòng tải ảnh lên hoặc chọn sử dụng ảnh mẫu!")