import ujson as json
from dotenv import load_dotenv

from src.generate_response import get_reply

headers = {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Methods": "OPTIONS,POST"}

load_dotenv()  # take environment variables from .env.


def lambda_handler(event, context=None):
    if event.get("source") == "serverless-plugin-warmup":
        return {}

    if "body" not in event:
        return {"statusCode": 400, "headers": headers}

    body = json.loads(event["body"])

    if "action" not in body:
        return {"statusCode": 400, "headers": headers}

    if body["action"] == "reply":
        response = get_reply(body["text"])

    return {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps({"response": response}),
    }
