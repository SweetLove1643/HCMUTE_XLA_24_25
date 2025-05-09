# Dự Án Nhận Diện và Xử Lý Hình Ảnh

![Banner](https://via.placeholder.com/1200x300.png?text=Dự+Án+Nhận+Diện+và+Xử+Lý+Hình+Ảnh)

## Giới Thiệu

Dự án này được phát triển bởi **Phan Văn Quân** (MSSV: 22110124) và **Hoàng Mạnh Tường** (MSSV: 22110215) nhằm xây dựng một hệ thống tích hợp các module xử lý hình ảnh và nhận diện sử dụng các kỹ thuật học sâu và thị giác máy tính. Dự án bao gồm các chức năng chính như nhận diện khuôn mặt, nhận diện trái cây, nhận diện phương tiện giao thông (xe máy, xe đạp, ô tô), và tách nền hình ảnh.

## Thành Viên Nhóm

- **Phan Văn Quân** (MSSV: 22110124)
  - Vai trò: Phát triển các module nhận diện và tối ưu hóa giao diện người dùng.
- **Hoàng Mạnh Tường** (MSSV: 22110215)
  - Vai trò: Xử lý dữ liệu và tích hợp các thuật toán AI.

## Các Module Dự Án

### 1. Nhận Diện Khuôn Mặt
- **Mô tả**: Module nhận diện khuôn mặt sử dụng các thuật toán học sâu để xác định và nhận diện khuôn mặt trong hình ảnh hoặc video.
- **Công nghệ sử dụng**: OpenCV, TensorFlow, MTCNN.
- **Hướng dẫn sử dụng**:
  1. Tải lên hình ảnh hoặc video chứa khuôn mặt.
  2. Chọn chế độ nhận diện (đơn khuôn mặt hoặc đa khuôn mặt).
  3. Nhấn nút "Nhận diện" để xem kết quả.
  4. Kết quả hiển thị tên và độ chính xác của khuôn mặt.
- **Lưu ý**: Đảm bảo hình ảnh có độ sáng tốt để đạt kết quả tối ưu.

### 2. Nhận Diện Trái Cây
- **Mô tả**: Module nhận diện và phân loại các loại trái cây dựa trên hình ảnh đầu vào.
- **Công nghệ sử dụng**: PyTorch, CNN, Dataset trái cây tùy chỉnh.
- **Hướng dẫn sử dụng**:
  1. Chụp hoặc tải lên hình ảnh trái cây.
  2. Chọn loại mô hình nhận diện (nếu có nhiều mô hình).
  3. Nhấn "Phân loại" để nhận kết quả.
  4. Kết quả hiển thị loại trái cây và độ tin cậy.
- **Lưu ý**: Hình ảnh cần rõ nét và chỉ chứa một loại trái cây chính.

### 3. Nhận Diện Xe
- **Mô tả**: Module nhận diện các loại phương tiện như xe máy, xe đạp, ô tô dựa trên hình ảnh hoặc video.
- **Công nghệ sử dụng**: YOLOv5, OpenCV.
- **Hướng dẫn sử dụng**:
  1. Tải lên hình ảnh hoặc video chứa phương tiện.
  2. Chọn loại phương tiện muốn nhận diện (nếu có).
  3. Nhấn "Nhận diện" để xem kết quả.
  4. Kết quả hiển thị loại phương tiện và vị trí trong hình ảnh.
- **Lưu ý**: Đảm bảo phương tiện được chụp rõ ràng, không bị che khuất.

### 4. Tách Nền Hình Ảnh
- **Mô tả**: Module tách nền giúp loại bỏ nền khỏi hình ảnh, giữ lại đối tượng chính.
- **Công nghệ sử dụng**: U-Net, Remove.bg API, OpenCV.
- **Hướng dẫn sử dụng**:
  1. Tải lên hình ảnh cần tách nền.
  2. Chọn chế độ tách nền (tự động hoặc thủ công).
  3. Nhấn "Tách nền" để xử lý.
  4. Tải xuống hình ảnh đã tách nền.
- **Lưu ý**: Đối tượng chính cần nổi bật so với nền để đạt kết quả tốt nhất.

## Cấu Trúc Dự Án

Dự án được tổ chức thành các chương để phát triển có hệ thống:

- **Chương 1**: Thu thập và tiền xử lý dữ liệu.
- **Chương 2**: Xây dựng mô hình nhận diện khuôn mặt và trái cây.
- **Chương 3**: Phát triển module nhận diện xe và tách nền.
- **Chương 4**: Tích hợp và kiểm thử toàn bộ hệ thống.
- **Chương 5**: Triển khai và tối ưu hóa giao diện người dùng.

## Yêu Cầu Hệ Thống

- **Python**: 3.8 trở lên
- **Thư viện**:
  - OpenCV
  - TensorFlow
  - PyTorch
  - Streamlit
  - NumPy
  - YOLOv5
- **Phần cứng**: GPU được khuyến nghị để tăng tốc độ xử lý.

## Hướng Dẫn Cài Đặt

1. **Sao chép kho mã nguồn**:
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```

2. **Cài đặt môi trường ảo**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Trên Windows: venv\Scripts\activate
   ```

3. **Cài đặt thư viện**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Chạy ứng dụng**:
   ```bash
   streamlit run app.py
   ```

## Giao Diện Người Dùng

Ứng dụng được xây dựng bằng **Streamlit**, cung cấp giao diện trực quan với:
- Sidebar điều khiển các thông số.
- Hiển thị kết quả nhận diện và xử lý hình ảnh theo thời gian thực.
- Hỗ trợ tải lên hình ảnh/video và tải xuống kết quả.

## Đóng Góp

Chúng tôi hoan nghênh mọi đóng góp! Để đóng góp:
1. Fork kho mã nguồn.
2. Tạo nhánh mới (`git checkout -b feature/ten-chuc-nang`).
3. Commit thay đổi (`git commit -m 'Thêm chức năng XYZ'`).
4. Push lên nhánh (`git push origin feature/ten-chuc-nang`).
5. Tạo Pull Request.

## Giấy Phép

Dự án được phát hành theo [Giấy phép MIT](LICENSE).

## Liên Hệ

- **Phan Văn Quân**: [quanpv22110124@example.com](mailto:quanpv22110124@example.com)
- **Hoàng Mạnh Tường**: [tuonghm22110215@example.com](mailto:tuonghm22110215@example.com)

---

**Được phát triển bởi Phan Văn Quân & Hoàng Mạnh Tường | 2025**
