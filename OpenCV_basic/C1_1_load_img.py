import cv2

# Đọc file ảnh từ đường dẫn
img = cv2.imread('Data/meo.jpg')
# Hiển thị hình ảnh
cv2.imshow('Meo con', img)
cv2.waitKey(0)