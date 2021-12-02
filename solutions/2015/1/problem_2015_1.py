"""

Problem 2015.1 : https://adventofcode.com/2015/day/1

"""
from solutions import tools


def convert_problem_input(problem_input_raw):
    return tools.convert_input_simple(problem_input_raw)


def solve_part_1(problem_input: list):
    parentheses = problem_input[0]
    floor = 0
    for letter in parentheses:
        if letter == ')':
            floor -= 1
        else:
            floor += 1

    return floor


def solve_part_2(problem_input: list):
    parentheses = problem_input[0]
    floor = 0
    for idx, letter in enumerate(parentheses):
        if letter == ')':
            floor -= 1
        else:
            floor += 1

        if floor == -1:
            return idx + 1

    return -1


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