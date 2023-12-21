from parse_input import create_array


def find_start(grid: dict, start_node="S"):
    for key, value in grid.items():
        if value == start_node:
            return key
    pass


class Graph:
    def __init__(self, grid: dict):
        self.num_nodes = len(grid.values())
        self.data = grid
        self.neighbours: dict = {}
        self.max_x = 0
        self.max_y = 0
        for x, y in grid:
            self.max_x = max(self.max_x, x)
            self.max_y = max(self.max_y, y)
        for x_coord, y_coord in grid.keys():  # connect garden plots
            neighbours_set: set = set()
            if x_coord < self.max_x and grid[(x_coord + 1, y_coord)] != "#":
                neighbours_set.add((x_coord + 1, y_coord))
            if x_coord > 0 and grid[(x_coord - 1, y_coord)] != "#":
                neighbours_set.add((x_coord - 1, y_coord))
            if y_coord < self.max_y and grid[(x_coord, y_coord + 1)] != "#":
                neighbours_set.add((x_coord, y_coord + 1))
            if y_coord > 0 and grid[(x_coord, y_coord - 1)] != "#":
                neighbours_set.add((x_coord, y_coord - 1))
            self.neighbours[(x_coord, y_coord)] = neighbours_set


def reach_of_elf(
    graph: Graph, steps_to_use: int, start_node, memoisation_dict: dict = {}
):
    # memoisation_dict: dict = {}
    places_possible: set = set()
    if steps_to_use == 0:
        # memoisation_dict[((steps_to_use), start_node)] = {start_node}
        # places_possible: set = {start_node}
        return {start_node}
    else:
        for neighbour in graph.neighbours[start_node]:
            # place: set = reach_of_elf(graph, (steps_to_use - 1), neighbour)
            if ((steps_to_use - 1), neighbour) in memoisation_dict.keys():
                place = memoisation_dict[((steps_to_use - 1), neighbour)]
            else:
                memoisation_dict[((steps_to_use - 1), neighbour)] = reach_of_elf(
                    graph, (steps_to_use - 1), neighbour, memoisation_dict
                )
                place = memoisation_dict[((steps_to_use - 1), neighbour)]
            places_possible.update(place)
        return places_possible


day_21_map: dict = create_array("day-21/input.txt")
map_graph = Graph(day_21_map)
start = find_start(day_21_map)
print(len(reach_of_elf(map_graph, 64, start)))

# def reach_of_elf(graph: Graph, steps_to_use: int, start="S"):
#     #    def dijkstra_algorithm(graph, start_node):
#     unvisited_nodes = list(graph.data.keys())

#     # We'll use this dict to save the cost of visiting each node and update it as we move along the graph
#     shortest_path = {}

#     # We'll use this dict to save the shortest known path to a node found so far
#     previous_nodes = {}

#     # We'll use max_value to initialize the "infinity" value of the unvisited nodes
#     max_value = float("inf")
#     for node in unvisited_nodes:
#         shortest_path[node] = max_value
#     # However, we initialize the starting node's value with 0
#     start_node: tuple = find_start(graph.data, start)
#     print(start_node)
#     shortest_path[start_node] = 0

#     # The algorithm executes until we visit all nodes
#     while unvisited_nodes:
#         # The code block below finds the node with the lowest score
#         current_min_node = None
#         for node in unvisited_nodes:  # Iterate over the nodes
#             if current_min_node == None:
#                 current_min_node = node
#             elif shortest_path[node] < shortest_path[current_min_node]:
#                 current_min_node = node

#         # The code block below retrieves the current node's neighbors and updates their distances
#         if current_min_node in graph.neighbours.keys():
#             neighbours = graph.neighbours[current_min_node]
#             for neighbour in neighbours:
#                 tentative_value = shortest_path[current_min_node] + 1
#                 if tentative_value < shortest_path[neighbour]:
#                     shortest_path[neighbour] = tentative_value
#                     # We also update the best path to the current node
#                     previous_nodes[neighbour] = current_min_node

#         # After visiting its neighbors, we mark the node as "visited"
#         unvisited_nodes.remove(current_min_node)
#     # to get list of nodes visited in order, return previous_nodes too
#     possible_places = 0
#     for x in shortest_path.values():
#         if x == steps_to_use:
#             possible_places += 1
#     return possible_places
