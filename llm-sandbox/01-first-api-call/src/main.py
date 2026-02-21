import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
print(client)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="What approach does binary search uses?"
)
print(response.text)