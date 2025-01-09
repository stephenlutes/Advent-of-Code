import pytest
from solution import Command, parse, part_1, part_2
from sugarplum import TestData, get_test_data


def test_parse() -> None:
    entry: TestData = get_test_data(2015, 6, "part-1")
    expected: list[Command] = [
        Command("turn on", 0, 0, 999, 999),
        Command("toggle", 0, 0, 999, 0),
        Command("turn off", 499, 499, 500, 500),
    ]

    assert parse(entry.data) == expected


def test_part_1() -> None:
    entry: TestData = get_test_data(2015, 6, "part-1")
    data: list[Command] = parse(entry.data)

    assert part_1(data) == 998996


@pytest.mark.parametrize("data,answer", get_test_data(2015, 6, "part-2"))
def test_part_2(data: str, answer: int) -> None:
    parsed_data: list[Command] = parse(data)

    assert part_2(parsed_data) == answer
