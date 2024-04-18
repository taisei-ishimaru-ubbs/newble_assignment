import cv2
import numpy as np

# 画像の読み込み
image_path = 'dog.jpg'
img = cv2.imread(image_path)

# 画像の表示
cv2.imshow('Original Image', img)
cv2.waitKey(0)

# リサイズ：画像を半分のサイズに縮小
resized_img = cv2.resize(img, None, fx=2, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(0)

# 回転：画像を90度回転
rows, cols = img.shape[:2]
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
rotated_img = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('Rotated Image', rotated_img)
cv2.waitKey(0)

# 二値化：閾値を設定して二値化
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Image', binary_img)
cv2.waitKey(0)

# すべてのウィンドウを閉じる
cv2.destroyAllWindows()
