"""

Problem 2021.6 : https://adventofcode.com/2021/day/6

"""
from solutions import tools
from collections import Counter


def convert_problem_input(problem_input_raw):
    raw = tools.convert_input_simple(problem_input_raw)
    processed = [int(num) for num in raw[0].split(',')]
    return processed


def solve_part_1(problem_input: list):
    fishes = list(problem_input)
    fish_count = iterate_days(80, build_fish_count(fishes))
    return sum(fish_count.values())


def solve_part_2(problem_input: list):
    fishes = list(problem_input)
    fish_count = iterate_days(256, build_fish_count(fishes))
    return sum(fish_count.values())


def build_fish_count(fishes):
    fish_count = dict(Counter(fishes).items())

    for idx in range(9):
        if idx not in fish_count:
            fish_count[idx] = 0

    return fish_count


def iterate_days(num_days, fish_count):
    for day in range(0, num_days):
        new_count = {}

        for idx in range(8, -1, -1):
            new_count[idx - 1] = fish_count[idx]

        breeding = new_count[-1]
        new_count[6] += breeding
        new_count[8] = breeding
        del new_count[-1]
        fish_count = new_count

    return fish_count


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