import os

import openai
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


openai.api_key = os.environ["OPENAI_API_KEY"]


def get_reply(text: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": text},
        ],
    )

    return response.choices[0].message.content
