"""Main module."""

import openai
import json
import time

with open("apikey.json", "r") as apikey_file:
    config = json.load(apikey_file)
    openai.api_key = config["apikey"]
    openai.organization = config["org"]
    model = config["model"]


def chat(messages):
    while trials < 5:
        try:
            completion = openai.ChatCompletion.create(
                model=model, messages=messages, max_tokens=2, temperature=0.1
            )
            print(completion)
        except Exception as e:
            print(e)
            time.sleep(10)
            trials = trials + 1
            # Open AI rate limit of one request per second, 60 / minute.
            time.sleep(2)
    return completion


prompt = [
    {
        "role": "system",
        "content": """\
""",
    },
    {
        "role": "user",
        "content": """"\
""",
    },
]
