import pytest
from solution import Present, parse, part_1, part_2
from sugarplum import TestData, get_test_data


def test_parse() -> None:
    entry: TestData = get_test_data(2015, 2, "parse")

    result: list[Present] = parse(entry.data)

    assert result == [(2, 3, 4), (1, 1, 10)]


@pytest.mark.parametrize("data,answer", get_test_data(2015, 2, "part-1"))
def test_part_1(data: str, answer: int) -> None:
    parsed_data: list[Present] = parse(data)

    assert part_1(parsed_data) == answer


@pytest.mark.parametrize("data,answer", get_test_data(2015, 2, "part-2"))
def test_part_2(data: str, answer: int) -> None:
    parsed_data: list[Present] = parse(data)

    assert part_2(parsed_data) == answer
