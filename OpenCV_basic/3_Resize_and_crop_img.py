import cv2

img = cv2.imread('Data/meo.jpg')
print(img.shape) # in kích thước ảnh img
# Thay đổi kích thước ảnh
img_resize = cv2.resize(img, (300, 300))
print(img_resize.shape) # in kích thước ảnh resize
# Cắt ảnh
img_cropped = img[0:300, 200:500]

# Hiển thị ảnh
cv2.imshow('Meo con', img)
cv2.imshow('Resize', img_resize)
cv2.imshow('Cropped', img_cropped)
cv2.waitKey(0)