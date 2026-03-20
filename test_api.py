from google import genai
import os

client = genai.Client(api_key="API_KEY")

responce = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Why is the sky blue?"
)

print(responce.text)
