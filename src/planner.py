# Claude API calls
import anthropic
import os

client = anthropic.Anthropic()  # automatically reads ANTHROPIC_API_KEY from .env

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=256,
    messages=[{"role": "user", "content": "Say hello."}]
)
print(message.content[0].text)