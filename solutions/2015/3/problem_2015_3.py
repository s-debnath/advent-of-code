"""

Problem 2015.3 : https://adventofcode.com/2015/day/3

"""
from solutions import tools


def convert_problem_input(problem_input_raw):
    return tools.convert_input_simple(problem_input_raw)


def santa_visit(directions):
    x, y = 0, 0
    visited_houses = {(0, 0)}

    for direction in directions:
        if direction == '>':
            x += 1
        elif direction == '<':
            x -= 1
        elif direction == '^':
            y += 1
        else:
            y -= 1

        visited_houses.add((x, y))

    return visited_houses


def solve_part_1(problem_input: list):
    directions = problem_input[0]

    return len(santa_visit(directions))


def solve_part_2(problem_input: list):
    directions = problem_input[0]
    santa_directions = []
    robosantas_directions = []

    for idx, direction in enumerate(directions):
        if idx % 2 == 0:
            santa_directions.append(direction)
        else:
            robosantas_directions.append(direction)

    return len(santa_visit(santa_directions).union(santa_visit(robosantas_directions)))


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