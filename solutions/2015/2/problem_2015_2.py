"""

Problem 2015.2 : https://adventofcode.com/2015/day/2

"""
from solutions import tools


def convert_problem_input(problem_input_raw):
    raw = tools.convert_input_simple(problem_input_raw)
    processed = []

    for line in raw:
        processed.append(tools.convert_input_simple(line.split('x')))

    return processed


def solve_part_1(problem_input: list):
    required_wrapping = 0

    for dimensions in problem_input:
        l, w, h = dimensions
        current_requirement = 2*l*w + 2*w*h + 2*l*h + min(l*w, w*h, l*h)
        required_wrapping += current_requirement

    return required_wrapping


def solve_part_2(problem_input: list):
    required_ribbon = 0

    for dimensions in problem_input:
        l, w, h = list(sorted(dimensions))
        current_requirement = 2*l + 2*w + l*w*h
        required_ribbon += current_requirement

    return required_ribbon


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