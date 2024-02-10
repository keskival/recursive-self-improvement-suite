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
                model=model, messages=session, temperature=0.2
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

    # We generate challenges, evaluation functions and solutions. Multiple response candidates.
    # Then we rank challenges, evaluation functions and solutions. Multiple ranking candidates.
    # Then we rank rankings of challeges, evaluation functions and solutions. Single rankings of rankings only.
    
    # We will typically choose the best challenge, evaluation function and solution in this order.
    # In order to do that, we need to produce multiple rankings for each, and then select the best ranking for each.
    # Only after selecting the best ranking, we can use that to select the best challenge, the best evaluation function and the best solution.

    # TODO: If you put 1 here, the bot will not generate a list. Handle this case as well with permissive JSON list parsing.
    number_of_best_challenges = 2

    challenges_prompt = coding.generate_challenges()
    challenges = json.loads(chat([challenges_prompt]))
    logging.info(f"Challenges: {challenges}")
    challenge_ids = list(map(lambda challenge: challenge["id"], challenges))

    evaluate_challenges_prompt = coding.evaluate_challenges(
        challenges, challenge_ids, number_of_best_challenges
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
    # We now have the best n challenges: Let's use those!

    for challenge in best_n_challenges:
        # For each challenge we want to create a set of evaluation functions, and choose the best one.
        number_of_solutions = 5
        number_of_evaluation_functions = 5
        number_of_solution_rankings = 2
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
        evaluation_function_rankings = [json.loads(
            chat([evaluate_evaluation_functions_prompt])
        ) for _ in range(number_of_evaluation_rankings)]
        
        evaluate_evaluation_function_rankings = coding.evaluate_evaluation_function_ranking(
            challenge, evaluation_functions,
            [
                {"id": id, "evaluation_function_ranking": evaluation_function_ranking}
                for id, evaluation_function_ranking in enumerate(evaluation_function_rankings)
            ],
            range(number_of_evaluation_rankings))
        best_evaluation_function_ranking = json.loads(chat([evaluate_evaluation_function_rankings]))
        # We now have the best evaluation function ranking: Let's use it!
        logging.info(f"Best evaluation function ranking: {best_evaluation_function_ranking}")
        best_evaluation_function_id = best_evaluation_function_ranking["best_ranking_id"]

        logging.info(f"Best evaluation function id: {best_evaluation_function_id}")
        best_evaluation_function = evaluation_functions[best_evaluation_function_id]
        logging.info(f"Best evaluation function: {best_evaluation_function}")
        
        # We now have the best evaluation function for this challenge: Let's use it!

        # Then we generate solutions, using the best evaluation function.
        solution_prompt = coding.generate_solutions(challenge, best_evaluation_function)
        solutions = [chat([solution_prompt]) for _ in range(number_of_solutions)]
        logging.info(f"Solutions: {solutions}")

        # TODO: Run the evaluation functions and add their outputs to the solutions.
        solutions_with_evaluation_function_outputs = solutions

        evaluate_solutions_prompt = coding.evaluate_solutions(
            challenge, best_evaluation_function, solutions_with_evaluation_function_outputs, range(number_of_solutions)
        )
        solution_evaluations = [json.loads(chat([evaluate_solutions_prompt])) for _ in range(number_of_solution_rankings)]

        # Then we rank solution rankings.
        ranking_evaluations_prompt = coding.evaluate_solution_ranking(
            challenge, best_evaluation_function, solutions_with_evaluation_function_outputs,
            [
                {"id": id, "solution_evaluation": solution_evaluation}
                for id, solution_evaluation in enumerate(solution_evaluations)
            ],
            range(number_of_solution_rankings))
        # TODO: The bot actually tends to rank the solutions, not the rankings here. Tune the prompt.
        ranking_of_solution_evaluations = json.loads(chat([ranking_evaluations_prompt]))
        
        logging.info(f"Ranking_of_solution_evaluations: {ranking_of_solution_evaluations}")
        best_solution_ranking_id = ranking_of_solution_evaluations["ranking_id"]
        logging.info(f"Best_solution_ranking_id: {best_solution_ranking_id}")
        best_solution_ranking = solution_evaluations[best_solution_ranking_id["sample_solution_ranking_id"]]
        logging.info(f"Best_solution_ranking: {best_solution_ranking}")
        # We now have the best solution ranking: Let's use that!

        best_solution_id = solutions[best_solution_ranking]
        logging.info(f"Best_solution_id: {best_solution_id}")
        best_solution = solutions[best_solution_id["sample_solution_id"]]
        logging.info(f"Best_solution: {best_solution}")
        
        # TODO: Actually run all the evaluation functions for the best solution here.
        evaluation_function_outputs_for_the_best_solution = solution_evaluations
        ranking_evaluation_functions_prompt = coding.evaluate_evaluation_function_ranking(
            challenge, best_solution, evaluation_function_outputs_for_the_best_solution, solution_evaluations)
        ranking_of_evaluation_functions = chat([ranking_evaluation_functions_prompt])
        logging.info(f"Eanking_of_evaluation_functions: {ranking_of_evaluation_functions}")
        

    # TODO: This is just one prototype iteration. Ultimately, after tuning prompts and all, we aim to collect
    #       the good trajectories and fine-tune the model with those. This will make the model better at the tasks and
    #       also in evaluation of the tasks over each iteration.


if __name__ == "__main__":
    coding_improvement_iteration()
