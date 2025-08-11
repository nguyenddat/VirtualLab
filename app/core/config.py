import os

from pydantic import BaseModel


class Config(BaseModel):
    base_dir: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
    api_key: str = os.getenv("API_KEY", "")

    database_url: str = os.getenv("DATABASE_URL",  "")

config = Config()

