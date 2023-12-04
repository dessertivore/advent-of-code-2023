from parse_input import parse_input_func
from day_4 import day4, day4_p2

input1 = parse_input_func("day-4/test_input4.txt")
input = [
    line.strip("Card ")
    .replace(": ", " ")
    .replace(" | ", " ")
    .replace("  ", " ")
    .split(" ")
    for line in input1
]  # remove double spaces and and separate all numbers


def test_part_of_part1() -> None:
    assert (day4([[1, 41, 48, 83, 86, 17, 83, 86, 6, 31, 17, 9, 48, 53]], 5)) == 8


def test_part1() -> None:
    assert (day4(input, 5)) == 13


def test_part_of_part2() -> None:
    assert (day4_p2([[1, 41, 48, 83, 86, 17, 83, 86, 6, 31, 17, 9, 48, 53]], 5)) == 1


def test_part2() -> None:
    assert (day4_p2(input, 5)) == 30
