"""Main module."""

import json
import logging
from openai import OpenAI
import time

from . import coding

with open("apikey.json", "r") as apikey_file:
    config = json.load(apikey_file)
    client = OpenAI(
        api_key=config["apikey"],
        organization=config["org"],
    )
    model = config["model"]

logging.basicConfig(level=logging.DEBUG)

def chat(messages):
    session = [
        {
            "role": "system",
            "content": """\
You are a component in a system of training exercises. You answer concisely without pleasantries or Markdown notation.
""",
        },
    ] + list(map(lambda message: {
            "role": "user",
            "content": message,
        }, messages))
    trials = 0
    while trials < 5:
        try:
            
            completion = client.chat.completions.create(
                model=model, messages=session, temperature=0.1
            )
            logging.debug(f"Request: {session}, completion: {completion}")
            return completion.choices[0].message.content
        except Exception as e:
            print(e)
            time.sleep(10)
            trials = trials + 1
            # Open AI rate limit of one request per second, 60 / minute.
            time.sleep(2)

def coding_improvement_iteration():
    challenges_prompt = coding.generate_challenges()
    challenges = chat([challenges_prompt])
    logging.info(f"Challenges: {challenges}")
    evaluation_functions_prompts = list(map(lambda challenge: coding.generate_evaluation_functions(challenge), challenges))
    logging.info(f"Evaluation_functions_prompts: {evaluation_functions_prompts}")
    solutions_prompts = list(map(lambda challenge: coding.generate_solutions(challenge, "TODO"), challenges))
    logging.info(f"Solutions_prompts: {solutions_prompts}")

if __name__ == "__main__":
    coding_improvement_iteration()
