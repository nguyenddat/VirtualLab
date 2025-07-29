from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper

client = OpenAI()
llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)
text2img = DallEAPIWrapper(
    n=1,
    size="512x512"  # Không dùng "quality"
)