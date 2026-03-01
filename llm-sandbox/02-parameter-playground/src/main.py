import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

PROMPT = "Write a one-sentence haiku about coding."
MODEL = "gemini-3-flash-preview"


def generate_with_temperature(temperature: float) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=PROMPT,
        config=types.GenerateContentConfig(temperature=temperature,top_p=0.95),
    )
    return response.text or ""

print(generate_with_temperature(0.2))

# if __name__ == "__main__":
#     for temp in (t / 10.0 for t in range(20, 21)):
#         print(f"\n--- Temperature {temp} ---")
#         print(generate_with_temperature(temp))