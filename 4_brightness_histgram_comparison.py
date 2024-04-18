from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

def load_image_in_grayscale(path):
    return Image.open(path).convert('L')

def plot_histogram(image, label, ax, color):
    data = np.array(image)
    ax.hist(data.ravel(), bins=256, color=color, alpha=0.5, label=label, range=[0,256])
    ax.legend(loc='upper right')

image_path1 = './Lenna.bmp'
image_path2 = './Pepper.bmp'

image1 = load_image_in_grayscale(image_path1)
image2 = load_image_in_grayscale(image_path2)

font_path = '/usr/share/fonts/truetype/migmix/migmix-2m-bold.ttf'
font_prop = FontProperties(fname=font_path)
plt.rcParams["font.family"] = font_prop.get_name()

plt.rcParams.update({'font.size': 16})

fig, ax = plt.subplots(figsize=(10, 6))

plot_histogram(image1, 'Lenna', ax, 'orange')
plot_histogram(image2, 'Pepper', ax, 'blue')

ax.set_title('輝度ヒストグラムの比較')
ax.set_xlabel('ピクセル強度')
ax.set_ylabel('頻度')


plt.savefig('histogram_comparison.pdf')

plt.show()
