import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

def SepareateBackground():
    # CSS tông màu tối với focus vào chữ
    st.markdown("""
        <style>
            /* Tổng thể */
            #bgrem_app-container {
                background-color: #1f2937;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
                font-family: 'Inter', Arial, sans-serif;
            }
            /* Tiêu đề */
            h1[anchor="bgrem_app-title"] {
                color: #60a5fa;
                text-align: center;
                margin-bottom: 20px;
                font-size: 28px;
                font-weight: 600;
            }
            /* Subheader */
            h3[anchor="bgrem_replace-background"] {
                color: #d1d5db;
                margin-top: 20px;
                font-size: 20px;
                font-weight: 500;
            }
            /* File uploader - nhãn chữ */
            div[data-testid="stFileUploader"] {
                border: 2px dashed #6b7280;
                padding: 15px;
                border-radius: 8px;
                background-color: #374151;
                margin-bottom: 15px;
            }
            div[data-testid="stFileUploader"] label, 
            div[data-testid="stFileUploader"] p {
                color: #e5e7eb;
                font-size: 16px;
                font-weight: 400;
                margin-bottom: 10px;
            }
            /* Selectbox - nhãn chữ */
            div[data-testid="stSelectbox"] label, 
            div[data-testid="stSelectbox"] p {
                color: #e5e7eb;
                font-size: 16px;
                font-weight: 400;
                margin-bottom: 10px;
            }
            /* Color picker - nhãn chữ */
            div[data-testid="stColorPicker"] {
                border: 1px solid #6b7280;
                border-radius: 5px;
                padding: 10px;
                background-color: #374151;
            }
            div[data-testid="stColorPicker"] label, 
            div[data-testid="stColorPicker"] p {
                color: #e5e7eb;
                font-size: 16px;
                font-weight: 400;
                margin-bottom: 10px;
            }
            /* Button - chữ trong button */
            button[kind="primary"] {
                background-color: #1e40af;
                color: #ffffff;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                transition: background-color 0.3s;
                font-size: 16px;
                font-weight: 500;
            }
            button[kind="primary"]:hover {
                background-color: #2563eb;
            }
            /* Image caption */
            .stImage > div > img + div {
                font-style: italic;
                color: #d1d5db;
                text-align: center;
                margin-top: 5px;
                font-size: 14px;
                font-weight: 300;
            }
            /* Spinner - chữ trong spinner */
            .stSpinner > div {
                color: #60a5fa;
                font-size: 16px;
                font-weight: 400;
            }
            /* Text chính (st.write) */
            #bgrem_instruction-text, #bgrem_no_image_text {
                color: #e5e7eb;
                font-size: 16px;
                font-weight: 400;
                margin-bottom: 15px;
            }
            /* Thông báo lỗi */
            .stAlert > div {
                color: #f87171;
                font-size: 16px;
                font-weight: 400;
                margin-bottom: 15px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Hàm tiền xử lý ảnh
    def preprocess_image(image):
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        enhanced = cv2.convertScaleAbs(gray, alpha=1.2, beta=0)
        blurred = cv2.GaussianBlur(enhanced, (5, 5), 0)
        return cv2.cvtColor(blurred, cv2.COLOR_GRAY2RGB)

    # Hàm tách nền bằng GrabCut
    def remove_background(image):
        image_processed = preprocess_image(image)
        mask = np.zeros(image_processed.shape[:2], np.uint8)
        bgd_model = np.zeros((1, 65), np.float64)
        fgd_model = np.zeros((1, 65), np.float64)
        h, w = image_processed.shape[:2]
        margin = int(min(w, h) * 0.05)
        rect = (margin, margin, w - 2*margin, h - 2*margin)
        cv2.grabCut(image_processed, mask, rect, bgd_model, fgd_model, 10, cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        result = image * mask2[:, :, np.newaxis]
        alpha = mask2 * 255
        result = np.dstack((result, alpha))
        return result

    # Hàm thay nền
    def replace_background(foreground, background_color=None, background_image=None):
        rgb = foreground[:, :, :3]
        alpha = foreground[:, :, 3] / 255.0
        
        if background_color is not None:
            # Tạo nền màu đơn sắc (RGB)
            bg = np.full_like(rgb, background_color, dtype=np.uint8)
            # Pha trộn nền và đối tượng
            result = (rgb * alpha[:, :, np.newaxis] + bg * (1 - alpha[:, :, np.newaxis])).astype(np.uint8)
            # Thêm kênh alpha (255 để không trong suốt)
            return np.dstack((result, np.full_like(alpha, 255, dtype=np.uint8)))
        
        if background_image is not None:
            bg = cv2.resize(background_image, (foreground.shape[1], foreground.shape[0]))
            bg = cv2.cvtColor(bg, cv2.COLOR_RGBA2RGB) if bg.shape[2] == 4 else bg
            result = (rgb * alpha[:, :, np.newaxis] + bg * (1 - alpha[:, :, np.newaxis])).astype(np.uint8)
            return np.dstack((result, np.full_like(alpha, 255, dtype=np.uint8)))
        
        return foreground

    # Giao diện Streamlit
    st.title("Tách Nền Ảnh Tự Động", anchor="bgrem_app-title")
    st.write("Tải ảnh lên để tự động tách đối tượng chính khỏi nền. Bạn có thể chọn nền trong suốt, màu đơn sắc, hoặc ảnh nền.", key="bgrem_instruction-text")

    # Tải ảnh chính
    uploaded_file = st.file_uploader("Chọn ảnh chứa đối tượng", type=["jpg", "jpeg", "png"], key="bgrem_main_uploader")

    if uploaded_file is not None:
        # Đọc và xử lý ảnh
        image = Image.open(uploaded_file)
        image_np = np.array(image)
        max_size = 1000
        h, w = image_np.shape[:2]
        if max(w, h) > max_size:
            scale = max_size / max(w, h)
            new_w, new_h = int(w * scale), int(h * scale)
            image_np = cv2.resize(image_np, (new_w, new_h))
        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGBA2RGB) if image_np.shape[2] == 4 else image_np
        
        # Hiển thị ảnh gốc
        st.image(image_np, caption="Ảnh gốc", use_container_width=True)
        
        # Tách nền
        with st.spinner("Đang tách nền..."):
            result = remove_background(image_np)
            result_image = Image.fromarray(result, mode='RGBA')
        
        # Hiển thị ảnh với nền trong suốt
        st.image(result_image, caption="Ảnh với nền trong suốt", use_container_width=True)
        
        # Tùy chọn tải ảnh với nền trong suốt
        buf = io.BytesIO()
        result_image.save(buf, format="PNG")
        byte_im = buf.getvalue()
        st.download_button(
            label="Tải ảnh với nền trong suốt",
            data=byte_im,
            file_name="background_removed.png",
            mime="image/png",
            key="bgrem_download_transparent"
        )
        
        # Tùy chọn thay nền
        st.subheader("Thay nền mới", anchor="bgrem_replace-background")
        background_option = st.selectbox(
            "Chọn loại nền",
            ["Nền trong suốt", "Màu đơn sắc", "Ảnh nền"],
            key="bgrem_background_select"
        )
        
        if background_option == "Màu đơn sắc":
            color = st.color_picker("Chọn màu nền", "#FFFFFF", key="bgrem_color_picker")
            try:
                # Chuyển màu hex sang RGB
                color_rgb = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
                with st.spinner("Đang thay nền màu..."):
                    result_with_bg = replace_background(result, background_color=color_rgb)
                    result_image_bg = Image.fromarray(result_with_bg, mode='RGBA')
                
                # Hiển thị ảnh với nền màu
                st.image(result_image_bg, caption=f"Ảnh với nền màu {color}", use_container_width=True)
                
                # Tùy chọn tải ảnh
                buf = io.BytesIO()
                result_image_bg.save(buf, format="PNG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="Tải ảnh với nền màu",
                    data=byte_im,
                    file_name="background_colored.png",
                    mime="image/png",
                    key="bgrem_download_colored"
                )
            except Exception as e:
                st.error(f"Lỗi khi thay nền màu: {str(e)}")
        
        elif background_option == "Ảnh nền":
            bg_file = st.file_uploader("Chọn ảnh nền", type=["jpg", "jpeg", "png"], key="bgrem_bg_uploader")
            if bg_file is not None:
                bg_image = Image.open(bg_file)
                bg_image_np = np.array(bg_image)
                bg_image_np = cv2.cvtColor(bg_image_np, cv2.COLOR_RGBA2RGB) if bg_image_np.shape[2] == 4 else bg_image_np
                with st.spinner("Đang thay nền ảnh..."):
                    result_with_bg = replace_background(result, background_image=bg_image_np)
                    result_image_bg = Image.fromarray(result_with_bg, mode='RGBA')
                
                # Hiển thị ảnh với nền mới
                st.image(result_image_bg, caption="Ảnh với nền mới", use_column_width=True, key="bgrem_replaced_image")
                
                # Tùy chọn tải ảnh
                buf = io.BytesIO()
                result_image_bg.save(buf, format="PNG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="Tải ảnh với nền mới",
                    data=byte_im,
                    file_name="background_replaced.png",
                    mime="image/png",
                    key="bgrem_download_replaced"
                )
    else:
        st.write("Vui lòng tải lên một ảnh để bắt đầu.", key="bgrem_no_image_text")

    st.markdown('</div>', unsafe_allow_html=True)