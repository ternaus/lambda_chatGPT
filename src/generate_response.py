import os

import httpx
import openai
import ujson as json
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


headers = {
    "content-type": "application/json",
    "Authorization": f'Bearer {os.environ["OPENAI_API_KEY"]}',
    "OpenAI-Organization": os.environ["OPENAI_OGRANIZATION"],
}


def get_reply(text: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": text},
        ],
    )
    response = httpx.post(
        "https://api.openai.com/v1/completions",
        headers=headers,
        data=json.dumps({"model": "gpt-3.5-turbo", "prompt": text, "temperature": 0, "max_tokens": 3900}),
    )

    return response.choices[0].message.content
