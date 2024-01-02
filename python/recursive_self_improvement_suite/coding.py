"""Coding task prompts."""

from typing import List

# The Code Llama prompts are given here as an inspiration, not something we want to follow.
# We need to make at least the following improvements:
# - The problems need to be open-ended, not simple interview questions with one correct answer.
# - The problems need to be realistic, with real world constraints and interfaces.
# - The problems need to require generalist skills, not one skill like in interview questions.
# - We need to evaluate solutions by rankings, potentially by involving running the unit tests and their resulting scores.
# - We need to have prompts also to evaluate evaluation rankings.

# The self-instruct in Code Llama was done with the following recipe:
# https://scontent.fgrx2-1.fna.fbcdn.net/v/t39.2365-6/369856151_1754812304950972_1159666448927483931_n.pdf
#
#  We construct the self-instruction dataset following the recipe
#  below, resulting in ∼14,000 question-tests-solution triplets:
#  1. Generate 62,000 interview-style programming questions by prompting (Figure 9) Llama 2 70B.
#  2. De-duplicate the set of questions by removing exact duplicates, resulting in ∼52,000 questions.
#  3. For each of these questions:
#  (a) Generate unit tests by prompting Code Llama 7B (Figure 10)
#  (b) Generate ten Python solutions by prompting Code Llama 7B (Figure 11)
#  (c) Run the unit tests on the ten solutions. Add the first solution that passes the tests (along with
#      its corresponding question and tests) to the self-instruct dataset.

code_llama_example_challenges_prompt = """\
Prompt: [INST] Write 50 programming interview questions of easy and medium complexity. Provide questions on a
diverse range of subjects, and make sure no two questions are alike. Make sure the problems can be solved with a
single standalone Python function using standard libraries. [/INST]
1. Write a function that finds the maximum depth of list nesting in a given list.
2. Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
3. Write a function that gets the musical pitch that is closest to a given frequency in Hz. A pitch should consist of a
letter, possibly a # sign, and an octave number.
4. Write a function that removes any sequences of whitespace that are between numbers in an input string.
5. Write a function that counts the number of words in a string that have length n, where n is an input. The function
should ignore characters that aren’t letters, numbers, or spaces.
6. Write a function that returns the longest palindromic substring in a given string.
7. Create a function that will find the length of the longest substring without repeating characters in a given string.
8. Write a function that reverses the diagits in a number.
9. Write a function that finds the valleys in a list of integers.
10. Write a python function that reverses every group of k words in a sentence."""

code_llama_example_evaluation_prompt = """\
[INST] Your task is to write 5 tests to check the correctness of a function that solves a programming
problem.
The tests must be between [TESTS] and [/TESTS] tags.
You must write the comment "#Test case n:" on a separate line directly above each assert statement,
where n represents the test case number, starting from 1 and increasing by one for each subsequent
test case.
Problem: Write a Python function to get the unique elements of a list.
[/INST]
[TESTS]
# Test case 1:
assert get_unique_elements([]) == []
# Test case 2:
assert get_unique_elements([1]) == [1]
# Test case 3:
assert get_unique_elements([1, 2, 3, 2, 1]) == [1, 2, 3]
[/TESTS]
[INST] Problem: %%%question%%%
[/INST]"""

code_llama_example_generate_unit_test_prompt = """\
[INST] Your task is to write a Python function to solve a programming problem.
The Python code must be between [PYTHON] and [/PYTHON] tags.
You are given one example test from which you can infere the function signature.
Problem: Write a Python function to get the unique elements of a list.
Test: assert get_unique_elements([1, 2, 3, 2, 1]) == [1, 2, 3]
[/INST]
[PYTHON]
def get_unique_elements(my_list):
return list(set(my_list))
[/PYTHON]
[INST] Problem: %%%question%%%
Test: %%%test%%%
[/INST]"""

code_llama_example_generate_solution_prompt = """\
You are an expert Python programmer, and here is your task: {task}
Your code should pass these tests:\n\n{tests}\nYour code should start with a [PYTHON] tag and end with a [/PYTHON] tag."""

# We need to generate the following:
# - Programming challenges
# - Evaluation functions where the programming challenge is known.
# - Solutions, where both the challenge and the evaluation function is known.
# We also need prompts to evaluate the quality of all three in relation to each others, by producing rankings for:
# - Programming challenges by a specific list of criteria.
# - Evaluation functions, when both the challenge and a sample solution are also given.
# - Solutions, where the challenge, the evaluation function, and the evaluation function output are also given.
# In addition we need a prompt to rank the rankings of each of the three ranking responses based on a given list of criteria.

# The problem here is that OpenAI GPT-x models are trained to not hallucinate, which
# makes them really bad at improvisation which is a skill needed here.
# No matter, we'll train the skill of improvisation back into the LLM model under training.
# For context size limit reasons we'll need to focus on challenges with short solutions.
# Note that initially we don't specify the JSON Schema, and let the bot to decide it. After that, we codify that schema.


def generate_challenges(n: int = 10):
    schema = """\
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "domain": {
        "type": "string"
      },
      "id": {
        "type": "string"
      },
      "description": {
        "type": "string"
      }
    },
    "required": ["id", "description"],
    "additionalProperties": false
  }
}
"""
    return f"""\
Please help me generate some open-ended programming challenges in Python.
The challenges shouldn't be puzzles, but components in a real-world application.
Choose a domain, like supply chain, medical systems, computer aided design, or anything else,
and produce a programming challenge for that domain.
The skillset needed to solve the programming challenge should involve specific libraries or frameworks,
but also should show domain understanding and understanding of user needs.
Solutions to the challenge should be implementable with some lines of code using a single function entrypoint,
although multiple functions are allowed, because the solutions will be automatically evaluated.
Your output must conform exactly to the following JSON Schema:
<JSON-Schema>
{schema}
</JSON-Schema>
Now, please give me {n} programming challenge descriptions. Produce them in a JSON form without Markdown notation because they are read by a machine.
"""

def generate_evaluation_function(challenge: str):
    return f"""\
Here is a programming challenge:
<challenge>
{challenge}
</challenge>
I need you to produce a small Python code which runs the function and prints out evaluation results for it.
Do not produce the expected output, just the plain Python code which prints out the results of running the code.
Answer just by giving the Python code with Markdown notation.
"""


def generate_solutions(challenge: str, evaluation_function: str):
    return f"""\
Here is a programming challenge:
<challenge>
{challenge}
</challenge>
Here is the code used to evaluate your solution:
<evaluation-function>
{evaluation_function}
</evaluation-function>

I need you to produce a small Python code which solves the given problem as evaluated by the evaluation code.
Answer just by giving the Python code with Markdown notation.
"""


def evaluate_challenges(challenges: List[str], challenge_ids: List[str], n: int = 5):
    schema = f"""\
{{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "array",
  "items": {{
    "type": "object",
    "properties": {{
      "id": {{
        "type": "string",
        "enum": [{challenge_ids}]
      }},
      "rationale": {{
        "type": "string"
      }}
    }},
    "required": ["id", "rationale"],
    "additionalProperties": false
  }}
}}
"""
    return f"""\
Here are some programming challenges which need to be evaluated and ranked:
<challenges>
{challenges}
</challenges>
Your output must conform exactly to the following JSON Schema:
<JSON-Schema>
{schema}
</JSON-Schema>
Please choose the best {n}. Evaluate the challenges based on the following criteria:
- Innovativeness and novelty. The challenge should not be very similar to known interview questions, or programming puzzles.
- Requires various skills and domain knowledge to solve well.
- Can be solved with few lines of code with a single function call entrypoint.
Now, please produce a JSON response without Markdown notation which refers to the best {n} challenges from this set by id, along with rationales.
"""


def evaluate_evaluation_functions(
    challenge: str, evaluation_functions: List[str]
):
    return f"""\
Here is a programming challenge, and a set of evaluation functions:
<challenge>
{challenge}
</challenge>
<evaluation-functions>
{evaluation_functions}
</evaluation-functions>
Please choose the best evaluation function which evaluates the quality of the sample solution in the most suitable manner.
Produce the best evaluation function id in a valid JSON object without Markdown notation.
"""


def evaluate_solutions(
    challenge: str,
    evaluation_function: str,
    sample_solutions_with_evaluation_function_outputs: str,
):
    return f"""\
Here is a programming challenge, an evaluation function and a set of sample solutions for it:
<challenge>
{challenge}
</challenge>
<evaluation-function>
{evaluation_function}
</evaluation-function>
<sample-solutions-with-evaluation-function-outputs>
{sample_solutions_with_evaluation_function_outputs}
</sample-solutions-with-evaluation-function-outputs>
Please choose the best sample solution.
Produce the sample solution id in a valid JSON object without Markdown notation.
"""


# Note that rankings include rationales for rankings which makes it easier to decide which one is the best.
def evaluate_challenge_ranking(challenges: List[str], rankings: List[str]):
    return f"""\
Here is a set of programming challenges:
<challenges>
{challenges}
</challenges>
<rankings>
{rankings}
</rankings>
Please choose the best ranking for the challenges.
Produce the ranking id in plain JSON without Markdown notation.
"""


def evaluate_solution_ranking(
    challenge: str,
    evaluation_function: str,
    sample_solutions_with_evaluation_function_outputs: List[str],
    sample_rankings_of_solutions: List[str],
):
    return f"""\
Here is a programming challenge, an evaluation function, a set of sample solutions for it, and a set of rankings for the sample solutions:
<challenge>
{challenge}
</challenge>
<evaluation-function>
{evaluation_function}
</evaluation-function>
<sample-solutions-with-evaluation-function-outputs>
{sample_solutions_with_evaluation_function_outputs}
</sample-solutions-with-evaluation-function-outputs>
<sample-rankings-of-solutions>
{sample_rankings_of_solutions}
</sample-rankings-of-solutions>
Please choose the best ranking for the solutions.
Produce the ranking id in plain JSON without Markdown notation.
"""


def evaluate_evaluation_function_ranking(
    challenge: str,
    sample_solution: str,
    evaluation_functions_with_outputs: str,
    sample_rankings_of_evaluation_functions: List[str],
):
    return f"""\
Here is a programming challenge, a sample solution for it, a set of evaluation functions with their outputs for the sample solution, and a set of rankings for the evaluation functions:
<challenge>
{challenge}
</challenge>
<sample-solution>
{sample_solution}
</sample-solution>
<evaluation-functions-with-outputs>
{evaluation_functions_with_outputs}
</evaluation-functions-with_outputs>
<sample-rankings-of-evaluation-functions>
{sample_rankings_of_evaluation_functions}
</sample-rankings-of-evaluation-functions>
Please choose the best ranking for the evaluation functions.
Produce the ranking id in plain JSON without Markdown notation.
"""
