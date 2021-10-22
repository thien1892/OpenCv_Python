import cv2
################################
frameHeight = 480 # Chieu cao
frameWidth = 640 # Chieu rong
################################

# Đoc webcam từ nguồn, hoặc ip, ...
cap = cv2.VideoCapture(0)
# Set chiều cao, chiều rộng, mức độ sáng, ....
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)
# Hiển thị video
while True:
    success, img = cap.read()
    cv2.imshow('Read Webcam', img)
    # Bam phim 'q' thi thoat
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break