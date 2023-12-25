"""Coding task prompts."""

# The Code Llama prompts are given here as an inspiration, not something we want to follow.
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
