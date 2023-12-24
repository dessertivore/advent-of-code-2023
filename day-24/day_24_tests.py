from parse_input import parse_input_func_2
from day_24 import find_collision_course

test_input = parse_input_func_2("day-24/test_input.txt")
assert find_collision_course(test_input, 7, 27) == 2
