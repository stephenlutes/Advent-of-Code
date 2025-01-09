from hashlib import md5


def parse(input_data: str) -> str:
    return input_data.strip()


def mine_coins(key: str, num: int, prefix_count: int) -> int:
    coin: str = md5(f"{key}{num}".encode("utf-8")).hexdigest()
    while coin[:prefix_count] != "0" * prefix_count:
        num += 1
        coin = md5(f"{key}{num}".encode("utf-8")).hexdigest()

    return num


def part_1(data: str) -> int:
    return mine_coins(data, 0, 5)


def part_2(data: str, num: int) -> int:
    # Num is the answer to part 1, since we know everything before it produces less than
    # 5 zeroes.
    return mine_coins(data, num, 6)
