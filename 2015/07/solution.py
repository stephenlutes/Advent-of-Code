from functools import cache

type Circuit = dict[str, list[str]]


def parse(input_data: str) -> Circuit:
    circuit: Circuit = {}
    for line in input_data.splitlines():
        cmd, key = line.split(" -> ")
        circuit[key] = cmd.split()

    return circuit


def run_circuit(circuit: Circuit) -> int:
    @cache
    def get_value(key: str) -> int:
        if key.isdigit():
            return int(key)
        if len(circuit[key]) == 1:
            return get_value(circuit[key][0])
        if "AND" in circuit[key]:
            return get_value(circuit[key][0]) & get_value(circuit[key][2])
        if "OR" in circuit[key]:
            return get_value(circuit[key][0]) | get_value(circuit[key][2])
        if "NOT" in circuit[key]:
            return ~get_value(circuit[key][1]) & 0xFFFF
        if "LSHIFT" in circuit[key]:
            return get_value(circuit[key][0]) << get_value(circuit[key][2])
        if "RSHIFT" in circuit[key]:
            return get_value(circuit[key][0]) >> get_value(circuit[key][2])

        raise Exception()

    get_value.cache_clear()
    return get_value("a")


def part_1(data: Circuit) -> int:
    return run_circuit(data)


def part_2(data: Circuit, prev: int) -> int:
    # prev is the answer that was found in part 1.
    data["b"] = [str(prev)]

    return run_circuit(data)
