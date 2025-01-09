from typing import Callable

type Point = tuple[int, int]


def parse(input_data: str) -> str:
    return input_data.strip()


def deliver_presents(directions: str) -> set[Point]:
    moves: dict[str, Callable] = {
        "^": lambda c: (c[0], c[1] + 1),
        ">": lambda c: (c[0] + 1, c[1]),
        "v": lambda c: (c[0], c[1] - 1),
        "<": lambda c: (c[0] - 1, c[1]),
    }
    visited: list[Point] = [(0, 0)]
    for step in directions:
        visited.append(moves[step](visited[-1]))

    return set(visited)


def part_1(data: str) -> int:
    return len(deliver_presents(data))


def part_2(data: str) -> int:
    return len(deliver_presents(data[::2]) | deliver_presents(data[1::2]))
