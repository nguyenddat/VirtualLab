from app.core.llm import client
from app.utils.chatbot_utils.chain import get_chat_completion
from app.utils.text2image_utils.prompts import create_tool

def create_image(params: dict):
    response = get_chat_completion(task="extract_tool", params=params)["response"]
    response = client.images.generate(
        model="dall-e-3",
        prompt=create_tool.prompt.format(question = response),
        n=1,
        size="1024x1024",
        response_format="b64_json"
    )
    return response.data[0].b64_json