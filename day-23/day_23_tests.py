from parse_input import create_array
from day_23 import find_start, find_scenic_walk, Graph

test_map: dict = create_array("day-23/test_input.txt")
test_map_graph: Graph = Graph(test_map)
start = find_start(test_map_graph, ".")
print(start)
print(find_scenic_walk(test_map_graph, start))
# assert find_scenic_walk(test_map_graph, start) == 94
