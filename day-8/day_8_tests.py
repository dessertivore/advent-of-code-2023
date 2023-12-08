from day_8 import day_8_part_1, open_input_8, day_8_part_2

test_directions, test_nodes, discard_test_A_list = open_input_8("day-8/test_input.txt")
test_directions_2, test_nodes_2, test_A_list = open_input_8("day-8/test_input_2.txt")


def test_day_8_p_1() -> None:
    assert (day_8_part_1(test_directions, test_nodes)) == 2


def test_day_8_p_2() -> None:
    assert (day_8_part_2(test_directions_2, test_nodes_2, test_A_list)) == 6
