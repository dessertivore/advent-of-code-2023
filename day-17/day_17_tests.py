from day_17 import Graph, dijkstra_algorithm, parse_input_func


test_graph = Graph(parse_input_func("day-17/test_input.txt"))
assert dijkstra_algorithm(test_graph) == 105
