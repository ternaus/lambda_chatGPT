import asyncio
import json
import logging
import sys
import time
import os

import httpx
from dotenv import load_dotenv

from src.generate_response import get_reply

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout),
    ],
)

load_dotenv()  # take environment variables from .env.

# headers = {"content-type": "application/json", "x-api-key": "SsOMsVn7HqmbLKxT0XsbaG54KxOsDyX3Y81NdUFd"}

# URL = "https://m5xr1yc3ef.execute-api.us-east-1.amazonaws.com/dev/"

# start_time = time.time()


# async def request():
#     async with httpx.AsyncClient(headers=headers, timeout=60000000000) as client:
#         result = await client.post(URL, data=json.dumps({"email": "iglovikov@gmail.com", "type": "get"}))
#         return result.json()


# base64result = asyncio.run(request())
# logging.info(base64result)

# headers = {
#     "content-type": "application/json",
#     "Authorization": f'Bearer {os.environ["OPENAI_API_KEY"]}',
#     "OpenAI-Organization": os.environ["OPENAI_OGRANIZATION"],
# }

# response = httpx.post(
#     "https://api.openai.com/v1/completions",
#     headers=headers,
#     data=json.dumps({"model": "text-davinci-003", "prompt": "Say this is a test", "temperature": 0, "max_tokens": 7}),
# )

# print(response.json())

input_email = """
Hey Vladimir! Thank you for reaching out to my services. I saw the video demo of the Chrome extension. I am glad to say that I can copy that kind of extension. :)
I can offer you the advanced tier of this project if you have the budget for this.
"""

print(get_reply(input_email))
