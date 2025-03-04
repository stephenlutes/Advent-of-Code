import pytest
from solution import parse, part_1, part_2
from sugarplum import get_test_data


@pytest.mark.parametrize("data,answer", get_test_data(2015, 3, "part-1"))
def test_part_1(data: str, answer: int) -> None:
    parsed_data: str = parse(data)

    assert part_1(parsed_data) == answer


@pytest.mark.parametrize("data,answer", get_test_data(2015, 3, "part-2"))
def test_part_2(data: str, answer: int) -> None:
    parsed_data: str = parse(data)

    assert part_2(parsed_data) == answer
