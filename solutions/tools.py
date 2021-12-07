def convert_input_simple(problem_input: list):
    converted = []

    for line in problem_input:
        line = line.strip()

        if ' ' not in line:
            result = cast_simple(line)
        else:
            result = tuple([cast_simple(part) for part in line.split()])

        converted.append(result)

    return converted


def cast_simple(unknown):
    if unknown.isdigit():
        maybe_float = float(unknown)
        try:
            maybe_int = int(unknown)
            if maybe_float == maybe_int:
                return maybe_int
            else:
                return maybe_float
        except:
            return maybe_float
    else:
        return str(unknown)


def convert_input_str(problem_input: list):
    return [str(line).strip() for line in problem_input]


class Node:

    def __init__(self, val, next_ptr=None):
        self.val = val
        self.next_ptr = next_ptr

    def append(self, next_ptr=None):
        self.next_ptr = next_ptr
        return next_ptr
