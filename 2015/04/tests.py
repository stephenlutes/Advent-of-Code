import pytest
from solution import parse, part_1
from sugarplum import get_test_data


@pytest.mark.parametrize("data,answer", get_test_data(2015, 4, "part-1"))
def test_part_1(data: str, answer: int) -> None:
    parsed_data: str = parse(data)

    assert part_1(parsed_data) == answer
