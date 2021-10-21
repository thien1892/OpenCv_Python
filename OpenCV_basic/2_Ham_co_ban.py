import cv2

img = cv2.imread('Data/meo.jpg')
# Ảnh đen trắng
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Lam mờ ảnh
# img_blur = cv2.blur(img, (7,7))
img_blur = cv2.GaussianBlur(img, (9,9), 0)
# Dò cạnh
img_canny = cv2.Canny(img, 100, 100)

# Hiển thị ảnh
cv2.imshow('Anh goc', img)
cv2.imshow('Anh den trang', img_gray)
cv2.imshow('Anh mo', img_blur)
cv2.imshow('Do canh', img_canny)

cv2.waitKey(0)