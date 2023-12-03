from day_3 import day3, populate_table, check_diag, day3_asterisk, check_ratio
import pytest

input: list[str] = open("day-3/test_input.txt", "r").readlines()
input1 = [line.strip("\n") for line in input]

input2 = populate_table(input1)


def test_check_diag() -> None:
    assert (check_diag(0, 2, 0, input2)) == True


def test_day3() -> None:
    assert day3(input2) == 4361


def test_check_digs() -> None:
    assert check_ratio(1, 3, input2) == 16345


def test_part2() -> None:
    assert day3_asterisk(input2) == 467835
