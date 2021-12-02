"""

Problem 2021.1 : https://adventofcode.com/2021/day/1

"""
from solutions import tools


def convert_problem_input(problem_input_raw):
    return tools.convert_input_simple(problem_input_raw)


def solve_part_1(depths: list):
    current_depth = depths[0]
    depth_increases = 0

    for idx in range(1, len(depths)):
        new_depth = depths[idx]
        if new_depth > current_depth:
            depth_increases += 1
        current_depth = new_depth

    return depth_increases


def solve_part_2(depths: list):
    current_depth_window = sum(depths[0:3])
    depth_increases = 0

    for idx in range(3, len(depths)):
        new_depth = depths[idx]
        new_depth_window = current_depth_window - depths[idx - 3] + new_depth
        if new_depth_window > current_depth_window:
            depth_increases += 1
        current_depth_window = new_depth_window

    return depth_increases


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