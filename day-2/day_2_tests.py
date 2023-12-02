from day_2 import parse_input, day2

test_input = parse_input(open("day-2/input_tests.txt", "r").readlines())

print(test_input)

assert day2(test_input) == 8
