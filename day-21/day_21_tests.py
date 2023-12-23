from day_21 import reach_of_elf, find_start, Graph, part_2
from parse_input import create_array

test_map: dict = create_array("day-21/test_input.txt")
start = find_start(test_map)

test_map_graph = Graph(test_map)

assert len(reach_of_elf(test_map_graph, 1, start)) == 2

assert len(reach_of_elf(test_map_graph, 6, start)) == 16

print(len((part_2(test_map, 50, start))))
