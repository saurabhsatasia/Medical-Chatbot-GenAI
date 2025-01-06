# app/config/settings.py
import os
from pathlib import Path
from dotenv import load_dotenv

# Get the absolute path to the .env file
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = BASE_DIR / '.env'

print(f"Looking for .env at: {ENV_FILE}")
print(f"File exists: {ENV_FILE.exists()}")

# Load the .env file
loaded = load_dotenv(ENV_FILE)
print(f"Load_dotenv result: {loaded}")


class Settings:
    def __init__(self):
        self.PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
        print(f"API Key found in env: {'Yes' if self.PINECONE_API_KEY else 'No'}")

        if not self.PINECONE_API_KEY:
            raise ValueError("PINECONE_API_KEY not found in environment variables")

        self.MODEL_PATH: str = str(BASE_DIR / 'model' / 'llama-2-7b-chat.ggmlv3.q4_0.bin')
        self.MODEL_TYPE: str = "llama"
        self.EMBEDDINGS_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
        self.INDEX_NAME: str = "medibot"
        self.DATA_PATH: str = "../data/"


settings = Settings()