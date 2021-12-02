"""

Problem 2020.2 : https://adventofcode.com/2020/day/2

"""
from solutions import tools


def convert_problem_input(problem_input_raw):
    raw = tools.convert_input_simple(problem_input_raw)
    processed = []

    for line in raw:
        min_max_range, letter, password = line

        min_amount, max_amount = [int(num) for num in min_max_range.split('-')]
        letter = letter.replace(':', '')

        processed.append(((min_amount, max_amount), letter, password))

    return processed


def solve_part_1(problem_input: list):
    num_good_passwords = 0

    for config in problem_input:
        min_max_range, letter, password = config

        num_letters = password.count(letter)

        if min_max_range[0] <= num_letters <= min_max_range[1]:
            num_good_passwords += 1

    return num_good_passwords


def solve_part_2(problem_input: list):
    num_good_passwords = 0

    for config in problem_input:
        index_range, letter, password = config
        expected_index, not_expected_index = [index - 1 for index in index_range]
        char_set = {password[expected_index], password[not_expected_index]}

        if letter in char_set and len(char_set) > 1:
            num_good_passwords += 1

    return num_good_passwords


def main():
    with open('input', 'r') as input_file:
        problem_input_raw = [line for line in input_file]

        problem_input = convert_problem_input(problem_input_raw)

        solution_1 = solve_part_1(problem_input)
        print(solution_1)

        solution_2 = solve_part_2(problem_input)
        print(solution_2)


if __name__ == '__main__':
    main()