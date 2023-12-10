from day_10 import day_10_parse_nodes, day_10_p_1

pipe_map, root = day_10_parse_nodes("day-10/test_input.txt")


def test_day_10_p1() -> None:
    assert day_10_p_1(pipe_map, root) == 4


# def test_day_10_p1() -> None:
#     assert day_10_p_1(array1) == 8
