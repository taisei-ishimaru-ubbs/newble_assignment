from PIL import Image, ImageChops, ImageOps

# 画像を読み込む
def load_image(path):
    return Image.open(path)

# 差分画像を生成する
def create_difference_image(image1_path, image2_path):
    # 画像を読み込む
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)
    
    # ２つの画像の差分を取る
    diff = ImageChops.difference(img1, img2)
    
    if diff.mode == "RGBA":
        # 透過情報を削除
        diff = diff.convert("RGB")
    
    # 差分画像を明るくして見やすくする
    diff = ImageOps.autocontrast(diff)
    
    # 差分画像を表示する
    diff.show()
    
    # 差分画像を保存する（必要に応じて）
    diff.save('difference_image.png')

# 使用例
if __name__ == "__main__":
    # ２つの画像のパスを指定
    image1_path = './chrome.png'
    image2_path = './chrome_aaa.png'
    
    # 差分画像を生成
    create_difference_image(image1_path, image2_path)
