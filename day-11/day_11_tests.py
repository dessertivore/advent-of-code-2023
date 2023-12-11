from day_11 import day_11_part_1


def test_all_day_11_part_1() -> None:
    assert day_11_part_1("day-11/test_input.txt")[0] == 9


def test_all_day_11_part_2() -> None:
    assert day_11_part_1("day-11/test_input.txt")[1] == 374
