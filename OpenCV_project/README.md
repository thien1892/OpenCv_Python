# OpenCV_projects

## 1. Scan tài liệu [source code here](https://github.com/thien1892/OpenCv_Python/blob/main/OpenCV_project/P1_scan_documents.py)
- Bước 1: Read webcam/ image
- Bước 2: Xử lý ảnh về dò cạnh
- Bước 3: Từ bức ảnh dò cạnh, ta dò đường bao (contour):
    - Lấy vùng có số cạnh == 4
    - Lấy vùng có diện tích lớn nhất
- Bước 4: Sau bước 3, ta xác định được tọa độ 4 góc cần lấy của khung hình. Ta sử dụng warp perspective để chuyển khung hình về kích thước ta cần chọn.

## 2. Xác định vật thể/ người qua webcam/ video/ image bằng Yolo [source code here](https://github.com/thien1892/OpenCv_Python/blob/main/OpenCV_project/P2_track_yolo.py)

<img src = 'https://i.imgur.com/IE1qpMN.jpg'>
- Sử dụng model yolov3 416
- Load pre-trained model: [click here](https://drive.google.com/file/d/1bhTkqX_I-JU7zGCi0owRTmfdw0QW-z15/view?usp=sharing)
- Lựa chọn label theo ý thích, mặc định mô hình có 80 label, bạn có thể chọn label tùy ý trong 80 label này ví dụ, chỉ chọn tracking người, ô tô, xe máy, ta chọn labels = ["person","car","motorbike"]
- Lựa chọn class_threshold để tạo bộ lọc kết quả đầu ra, mặc định 0.6, càng thấp thì bộ lọc càng ít.
- Dùng Open-CV để mở webcam/ camera IP /video của bạn và enjoy!!!
- [code yolo here](https://github.com/thien1892/OpenCv_Python/blob/main/OpenCV_project/yolo3.py)