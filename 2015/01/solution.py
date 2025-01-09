from collections import Counter


def parse(input_data: str) -> str:
    return input_data.strip()


def part_1(data: str) -> int:
    counter: Counter = Counter(data)

    return counter["("] - counter[")"]


def part_2(data: str) -> int:
    floor: int = 0
    moves: dict[str, int] = {"(": 1, ")": -1}
    for i, step in enumerate(data, 1):
        floor += moves[step]
        if floor == -1:
            return i

    raise Exception()
