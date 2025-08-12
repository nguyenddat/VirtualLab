from app.utils.text2image_utils.chain import create_image
from app.utils.remove_background import remove_background_from_base64, save_from_base64

def create_tool(params: dict):
    response = create_image(params=params)
    removed_bg_image = remove_background_from_base64(response)
    save_from_base64(removed_bg_image)