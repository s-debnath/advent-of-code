"""

Problem 2021.2 : https://adventofcode.com/2021/day/2

"""
from solutions import tools


def convert_problem_input(problem_input_raw):
    return tools.convert_input_simple(problem_input_raw)


def solve_part_1(problem_input: list):
    x, y = 0, 0

    for direction, amount in problem_input:
        if direction == 'forward':
            x += amount
        elif direction == 'down':
            y += amount
        else:
            y -= amount

    return x * y


def solve_part_2(problem_input: list):
    x, y, aim = 0, 0, 0

    for direction, amount in problem_input:
        if direction == 'forward':
            x += amount
            y += (amount*aim)
        elif direction == 'down':
            aim += amount
        else:
            aim -= amount

    return x * y


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