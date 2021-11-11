# Phần 1: OpenCv_Basic

## 1. Load ảnh, video, webcam
 - 1.1. Load ảnh [click here](https://github.com/thien1892/OpenCv_Python/blob/main/OpenCV_basic/C1_1_load_img.py)
 - 1.2. Load video [click here](https://github.com/thien1892/OpenCv_Python/blob/main/OpenCV_basic/C1_2_load_video.py)
 - 1.3. Load webcam/camera [click here](https://github.com/thien1892/OpenCv_Python/blob/main/OpenCV_basic/C1_3_load_webcam.py)

## 2. Một số hàm cơ bản [click here](https://github.com/thien1892/OpenCv_Python/blob/main/OpenCV_basic/C2_Ham_co_ban.py)
 - 2.1. Chuyển đen trắng
 - 2.2. Làm mờ ảnh
 - 2.3. Detect cạnh
 - 2.4. Mở rộng detect cạnh
 - 2.5. Thu hẹp detect cạnh

## 3. Thay đổi kích thước và cắt ảnh [click here](https://github.com/thien1892/OpenCv_Python/blob/main/OpenCV_basic/C3_Resize_and_crop_img.py)

- Ta xem các tọa độ của ảnh trong open cv:
<img src = 'https://i.imgur.com/IGD7TwR.jpg'>

 - 3.1. Resize ảnh
 - 3.2. Cắt ảnh

## 4. Hình vẽ và text [click here](https://github.com/thien1892/OpenCv_Python/blob/main/OpenCV_basic/C4_Shape_text.py)
 - 4.1. Vẽ đường thẳng
 - 4.2. Vẽ hình chữ nhật
 - 4.3. Vẽ hình tròn
 - 4.4. Thêm text

## 5. Warping perspective (Bẻ cong phối cảnh ~~~ không biết nên dịch ra sao) [click here](https://github.com/thien1892/OpenCv_Python/blob/main/OpenCV_basic/C5_warping_perspective.py)

## 6. Join nhiều ảnh [click here](https://github.com/thien1892/OpenCv_Python/blob/main/OpenCV_basic/C6_join_img.py)

## 7. Phát hiện màu sắc (Colour Detection) [click here](https://github.com/thien1892/OpenCv_Python/blob/main/OpenCV_basic/C7_detect_color.py)

## 8. Phát hiện đường viền và hình dạng (Contouring and shape detection) [click here](https://github.com/thien1892/OpenCv_Python/blob/main/OpenCV_basic/C8_Contouring_shape_detection.py)

## 9. Detech khuôn mặt

# Phần 2: OpenCV_projects

## 1. Scan tài liệu [source code here](https://github.com/thien1892/OpenCv_Python/blob/main/OpenCV_project/P1_scan_documents.py)
- Bước 1: Read webcam/ image
- Bước 2: Xử lý ảnh về dò cạnh
- Bước 3: Từ bức ảnh dò cạnh, ta dò đường bao (contour):
    - Lấy vùng có số cạnh == 4
    - Lấy vùng có diện tích lớn nhất
- Bước 4: Sau bước 3, ta xác định được tọa độ 4 góc cần lấy của khung hình. Ta sử dụng warp perspective để chuyển khung hình về kích thước ta cần chọn.

## 2. Xác định vật thể/ người qua webcam/ video/ image bằng Yolo [source code here](https://github.com/thien1892/OpenCv_Python/blob/main/OpenCV_project/P2_track_yolo.py) [code yolo here](https://github.com/thien1892/OpenCv_Python/blob/main/OpenCV_project/yolo3.py)
- Sử dụng model yolov3 416
- Load pre-trained model: [click here](https://drive.google.com/file/d/1bhTkqX_I-JU7zGCi0owRTmfdw0QW-z15/view?usp=sharing)
- Lựa chọn label theo ý thích, mặc định mô hình có 80 label, bạn có thể chọn label tùy ý trong 80 label này ví dụ, chỉ chọn tracking người, ô tô, xe máy, ta chọn labels = ["person","car","motorbike"]
- Lựa chọn class_threshold để tạo bộ lọc kết quả đầu ra, mặc định 0.6, càng thấp thì bộ lọc càng ít.
- Dùng Open-CV để mở webcam/ camera IP /video của bạn và enjoy!!!