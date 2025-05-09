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
            <p>Mã số sinh viên: 22110215</p>
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
        1. Tải lên hình ảnh hoặc video chứa khuôn mặt.
        2. Chọn chế độ nhận diện (đơn khuôn mặt hoặc đa khuôn mặt).
        3. Nhấn nút "Nhận diện" để xem kết quả.
        4. Kết quả sẽ hiển thị tên và độ chính xác của khuôn mặt đã nhận diện.
        
        **Lưu ý**: Đảm bảo hình ảnh có độ sáng tốt để đạt kết quả tối ưu.
        """)

    # Fruit Recognition
    with st.expander("Nhận Diện Trái Cây"):
        st.write("""
        **Mô tả**: Module nhận diện trái cây giúp phân loại các loại trái cây dựa trên hình ảnh đầu vào.
        
        **Công nghệ sử dụng**: PyTorch, CNN, Dataset trái cây tùy chỉnh.
        
        **Hướng dẫn sử dụng**:
        1. Chụp hoặc tải lên hình ảnh trái cây.
        2. Chọn loại mô hình nhận diện (nếu có nhiều mô hình).
        3. Nhấn "Phân loại" để nhận kết quả.
        4. Kết quả sẽ hiển thị loại trái cây và độ tin cậy.
        
        **Lưu ý**: Hình ảnh cần rõ nét và chỉ chứa một loại trái cây chính.
        """)

    # Vehicle Recognition
    with st.expander("Nhận Diện Xe"):
        st.write("""
        **Mô tả**: Module nhận diện các loại phương tiện như xe máy, xe đạp, ô tô dựa trên hình ảnh hoặc video.
        
        **Công nghệ sử dụng**: YOLOv5, OpenCV.
        
        **Hướng dẫn sử dụng**:
        1. Tải lên hình ảnh hoặc video chứa phương tiện.
        2. Chọn loại phương tiện muốn nhận diện (nếu có).
        3. Nhấn "Nhận diện" để xem kết quả.
        4. Kết quả sẽ hiển thị loại phương tiện và vị trí trong hình ảnh.
        
        **Lưu ý**: Đảm bảo phương tiện được chụp rõ ràng, không bị che khuất.
        """)

    # Background Removal
    with st.expander("Tách Nền Hình Ảnh"):
        st.write("""
        **Mô tả**: Module tách nền giúp loại bỏ nền khỏi hình ảnh, giữ lại đối tượng chính.
        
        **Công nghệ sử dụng**: U-Net, Remove.bg API, OpenCV.
        
        **Hướng dẫn sử dụng**:
        1. Tải lên hình ảnh cần tách nền.
        2. Chọn chế độ tách nền (tự động hoặc thủ công).
        3. Nhấn "Tách nền" để xử lý.
        4. Tải xuống hình ảnh đã tách nền.
        
        **Lưu ý**: Đối tượng chính cần nổi bật so với nền để đạt kết quả tốt nhất.
        """)

    # Chapters
    with st.expander("Các Chương Dự Án"):
        st.write("""
        **Mô tả**: Dự án được chia thành nhiều chương để tổ chức và phát triển các module một cách có hệ thống.
        
        **Danh sách chương**:
        - **Chương 1**: Thu thập và tiền xử lý dữ liệu.
        - **Chương 2**: Xây dựng mô hình nhận diện khuôn mặt và trái cây.
        - **Chương 3**: Phát triển module nhận diện xe và tách nền.
        - **Chương 4**: Tích hợp và kiểm thử toàn bộ hệ thống.
        - **Chương 5**: Triển khai và tối ưu hóa giao diện người dùng.
        
        **Hướng dẫn sử dụng**:
        1. Truy cập tài liệu dự án để xem chi tiết từng chương.
        2. Sử dụng các module tương ứng với từng chương để kiểm tra chức năng.
        3. Gửi phản hồi nếu phát hiện lỗi hoặc cần cải tiến.
        
        **Lưu ý**: Đọc kỹ tài liệu để hiểu rõ tiến trình phát triển.
        """)

    # Footer
    st.markdown("""
    <div style='text-align: center; margin-top: 20px; color: #7f8c8d;'>
        Được phát triển bởi Phan Văn Quân & Hoàng Mạnh Tường | 2025
    </div>
    """, unsafe_allow_html=True)