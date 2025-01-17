import pytest
from solution import Circuit, parse, part_1
from sugarplum import TestData, get_test_data


def test_parse() -> None:
    entry: TestData = get_test_data(2015, 7, "parse")

    assert parse(entry.data) == entry.answer


@pytest.mark.parametrize("data,answer", get_test_data(2015, 7, "part-1"))
def test_part_1(data: str, answer: int) -> None:
    entry: TestData = get_test_data(2015, 7, "parse")
    circuit: Circuit = parse(entry.data.replace(data, "a"))

    assert part_1(circuit) == answer
