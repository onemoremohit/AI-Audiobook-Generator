from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

responce = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What Einstein was doing during his last years of life?"
)

print(responce.text)
