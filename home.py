def home():
    import streamlit as st

    # CSS tùy chỉnh
    def local_css():
        st.markdown("""
        <style>
        /* Tổng thể */
        .stApp {
            font-family: 'Arial', sans-serif;
        }

        /* Tiêu đề */
        h1, h2, h3 {
            color: #2c3e50;
            text-align: center;
        }

        /* Nội dung chính */
        .main .block-container {
            background-color: white;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }

        /* Expander */
        .stExpander {
            background-color: #ecf0f1;
            border-radius: 8px;
            margin-bottom: 10px;
        }

        .stExpander summary {
            background-color: #3498db;
            color: white;
            padding: 15px;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .stExpander summary:hover {
            background-color: #2980b9;
        }

        .stExpander div {
            padding: 15px;
            color: #2c3e50;
        }

        /* Thành viên */
        .member-card {
            background-color: #D2B48C;
            border-radius: 10px;
            padding: 20px;
            margin: 10px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            text-align: center;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .main .block-container {
                padding: 20px;
            }
            .member-card {
                margin: 5px;
            }
        }
        </style>
        """, unsafe_allow_html=True)

    # Áp dụng CSS
    local_css()

    # Tiêu đề
    st.title("Giới Thiệu Dự Án Nhóm")

    # Giới thiệu thành viên
    st.header("Thành Viên Nhóm")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='member-card'>
            <h3>Phan Văn Quân</h3>
            <p>Mã số sinh viên: 22110124</p>
            <p>Vai trò: Phát triển các module nhận diện và tối ưu hóa giao diện</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='member-card'>
            <h3>Hoàng Mạnh Tường</h3>
            <p>Mã số sinh viên: 22110262</p>
            <p>Vai trò: Xử lý dữ liệu và tích hợp các thuật toán AI</p>
        </div>
        """, unsafe_allow_html=True)

    # Giới thiệu dự án
    st.header("Các Phần Của Dự Án")

    # Face Recognition
    with st.expander("Nhận Diện Khuôn Mặt"):
        st.write("""
        **Mô tả**: Module nhận diện khuôn mặt sử dụng các thuật toán học sâu để xác định và nhận diện khuôn mặt trong hình ảnh hoặc video.
        
        **Công nghệ sử dụng**: OpenCV, TensorFlow, MTCNN.
        
        **Hướng dẫn sử dụng**:
        1. Chọn chế độ nhận diện khuôn mặt thông qua ảnh hoặc camera.
        2. Tải ảnh bạn muốn nhận diện lên, hoặc chọn thiết bị camera đầu vào
        3. Nhấn nút "Nhận diện" để xem kết quả.
        4. Kết quả sẽ hiển thị tên của khuôn mặt đã nhận diện.
        
        **Lưu ý**: Đảm bảo hình ảnh có độ sáng tốt để đạt kết quả tối ưu.
        """)

    # Fruit Recognition
    with st.expander("Nhận Diện Trái Cây"):
        st.write("""
        **Mô tả**: Module nhận diện trái cây giúp phân loại các loại trái cây dựa trên hình ảnh đầu vào.
        
        **Công nghệ sử dụng**: YOLO, Dataset trái cây tùy chỉnh.
        
        **Hướng dẫn sử dụng**:
        1. Chụp hoặc tải lên hình ảnh trái cây.
        2. Nhấn "Phân loại" để nhận kết quả.
        3. Kết quả sẽ hiển thị số lượng và loại trái cây và độ tin cậy.
        
        **Lưu ý**: Hình ảnh cần rõ nét và chỉ chứa một loại trái cây chính.
        """)

    # Chapters
    with st.expander("Các Chương Dự Án"):
        st.write("""
        **Mô tả**: Dự án được tổng hợp từ các mini project ở các chapter 3, 4, 5 và 9 trong chương trình học.
        
        **Danh sách chương**:
        - **Chương 3**: Bao gồm các phương pháp biến đổi ảnh như: Đảo ngược ảnh sáng, tăng tương phản cho ảnh, các phương pháp lọc hoặc tính toán gradient.
        - **Chương 4**: Bao gồm các phương pháp xử lí ảnh trong miền tần số như: Spectrum, Frequency Filter, ...
        - **Chương 5**: Bao gồm các phương pháp xử lí ảnh như: Gây nhiễu, khôi phục và tăng cường ảnh, lọc nhiễu.
        - **Chương 9**: Bao gồm các phương pháp trích xuất thông tin từ ảnh như: Đếm vật thể, tìm khu vực liên thông và tìm biên ảnh.
        **Hướng dẫn sử dụng**:
        1. Truy cập và các chương chứa phương pháp muốn xử lí
        2. Chọn phương pháp muốn xử lí và tải ảnh lên
        3. Nhấn nút xử lí và tải ảnh xuống nếu muốn.
        
        **Lưu ý**: Tùy thuộc vào chất lượng của ảnh để chọn phương pháp cho phù hợp.
        """)

    # Vehicle Recognition
    with st.expander("Nhận Diện Xe"):
        st.write("""
        **Mô tả**: Module nhận diện các loại phương tiện như xe máy, xe đạp, ô tô, ... dựa trên hình ảnh.
        
        **Công nghệ sử dụng**: YOLOv8, OpenCV.
        
        **Hướng dẫn sử dụng**:
        1. Tải lên hình ảnh chứa phương tiện.
        2. Nhấn "Nhận diện" để xem kết quả.
        3. Kết quả sẽ hiển thị loại phương tiện và vị trí trong hình ảnh.
        
        **Lưu ý**: Đảm bảo phương tiện được chụp rõ ràng, không bị che khuất.
        """)

    # Background Removal
    with st.expander("Tách Nền Hình Ảnh"):
        st.write("""
        **Mô tả**: Module tách nền giúp loại bỏ nền khỏi hình ảnh, giữ lại đối tượng chính và thay thế nền cũ bằng nền khác.
        
        **Công nghệ sử dụng**: OpenCV, cv2
        
        **Hướng dẫn sử dụng**:
        1. Tải lên hình ảnh cần tách nền.
        2. Nhấn "Tách nền" để xử lý.
        3. Chọn loại nền muốn sử dụng để thay thế(nền đơn sắc hoặc ảnh khác)
        4. Nhấn "Thay thế" để thêm ảnh nền sau khi tách
        
        **Lưu ý**: Đối tượng chính cần nổi bật so với nền để đạt kết quả tốt nhất.
        """)

    

    # Footer
    st.markdown("""
    <div style='text-align: center; margin-top: 20px; color: #7f8c8d;'>
        Được phát triển bởi Phan Văn Quân & Hoàng Mạnh Tường | 2025
    </div>
    """, unsafe_allow_html=True)