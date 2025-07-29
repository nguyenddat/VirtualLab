import os
import base64
from io import BytesIO

from PIL import Image
from rembg import remove

def remove_background_from_base64(base64_str: str) -> str:
    image_data = base64.b64decode(base64_str)
    input_image = Image.open(BytesIO(image_data)).convert("RGBA")

    # Tách nền
    output_image = remove(input_image)

    # Chuyển ảnh kết quả thành base64
    buffer = BytesIO()
    output_image.save(buffer, format="PNG")
    output_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return output_base64


def save_from_base64(base64_str: str):
    image_data = base64.b64decode(base64_str)
    image_io = BytesIO(image_data)
    image_pil = Image.open(image_io)

    # Lưu vào file PNG
    output_path = "removed_background.png"
    image_pil.save(output_path, format="PNG")

    return output_path