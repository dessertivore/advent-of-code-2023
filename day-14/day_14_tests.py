from parse_input import create_array
from day_14 import find_rocks_and_round_rocks, move_rocks, calculate_load

test_map: dict = create_array("day-14/test_input.txt")
test_round_rocks, test_rocks, test_max_x, test_max_y = find_rocks_and_round_rocks(
    test_map
)
test_new_round_rocks = move_rocks(test_round_rocks, test_rocks)
print(calculate_load(test_new_round_rocks, test_max_x))
assert calculate_load(test_new_round_rocks, test_max_x) == 136
