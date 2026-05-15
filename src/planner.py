# Claude API calls
from anthropic import Anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)  # read ANTHROPIC_API_KEY from .env

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=256,
    messages=[
        {"role": "user", "content": "Say hello."}
    ]
)

print(response.content[0].text)