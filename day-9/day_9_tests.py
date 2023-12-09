from parse_input import parse_input_func_2
from day_9 import day_9_part_1

day_9_test = parse_input_func_2("day-9/test_input.txt")
print(day_9_test)


def test_part_of_part_1() -> None:
    assert day_9_part_1([[0, 3, 6, 9, 12, 15]]) == 18


def test_part2_of_part_1() -> None:
    assert day_9_part_1([[1, 3, 6, 10, 15, 21]]) == 28


def test_part3_of_part_1() -> None:
    assert day_9_part_1([[10, 13, 16, 21, 30, 45]]) == 68


def test_day_9_part_1() -> None:
    assert day_9_part_1(day_9_test) == 114
