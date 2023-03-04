import asyncio
import json
import logging
import sys

import httpx
from dotenv import load_dotenv

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
Hey Vladimir! Thank you for reaching out to my services.
I saw the video demo of the Chrome extension. I am glad to say that I can copy that kind of extension. :)
I can offer you the advanced tier of this project if you have the budget for this.
"""


request_text = f"""
Respond to the most recent email in a comprehensive and professional tone and sign off with my name at the end

---

{input_email}
"""


async def request():
    async with httpx.AsyncClient(headers=headers, timeout=60000000000) as client:
        result = await client.post(URL, data=json.dumps({"action": "reply", "text": input_email}))
        print(result.headers)
        return result.json()


result = asyncio.run(request())
logging.info(result)
