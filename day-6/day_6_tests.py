from parse_input import parse_input_func_2, parse_input_1_no_per_line
from day_6 import day_6_pt_1, day_6_pt_2

input1 = parse_input_func_2("day-6/test_input.txt")

print(day_6_pt_1(input1))


def test_day6_part_1() -> None:
    assert (day_6_pt_1(input1)) == 288


part_2_input = parse_input_1_no_per_line("day-6/test_input.txt")


def test_day6_part_2() -> None:
    assert (day_6_pt_2(part_2_input)) == 71503
