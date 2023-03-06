import os

import ujson as json
from dotenv import load_dotenv
from mixpanel import Mixpanel

from src.generate_response import get_reply

headers = {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Methods": "OPTIONS,POST"}

load_dotenv()  # take environment variables from .env.

mp = Mixpanel(os.environ["MIXPANEL_TOKEN"])


def lambda_handler(event, context=None):
    if event.get("source") == "serverless-plugin-warmup":
        return {}

    if "body" not in event:
        return {"statusCode": 400, "headers": headers}

    body = json.loads(event["body"])

    if "action" not in body:
        return {"statusCode": 400, "headers": headers}

    action = body["action"]

    if action == "reply":
        response = get_reply(body["text"])
        distinct_id = body.get("metadata", {}).get("distinct_id", "unknown")
        mp.track(distinct_id, {"action": "reply", **body.get("metadata", {})})

    return {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps({"response": response}),
    }
