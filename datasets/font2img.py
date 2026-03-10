import os
from font2data.FontData import FontData


if __name__ == "__main__":
    
    with open("data/common_chars.txt", "r", encoding="utf-8") as f:
        text = f.read()
        # 去掉空白與換行，再拆成單個字
        common_chars = list(text.replace(" ", "").replace("\n", "").strip())
        # 如需去重，可保留下一行，否則刪掉
        common_chars = list(set(common_chars))
        print(common_chars)

    for folder in os.listdir("data"):
        if os.path.isdir(f"data/{folder}"):
            images_folder = f"fonts/{folder}"
            os.makedirs(images_folder, exist_ok=True)
            for font in os.listdir(f"data/{folder}"):
                print(f"{folder} Processing font: ", font)
                font_filename = font.split(".")[0]
                font_image_folder = f"{images_folder}/{font_filename}"
                os.makedirs(font_image_folder, exist_ok=True)
                font_data = FontData(f"data/{folder}/{font}", font_size=256)
                for char in common_chars:
                    image = font_data.char2img(char)
                    if image is not None:
                        image = image.convert("L")
                        # 使用 Unicode 碼點 (hex) 當檔名，避免 Windows 中文檔名編碼問題
                        hex_name = f"{ord(char):04X}.png"
                        image.save(os.path.join(font_image_folder, hex_name))
