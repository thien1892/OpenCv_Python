import cv2
import numpy as np

##################################
width, height = 250, 300
##################################
img = cv2.imread('Data/cards.jpg')
# Lấy tọa độ 4 góc của lá bài trong bức ảnh
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
# Lấy tọa độ 4 góc của khung hình ta mong muốn kéo dãn ảnh đã lấy trên
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# Lấy ảnh ở 4 tọa độ pt1, tạo ra ảnh có 4 góc như pts2 từ ảnh gốc img
matrix = cv2.getPerspectiveTransform(pts1, pts2)
img_output = cv2.warpPerspective(img, matrix, (width, height))

# Hiển thị ảnh
print(img.shape)
cv2.imshow('Anh goc', img)
cv2.imshow('Ket qua', img_output)
cv2.waitKey(0)