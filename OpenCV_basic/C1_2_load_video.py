import cv2
################################
frameHeight = 480 # Chieu cao
frameWidth = 640 # Chieu rong
################################

# Đoc file video từ đường dẫn
cap = cv2.VideoCapture('Data/test_video.mp4')
# Hiển thị video
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow('Read Video', img)
    # Bam phim 'q' thi thoat
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break