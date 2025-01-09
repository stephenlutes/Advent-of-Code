import re
from typing import Callable, NamedTuple


class Command(NamedTuple):
    cmd: str
    x1: int
    y1: int
    x2: int
    y2: int


def parse(input_data: str) -> list[Command]:
    commands: list[Command] = []
    for entry in input_data.splitlines():
        result: tuple = re.match(  # type: ignore
            r"(?P<cmd>\w*(?: \w*)?) (?P<x1>\d*),(?P<y1>\d*) through (?P<x2>\d*),(?P<y2>\d*)",
            entry,
        ).groups()
        commands.append(
            Command(
                result[0],
                int(result[1]),
                int(result[2]),
                int(result[3]),
                int(result[4]),
            )
        )

    return commands


def run_sequence(data: list[Command], operations: dict[str, Callable]) -> int:
    lights: list[list[int]] = [[0 for x in range(1000)] for y in range(1000)]
    for command in data:
        for y in range(command.y1, command.y2 + 1):
            for x in range(command.x1, command.x2 + 1):
                lights[y][x] = operations[command.cmd](lights[y][x])

    return sum(sum(x) for x in lights)


def part_1(data: list[Command]) -> int:
    operations: dict[str, Callable] = {
        "turn on": lambda x: 1,
        "toggle": lambda x: x ^ True,
        "turn off": lambda x: 0,
    }

    return run_sequence(data, operations)


def part_2(data: list[Command]) -> int:
    operations: dict[str, Callable] = {
        "turn on": lambda x: x + 1,
        "toggle": lambda x: x + 2,
        "turn off": lambda x: x - 1 if x - 1 >= 0 else 0,
    }

    return run_sequence(data, operations)
