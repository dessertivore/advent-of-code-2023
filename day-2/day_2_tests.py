from day_2 import parse_input, day2, d2_part2, total_d2_part2

test_input = parse_input(open("day-2/input_tests.txt", "r").readlines())

assert day2(test_input) == 8

assert d2_part2(test_input, 1) == 48
assert d2_part2(test_input, 2) == 12
assert d2_part2(test_input, 3) == 1560
assert d2_part2(test_input, 4) == 630
assert d2_part2(test_input, 5) == 36
assert total_d2_part2(test_input) == 2286
