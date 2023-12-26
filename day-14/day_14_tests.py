from parse_input import create_array
from day_14 import (
    find_rocks_and_round_rocks,
    move_rocks_north,
    calculate_load,
    spin_cycle,
)

test_map: dict = create_array("day-14/test_input.txt")
(
    test_round_rocks,
    test_rocks_by_x,
    test_rocks_by_y,
    test_max_x,
    test_max_y,
) = find_rocks_and_round_rocks(test_map)

test_new_round_rocks = move_rocks_north(test_round_rocks, test_rocks_by_y)
assert calculate_load(test_new_round_rocks, test_max_x) == 136

assert (
    spin_cycle(
        test_round_rocks,
        test_rocks_by_x,
        test_rocks_by_y,
        test_max_x,
        test_max_y,
        1000000000,
    )
    == 64
)
