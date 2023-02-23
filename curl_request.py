import asyncio
import json
import logging
import os
import sys
import time

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

headers = {"content-type": "application/json", "x-api-key": "0Xm4ZJBA4D2DQi763h46S5CmhtfLn6yma3VKRYKQ"}

URL = "https://2pr6s20k4b.execute-api.us-east-1.amazonaws.com/dev/"

input_email = """
Hey Vladimir! Thank you for reaching out to my services. I saw the video demo of the Chrome extension. I am glad to say that I can copy that kind of extension. :)
I can offer you the advanced tier of this project if you have the budget for this.
"""


async def request():
    async with httpx.AsyncClient(headers=headers, timeout=60000000000) as client:
        result = await client.post(URL, data=json.dumps({"action": "reply", "text": input_email}))
        return result.json()


result = asyncio.run(request())
logging.info(result)
