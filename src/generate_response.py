import os

import httpx
import ujson as json
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


headers = {
    "content-type": "application/json",
    "Authorization": f'Bearer {os.environ["OPENAI_API_KEY"]}',
    "OpenAI-Organization": os.environ["OPENAI_OGRANIZATION"],
}


def get_reply(text: str) -> str:
    request_text = f"""
    Generate a reply for a given email:

    ---
    {text}
    """

    response = httpx.post(
        "https://api.openai.com/v1/completions",
        headers=headers,
        data=json.dumps({"model": "text-davinci-003", "prompt": request_text, "temperature": 0, "max_tokens": 3900}),
    )

    return response.json()["choices"][0]["text"]
