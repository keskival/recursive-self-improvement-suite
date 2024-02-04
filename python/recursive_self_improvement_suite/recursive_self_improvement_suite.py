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
    session = (
        [
            {
                "role": "system",
                "content": """\
You are a component in a system of training exercises. You answer concisely without pleasantries.
You will produce either JSON responses without Markdown notation, or Python code in Markdown blocks.
""",
            },
        ]
        + list(
            map(
                lambda message: {
                    "role": "user",
                    "content": message,
                },
                messages,
            )
        )
    )
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
    print("Failed calling OpenAI API even with repeated trials!")
    exit(1)


def coding_improvement_iteration():
    # TODO: Just generate one complete iteration from one challenge, and output this as a Dot language diagram
    #       for graphing it with GraphViz to demonstrate one iteration for the documentation.
    challenges_prompt = coding.generate_challenges()
    challenges = json.loads(chat([challenges_prompt]))
    logging.info(f"Challenges: {challenges}")
    challenge_ids = list(map(lambda challenge: challenge["id"], challenges))

    # Let's only pick 5 best challenges out of 10.
    evaluate_challenges_prompt = coding.evaluate_challenges(
        challenges, challenge_ids, 5
    )
    best_n_challenge_ids = json.loads(chat([evaluate_challenges_prompt]))
    logging.info(f"Best n challenge ids: {best_n_challenge_ids}")
    best_n_challenges = [
        next(
            (
                challenge
                for challenge in challenges
                if challenge["id"] == selected_challenge["id"]
            ),
            None,
        )
        for selected_challenge in best_n_challenge_ids
    ]
    logging.info(f"Best n challenges: {best_n_challenges}")

    for challenge in best_n_challenges:
        # For each challenge we want to create a set of evaluation functions, and choose the best one.
        number_of_evaluation_functions = 5
        number_of_rankings = 2
        number_of_evaluation_rankings = 2
        
        evaluation_function_prompt = coding.generate_evaluation_function(challenge)
        evaluation_functions = [
            chat([evaluation_function_prompt])
            for _ in range(number_of_evaluation_functions)
        ]
        logging.info(f"Evaluation_functions: {evaluation_functions}")

        evaluate_evaluation_functions_prompt = coding.evaluate_evaluation_functions(
            challenge["description"],
            [
                {"id": id, "evaluation_function": evaluation_function}
                for id, evaluation_function in enumerate(evaluation_functions)
            ],
            range(len(evaluation_functions)),
        )
        best_evaluation_function_id = json.loads(
            chat([evaluate_evaluation_functions_prompt])
        )
        logging.info(f"Best evaluation function id: {best_evaluation_function_id}")
        best_evaluation_function = evaluation_functions[best_evaluation_function_id["best_evaluation_function_id"]]
        logging.info(f"Best evaluation function: {best_evaluation_function}")

        # Then we generate solutions, using the best evaluation function.
        solution_prompt = coding.generate_solutions(challenge, best_evaluation_function)
        number_of_solutions = 5
        solutions = [chat([solution_prompt]) for _ in range(number_of_solutions)]
        logging.info(f"Solutions: {solutions}")

        evaluate_solutions_prompt = coding.evaluate_solutions(
            challenge, best_evaluation_function, solutions, range(number_of_solutions)
        )
        solution_evaluations = [chat([evaluate_solutions_prompt]) for _ in range(number_of_rankings)]

        # TODO: Run the evaluation functions and add their outputs to the solutions.
        solutions_with_evaluation_function_outputs = solutions
        # TODO: Then we rank evaluations, i.e. rankings.
        ranking_evaluations_prompt = coding.evaluate_solution_ranking(challenge, best_evaluation_function, solutions, solution_evaluations)
        rankings_of_evaluations = [chat([ranking_evaluations_prompt]) for _ in range(number_of_evaluation_rankings)]
        logging.info(f"Rankings_of_evaluations: {rankings_of_evaluations}")

        best_solution_id = json.loads(chat([evaluate_solutions_prompt]))
        logging.info(f"Best_solution_id: {best_solution_id}")
        best_solution = solutions[best_solution_id["sample_solution_id"]]
        logging.info(f"Best_solution: {best_solution}")

        # Then we evaluate the solution rankings.
    # TODO: This is just one prototype iteration. Ultimately, after tuning prompts and all, we aim to collect
    #       the good trajectories and fine-tune the model with those. This will make the model better at the tasks and
    #       also in evaluation of the tasks over each iteration.


if __name__ == "__main__":
    coding_improvement_iteration()
