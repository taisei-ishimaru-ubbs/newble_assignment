import cv2

# 画像の読み込み
image_path = './Lenna.bmp'
img = cv2.imread(image_path)

resized_img = cv2.resize(img, None, fx=1, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imwrite('resized_lenna.bmp', resized_img)

rows, cols = img.shape[:2]
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
rotated_img = cv2.warpAffine(img, M, (cols, rows))
cv2.imwrite('rotated_lenna.bmp', rotated_img)

# 二値化：閾値を設定して二値化
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('binary_lenna.bmp', binary_img)