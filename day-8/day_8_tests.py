from day_8 import day_8_part_1, open_input_8

test1_directions, test1_nodes = open_input_8("day-8/test_input.txt")


def test_day_8_p_1() -> None:
    assert (day_8_part_1(test1_directions, test1_nodes)) == 6
