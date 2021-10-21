import cv2
import numpy as np

img = np.zeros((480,640,3), np.uint8)

#Vẽ đường thảng
cv2.line(img, (0,0), (img.shape[1] // 2, img.shape[0] // 2), (255,0,0), 5)
# Vẽ hình chữ nhật
cv2.rectangle(img, (50,50), (600,400), (0,255,0), 4)
# Vẽ hình tròn
cv2.circle(img, (img.shape[1] // 2, img.shape[0] //2), 100, (0,0,255), 3)
# Thêm text
cv2.putText(img, 'Tran Van Thien', (img.shape[1] // 2, img.shape[0] //2), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0), 3)

# Hiển thị ảnh
cv2.imshow('Ket qua', img)
cv2.waitKey(0)