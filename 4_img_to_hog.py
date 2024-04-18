import cv2
import matplotlib.pyplot as plt
import numpy as np

gray_image = cv2.imread("Lenna.bmp", cv2.IMREAD_GRAYSCALE)

win_size = (64, 64)
block_size = (16, 16)
block_stride = (8, 8)
cell_size = (8, 8)
n_bins = 9

hog = cv2.HOGDescriptor(win_size, block_size, block_stride, cell_size, n_bins)

hog_features = hog.compute(gray_image)

plt.figure()
plt.title("Histogram of HOG features")
plt.xlabel("Bin")
plt.ylabel("Frequency")
plt.hist(hog_features, bins=50, color="blue", range=(0, 0.2))
plt.show()
