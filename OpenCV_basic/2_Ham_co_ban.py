import cv2
import numpy as np

img = cv2.imread('Data/meo.jpg')
# Ảnh đen trắng
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Làm mờ ảnh
# img_blur = cv2.blur(img, (7,7))
img_blur = cv2.GaussianBlur(img, (9,9), 0)
# Dò cạnh
img_canny = cv2.Canny(img, 150, 150)
# Mở rộng dò cạnh
img_dialation = cv2.dilate(img_canny, kernel= np.ones((2,2), np.uint8), iterations= 2)
# Giảm mức độ dò cạnh (erode - xói mòn)
img_erode = cv2.erode(img_dialation, kernel= np.ones((2,2), np.uint8), iterations= 2)

# Hiển thị ảnh
cv2.imshow('Anh goc', img)
cv2.imshow('Anh den trang', img_gray)
cv2.imshow('Anh mo', img_blur)
cv2.imshow('Do canh', img_canny)
cv2.imshow('Mo rong do canh', img_dialation)
cv2.imshow('Erode', img_erode)

cv2.waitKey(0)