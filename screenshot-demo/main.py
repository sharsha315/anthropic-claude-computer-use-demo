import os
import anthropic
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Create an Claude instance

client = anthropic.Anthropic(
    api_key=ANTHROPIC_API_KEY,
)

# message = client.messages.create(
#     model="claude-3-5-sonnet-20241022",
#     max_tokens=1024,
#     messages=[
#         {"role": "user", "content": "Hello, Claude"}
#     ]
# )
# print(message.content)


