"""

Problem 2015.4 : https://adventofcode.com/2015/day/4

"""
from solutions import tools
import sys
import hashlib


def convert_problem_input(problem_input_raw):
    return tools.convert_input_simple(problem_input_raw)


def solve_part_1(problem_input: list):
    password = problem_input[0]

    for num in range(0, sys.maxsize):
        unencrypted = f"{password}{num}"
        encrypted = hashlib.md5(unencrypted.encode('utf-8')).hexdigest()
        if encrypted.startswith("00000"):
            return num


def solve_part_2(problem_input: list):
    password = problem_input[0]

    for num in range(0, sys.maxsize):
        unencrypted = f"{password}{num}"
        encrypted = hashlib.md5(unencrypted.encode('utf-8')).hexdigest()
        if encrypted.startswith("000000"):
            return num


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