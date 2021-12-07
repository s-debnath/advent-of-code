"""

Problem 2021.5 : https://adventofcode.com/2021/day/5

"""
from solutions import tools


def convert_problem_input(problem_input_raw):
    raw = tools.convert_input_simple(problem_input_raw)
    converted = []

    max_x, max_y = 0, 0

    for line in raw:
        original, _, new = line
        x_orig, y_orig = [int(coord) for coord in original.split(',')]
        x_new, y_new = [int(coord) for coord in new.split(',')]
        max_x = max(max_x, x_orig, x_new)
        max_y = max(max_y, y_orig, y_new)
        converted.append(((x_orig, y_orig), (x_new, y_new)))

    return converted, (max_x, max_y)


def solve_part_1(problem_input: tuple):
    segments, (max_x, max_y) = problem_input
    spectrogram = [[0] * (max_y + 1) for _ in range(max_x + 1)]

    for (x_orig, y_orig), (x_new, y_new) in segments:
        if x_orig != x_new and y_orig != y_new:
            continue

        mark_crossed(spectrogram, x_orig, y_orig, x_new, y_new)

    return calc_num_dangerous(spectrogram)


def solve_part_2(problem_input: tuple):
    segments, (max_x, max_y) = problem_input
    spectrogram = [[0] * (max_y + 1) for _ in range(max_x + 1)]

    for (x_orig, y_orig), (x_new, y_new) in segments:
        mark_crossed(spectrogram, x_orig, y_orig, x_new, y_new)

    return calc_num_dangerous(spectrogram)


def mark_crossed(spectrogram, x_orig, y_orig, x_new, y_new):
    is_moving_vertically = x_orig == x_new
    is_moving_horizontally = y_orig == y_new

    if is_moving_vertically:
        move_x = lambda x: x
        direction = 1 if y_new > y_orig else -1
        move_y = lambda y: y + direction
    elif is_moving_horizontally:
        move_y = lambda y: y
        direction = 1 if x_new > x_orig else -1
        move_x = lambda x: x + direction
    else:
        direction_x = 1 if x_new > x_orig else -1
        move_x = lambda x: x + direction_x
        direction_y = 1 if y_new > y_orig else -1
        move_y = lambda y: y + direction_y

    cur_x, cur_y = x_orig, y_orig

    while cur_x != x_new or cur_y != y_new:
        spectrogram[cur_x][cur_y] += 1
        cur_x = move_x(cur_x)
        cur_y = move_y(cur_y)

    spectrogram[x_new][y_new] += 1


def calc_num_dangerous(spectrogram):
    num_dang = 0

    for row in spectrogram:
        for val in row:
            if val >= 2:
                num_dang += 1

    return num_dang


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
