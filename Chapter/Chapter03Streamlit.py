import streamlit as st
import numpy as np
import cv2
import os
from PIL import Image
from Chapter03 import *

# Giao diện Streamlit
st.title("Ứng dụng Xử lý Ảnh")


# Danh sách kỹ thuật xử lý
processing_options = [
    "Negative Image",
    "Logarit Image",
    "Power Image",
    "Piecewise Linear",
    "Histogram",
    "Histogram Equalization",
    "Histogram Equalization (Color)",
    "Local Histogram",
    "Histogram Statistics",
    "Box Filter (Custom)",
    "Box Filter (OpenCV)",
    "Threshold",
    "Median Filter",
    "Sharpen",
    "Gradient"
]

# Sidebar
st.header("Cài đặt Xử lý Ảnh")
use_sample_image = st.checkbox("Sử dụng ảnh mẫu", value=False)

# Tải ảnh mẫu hoặc ảnh chính
sample_image_file = None
if use_sample_image:
    sample_image_file = st.file_uploader("Chọn ảnh mẫu", type=["png", "jpg", "jpeg", "bmp"], key="sample_uploader")
    if sample_image_file:
        st.success("Đã chọn ảnh mẫu!")
    else:
        st.warning("Vui lòng tải ảnh mẫu!")

selected_option = st.selectbox("Chọn kỹ thuật xử lý", processing_options)

image_file = None
if not use_sample_image:
    image_file = st.file_uploader("Tải ảnh lên", type=["png", "jpg", "jpeg", "bmp"], key="main_uploader")

# Xử lý và hiển thị ảnh
if image_file or use_sample_image:
    
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
            st.subheader("Ảnh Gốc")
            st.image(image, use_container_width=True)

        with col2:
            st.subheader("Ảnh Đã Xử Lý")
            if selected_option == "Negative Image":
                imgout = Negative(imgin)
            elif selected_option == "Logarit Image":
                imgout = Logarit(imgin)
            elif selected_option == "Power Image":
                imgout = Power(imgin)
            elif selected_option == "Piecewise Linear":
                imgout = PiecewiseLinear(imgin)
            elif selected_option == "Histogram":
                imgout = Histogram(imgin)
            elif selected_option == "Histogram Equalization":
                imgout = HistEqual(imgin)
            elif selected_option == "Histogram Equalization (Color)":
                imgout = HistEqualColor(imgin)
            elif selected_option == "Local Histogram":
                imgout = LocalHist(imgin)
            elif selected_option == "Histogram Statistics":
                imgout = HistStat(imgin)
            elif selected_option == "Box Filter (Custom)":
                imgout = MyBoxFilter(imgin)
            elif selected_option == "Box Filter (OpenCV)":
                imgout = BoxFilter(imgin)
            elif selected_option == "Threshold":
                imgout = Threshold(imgin)
            elif selected_option == "Median Filter":
                imgout = MedianFilter(imgin)
            elif selected_option == "Sharpen":
                imgout = Sharpen(imgin)
            elif selected_option == "Gradient":
                imgout = Gradient(imgin)
            
            st.image(imgout, use_container_width=True, channels="BGR" if selected_option == "Histogram Equalization (Color)" else "GRAY")

    # Tải ảnh
    image = ""
    if image_file:
        image = Image.open(image_file)
        process_image(image)
    else:
        if sample_image_file:
            # Ảnh mẫu (cần có file ảnh mẫu trong thư mục)
            image = Image.open(sample_image_file)
            process_image(image)
        else:
            st.warning("Vui lòng tải ảnh lên hoặc chọn sử dụng ảnh mẫu!")

else:
    st.warning("Vui lòng tải ảnh lên hoặc chọn sử dụng ảnh mẫu!")