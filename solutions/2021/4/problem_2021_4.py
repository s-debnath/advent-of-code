"""

Problem 2021.4 : https://adventofcode.com/2021/day/4

"""
from solutions import tools
from collections import OrderedDict, defaultdict


def convert_problem_input(problem_input_raw):
    raw = tools.convert_input_str(problem_input_raw)
    converted = {
        'drawing_nums':  [int(num) for num in raw[0].split(',')],
        'num_board_map': defaultdict(list)
    }

    current_board = OrderedDict()

    for board_start_idx in range(2, len(raw), 6):
        current_idx = board_start_idx
        while  current_idx < len(raw) and raw[current_idx]:
            current_row = raw[current_idx]
            for num_str in current_row.split():
                num = int(num_str)
                if num in current_board:
                    raise Exception()
                current_board[num] = False
                converted['num_board_map'][num].append(current_board)
            current_idx += 1
        current_board = OrderedDict()

    return converted


def solve_part_1(problem_input: dict):
    drawing_nums = problem_input['drawing_nums']
    num_board_map = problem_input['num_board_map']

    for num in drawing_nums:
        relevant_boards = num_board_map.get(num)

        for board in relevant_boards:
            board[num] = True
            if is_winner(board):
                sum_unmarked = calc_sum_unmarked(board)
                return sum_unmarked * num


def is_winner(board):
    keys = [key for key in board.keys()]

    for board_start_idx in range(0, len(board), 5):
        current_idx = board_start_idx
        while current_idx < board_start_idx + 5:
            current_key = keys[current_idx]
            if not board[current_key]:
                break
            current_idx += 1
        else:
            return True

    for board_start_idx in range(0, 5):
        for add in range(0, 5):
            current_idx = board_start_idx + 5*add
            current_key = keys[current_idx]
            if not board[current_key]:
                break
            current_idx += 1
        else:
            return True

    return False


def calc_sum_unmarked(board):
    running_sum = 0
    for amount, found in board.items():
        if not found:
            running_sum += amount

    return running_sum


def solve_part_2(problem_input: dict):
    drawing_nums = problem_input['drawing_nums']
    num_board_map = problem_input['num_board_map']
    winning_boards = set()
    last_board = None
    last_num = None

    for num in drawing_nums:
        relevant_boards = num_board_map.get(num)

        for board in relevant_boards:
            if tuple(board.keys()) in winning_boards:
                continue

            board[num] = True
            if is_winner(board):
                winning_boards.add(tuple(board.keys()))
                last_board = board
                last_num = num

    return last_num * calc_sum_unmarked(last_board)



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