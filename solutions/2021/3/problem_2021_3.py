"""

Problem 2021.3 : https://adventofcode.com/2021/day/3

"""
from solutions import tools


def convert_problem_input(problem_input_raw):
    return tools.convert_input_str(problem_input_raw)


def solve_part_1(problem_input: list):
    buckets = {}
    for line in problem_input:
        for idx, digit in enumerate(line):
            if idx not in buckets:
                buckets[idx] = {
                    '0': 0,
                    '1': 0
                }

            buckets[idx][digit] += 1

    gamma = ''
    epsilon = ''

    for amount in buckets.values():
        num_zeros = amount['0']
        num_ones = amount['1']
        most_common = '1' if num_ones > num_zeros else '0'
        least_common = '1' if num_ones < num_zeros else '0'

        gamma += most_common
        epsilon += least_common

    return int(gamma, 2) * int(epsilon, 2)


def solve_part_2(problem_input: list):

    oxygen_lines = {line: True for line in problem_input}
    c02_lines = {line: True for line in problem_input}

    num_digits = len(problem_input[0])

    oxygen_num = ''
    for idx in range(0, num_digits):
        idx_bucket = {
                    '0': 0,
                    '1': 0
                }

        for line in oxygen_lines:
            idx_bucket[line[idx]] += 1

        num_zeros = idx_bucket['0']
        num_ones = idx_bucket['1']

        most_common = '1' if num_ones > num_zeros else '0'

        if num_ones == num_zeros:
            most_common = '1'

        delete_list = []
        for line in oxygen_lines.keys():
            if line[idx] != most_common:
                delete_list.append(line)

        for delete in delete_list:
            del oxygen_lines[delete]

        if len(oxygen_lines) == 1:
            oxygen_num = [key for key in oxygen_lines][0]

    co2_num = ''
    for idx in range(0, num_digits):
        idx_bucket = {
            '0': 0,
            '1': 0
        }

        for line in c02_lines:
            idx_bucket[line[idx]] += 1

        num_zeros = idx_bucket['0']
        num_ones = idx_bucket['1']

        least_common = '1' if num_ones < num_zeros else '0'

        if num_ones == num_zeros:
            least_common = '0'

        delete_list = []
        for line in c02_lines.keys():
            if line[idx] != least_common:
                delete_list.append(line)

        for delete in delete_list:
            del c02_lines[delete]

        if len(c02_lines) == 1:
            co2_num = [key for key in c02_lines][0]

    return int(oxygen_num, 2) * int(co2_num, 2)


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