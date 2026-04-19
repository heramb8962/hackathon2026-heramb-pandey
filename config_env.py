from dotenv import load_dotenv
import os

# force load .env
load_dotenv()

def get_api_key():
    key = os.getenv("OPENAIAPI_KEY")
    print("DEBUG API KEY:", key)  # temporary debug
    return key