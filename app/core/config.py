import os

from pydantic import BaseModel


class Config(BaseModel):
    base_dir: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
    api_key: str = os.getenv("API_KEY", "")


config = Config()

