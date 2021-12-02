"""

Problem 2020.1 : https://adventofcode.com/2020/day/1

"""
from solutions import tools


def convert_problem_input(problem_input_raw):
    return tools.convert_input_simple(problem_input_raw)


def solve_part_1(problem_input: list):
    expenses_set = {expense for expense in problem_input}
    target_num = 2020

    for expense in expenses_set:
        other_val = target_num - expense
        if other_val in expenses_set:
            return expense * other_val

    return -1


def solve_part_2(problem_input: list):
    sorted_expenses = list(sorted(problem_input))
    expenses_set = {expense for expense in problem_input}
    target_num = 2020

    for idx, first_val in enumerate(sorted_expenses):
        for second_val in sorted_expenses[idx+1:]:
            if first_val + second_val < target_num:
                third_val = target_num - first_val - second_val
                if third_val in expenses_set:
                    return first_val * second_val * third_val

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