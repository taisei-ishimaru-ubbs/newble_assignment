from PIL import Image, ImageOps

# 画像を二値化する
def binarize_image(image, threshold=128):
    # グレースケールに変換
    image = image.convert('L')
    # 二値化処理
    return image.point(lambda x: 255 if x > threshold else 0, '1')

# 使用例
if __name__ == "__main__":
    # 画像を読み込む
    img = Image.open('./dog.jpg')
    
    # 画像を表示する
    img.show()
    
    # 画像を縮小する
    resized_img = img.resize((300, 400))
    resized_img.show()
    
    # 画像を90度回転する
    rotated_img = img.rotate(90)
    rotated_img.show()
    
    # 画像を二値化する
    binarized_img = binarize_image(img)
    binarized_img.show()
