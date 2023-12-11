from day_10 import day_10_parse_nodes, day_10_p_1, find_area

pipe_map, root, discard_map, discard = day_10_parse_nodes("day-10/test_input.txt")
pipe_map2, root2, discard_map1, discard = day_10_parse_nodes("day-10/test_input2.txt")
pipe_map3, root3, full_map, dict_map1 = day_10_parse_nodes("day-10/test_input3.txt")
pipe_map4, root4, full_map2, dict_map2 = day_10_parse_nodes("day-10/test_input4.txt")


def test_day_10_p1() -> None:
    assert day_10_p_1(pipe_map, root)[0] == 4


def test_day_10_p1_input2() -> None:
    assert day_10_p_1(pipe_map2, root2)[0] == 8


discard_max_dist, node_list_part_2 = day_10_p_1(pipe_map3, root3)
discard_max_dist3, node_list_part_3 = day_10_p_1(pipe_map4, root4)


def test_day_10_p2() -> None:
    assert find_area(node_list_part_2, full_map, dict_map1) == 4


def test_day_10_p2_input2() -> None:
    assert find_area(node_list_part_3, full_map2, dict_map2) == 10


(find_area(node_list_part_3, full_map2, dict_map2))
