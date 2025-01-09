import math
from heapq import nsmallest
from itertools import combinations

type Present = tuple[int, ...]


def parse(input_data: str) -> list[Present]:
    return [tuple(map(int, p.split("x"))) for p in input_data.splitlines()]


def part_1(data: list[Present]) -> int:
    return sum(
        sum(math.prod(c) * 2 for c in combinations(present, 2))
        + math.prod(nsmallest(2, present))
        for present in data
    )


def part_2(data: list[Present]) -> int:
    return sum(sum(nsmallest(2, present)) * 2 + math.prod(present) for present in data)
