import os
from PIL import Image

def batch_resize_images_to_png(input_dir, output_dir, size=(64, 64)):
    valid_exts = ('.png', '.jpg', '.jpeg', '.bmp', '.webp')
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(valid_exts):
            input_path = os.path.join(input_dir, filename)
            name, _ = os.path.splitext(filename)
            output_path = os.path.join(output_dir, name + ".png")

            try:
                img = Image.open(input_path).convert("RGB")
                img_resized = img.resize(size, Image.LANCZOS)
                img_resized.save(output_path)
                print(f"已保存: {output_path}")
            except Exception as e:
                print(f"处理失败 {filename}: {e}")

# 使用示例
batch_resize_images_to_png("/root/autodl-tmp/ControlNet-main/Chars74K_Style/train/ContentImage", "/root/autodl-tmp/ControlNet-main/Chars74K_Style/train/ContentImage64", size=(64, 64))
