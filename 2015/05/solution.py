import re


def parse(input_data: str) -> list[str]:
    return input_data.splitlines()


def part_1(strings: list[str]) -> int:
    return len(
        [
            s
            for s in strings
            if re.search(r"([aeiou].*){3}", s)
            and re.search(r"([a-z])\1", s)
            and not re.search(r"ab|cd|pq|xy", s)
        ]
    )


def part_2(strings: list[str]) -> int:
    return len(
        [
            s
            for s in strings
            if re.search(r"([a-z]{2}).*\1", s) and re.search(r"([a-z]).\1", s)
        ]
    )
