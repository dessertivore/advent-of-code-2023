from day_16 import create_array, follow_map, part_2
from parse_input import create_array

testing = create_array("day-16/test_input.txt")

assert (follow_map(testing)) == 46

assert part_2(testing) == 51
