import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper

# Khởi tạo OpenAI client với API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Khởi tạo OpenAI client một cách an toàn
try:
    client = OpenAI(api_key=openai_api_key) if openai_api_key else None
except Exception as e:
    print(f"Warning: Could not initialize OpenAI client: {e}")
    client = None

# Khởi tạo LangChain LLM
try:
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=openai_api_key
    ) if openai_api_key else None
except Exception as e:
    print(f"Warning: Could not initialize LangChain LLM: {e}")
    llm = None

# Khởi tạo DALL-E wrapper
try:
    text2img = DallEAPIWrapper(
        n=1,
        size="512x512"
    ) if openai_api_key else None
except Exception as e:
    print(f"Warning: Could not initialize DALL-E wrapper: {e}")
    text2img = None