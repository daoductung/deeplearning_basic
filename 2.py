import cv2
import os

PATH_DATASET = os.getcwd() + '\\dataset'

img_path = PATH_DATASET + '\\image.png'
img = cv2.imread(img_path)
height, width = img.shape[:2]
x = 0
y = 0
# Cắt góc phần tư thứ nhất của ảnh
crop = img[x:x + height // 2, y:y + width // 2]
cv2.imshow('Crop image', crop)

# Resize ảnh thành 1/2 chiều dài và rộng
dim = (width // 2, height // 2)
resized = cv2.resize(img, dim)
cv2.imshow("Resized image", resized)

# Thực hiện Gaussian blur ảnh
blur = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("GaussianBlur image", blur)

# Phát hiện edge trong ảnh.
edges = cv2.Canny(img, height, width)
cv2.imshow("Edges image", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()