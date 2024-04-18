from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def load_image_in_grayscale(path):
    return Image.open(path).convert('L')

# ヒストグラムを表示する関数
def plot_histogram(image, label, ax, color):
    data = np.array(image)
    ax.hist(data.ravel(), bins=256, color=color, alpha=0.5, label=label, range=[0,256])
    ax.legend(loc='upper right')

# 画像のパス
image_path1 = './Lenna.bmp'
image_path2 = './Pepper.bmp'

# 画像を読み込み
image1 = load_image_in_grayscale(image_path1)
image2 = load_image_in_grayscale(image_path2)


fig, ax = plt.subplots(figsize=(10, 6))

plot_histogram(image1, 'Image 1', ax, 'orange')
plot_histogram(image2, 'Image 2', ax, 'blue')

ax.set_title('Brightness Histogram Comparison')
ax.set_xlabel('Pixel Intensity')
ax.set_ylabel('Frequency')

plt.show()
