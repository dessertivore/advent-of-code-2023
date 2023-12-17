from collections import defaultdict


def parse_input_func(input_file_name: str) -> list:
    input_as_list: list[str] = open(input_file_name, "r").readlines()
    ouput = [line.strip("\n") for line in input_as_list]
    return ouput


parse_input_func("day-17/input.txt")


class Graph:
    def __init__(self, grid: list):
        self.num_nodes = len(grid) * len(grid[0])
        self.grid = grid
        self.data: dict = defaultdict(dict)
        for x_coordinate, list in enumerate(grid):
            for y_coordinate, y_num in enumerate(grid):
                # # create unidirectional weighted edge list - for each node creates a list
                # # of edges to nodes around it.
                # # there are edges between nodes, but also up to 3 edges are concatenated into 1
                # # as that is how far the crucible can go straight at once.
                # if y_coordinate < len(grid[0]) - 3:
                #     self.data[(x_coordinate, y_coordinate)][
                #         (x_coordinate, y_coordinate + 3)
                #     ] = (
                #         grid[x_coordinate][y_coordinate + 1]
                #         + grid[x_coordinate][y_coordinate + 2]
                #         + grid[x_coordinate][y_coordinate + 3]
                #     )
                # if x_coordinate < len(grid) - 3:
                #     self.data[(x_coordinate, y_coordinate)][
                #         (x_coordinate + 3, y_coordinate)
                #     ] = (
                #         grid[x_coordinate + 1][y_coordinate]
                #         + grid[x_coordinate + 2][y_coordinate]
                #         + grid[x_coordinate + 3][y_coordinate]
                #     )
                # if x_coordinate > 3:
                #     self.data[(x_coordinate, y_coordinate)][
                #         (x_coordinate - 3, y_coordinate)
                #     ] = (
                #         grid[x_coordinate - 1][y_coordinate]
                #         + grid[x_coordinate - 2][y_coordinate]
                #         + grid[x_coordinate - 3][y_coordinate]
                #     )
                # if y_coordinate > 3:
                #     self.data[(x_coordinate, y_coordinate)][
                #         (x_coordinate, y_coordinate - 3)
                #     ] = (
                #         grid[x_coordinate][y_coordinate - 1]
                #         + grid[x_coordinate][y_coordinate - 2]
                #         + grid[x_coordinate][y_coordinate - 3]
                #     )

                # if y_coordinate < len(grid[0]) - 2:
                #     self.data[(x_coordinate, y_coordinate)][
                #         (x_coordinate, y_coordinate + 2)
                #     ] = (
                #         grid[x_coordinate][y_coordinate + 1]
                #         + grid[x_coordinate][y_coordinate + 2]
                #     )
                # if x_coordinate < len(grid) - 2:
                #     self.data[(x_coordinate, y_coordinate)][
                #         (x_coordinate + 2, y_coordinate)
                #     ] = (
                #         grid[x_coordinate + 1][y_coordinate]
                #         + grid[x_coordinate + 2][y_coordinate]
                #     )
                # if x_coordinate > 2:
                #     self.data[(x_coordinate, y_coordinate)][
                #         (x_coordinate - 2, y_coordinate)
                #     ] = (
                #         grid[x_coordinate - 1][y_coordinate]
                #         + grid[x_coordinate - 2][y_coordinate]
                #     )
                # if y_coordinate > 2:
                #     self.data[(x_coordinate, y_coordinate)][
                #         (x_coordinate, y_coordinate - 2)
                #     ] = (
                #         grid[x_coordinate][y_coordinate - 1]
                #         + grid[x_coordinate][y_coordinate - 2]
                #     )

                if y_coordinate < len(grid[0]) - 1:
                    self.data[(x_coordinate, y_coordinate)][
                        (x_coordinate, y_coordinate + 1)
                    ] = grid[x_coordinate][y_coordinate + 1]
                if x_coordinate < len(grid) - 1:
                    self.data[(x_coordinate, y_coordinate)][
                        (x_coordinate + 1, y_coordinate)
                    ] = grid[x_coordinate + 1][y_coordinate]
                if x_coordinate - 1 >= 0:
                    self.data[(x_coordinate, y_coordinate)][
                        (x_coordinate - 1, y_coordinate)
                    ] = grid[x_coordinate - 1][y_coordinate]
                if y_coordinate - 1 >= 0:
                    self.data[(x_coordinate, y_coordinate)][
                        (x_coordinate, y_coordinate - 1)
                    ] = grid[x_coordinate][y_coordinate - 1]

    # def add_edge(self, new_edge: tuple):
    #     if len(new_edge) != 2:
    #         raise ValueError("Node must be tuple of 2")
    #     # unpack tuple
    #     n1, n2 = new_edge

    #     if n1 < 0 or n2 < 0:
    #         # Check that the node IDs are within the valid range
    #         raise ValueError("Node IDs must be more than 0")

    #     # Update num_nodes if necessary
    #     if n1 >= self.num_nodes or n2 >= self.num_nodes:
    #         self.num_nodes = max(n1, n2) + 1  # Update the number of nodes
    #         self.data.extend([] for _ in range((self.num_nodes) - len(self.data)))

    #     self.data[n1].append(n2)
    #     self.data[n2].append(n1)


def dijkstra_algorithm(weighted_graph: Graph, start_node: tuple = (0, 0)) -> dict:
    """
    Find best path from top left to bottom right of grid, with weighted edges ('heat accumulation').
    This is currently an absolute mess, as the 'crucible' cannot go more than 3 steps in any direction
    and I am in the process of solving for this still.
    """
    unvisited_nodes = set(x for x in weighted_graph.data.keys())
    # create list of shortest paths, and initialize value of the unvisited nodes as infinity
    shortest_path: dict = defaultdict(lambda: float("inf"))
    # However, we initialize the starting node's value with 0
    shortest_path[start_node] = 0
    movement_since_turn: tuple = (0, 0)

    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes: dict = defaultdict()

    max_x = 0
    max_y = 0
    for x, y in weighted_graph.data.keys():
        max_x = max(x, max_x)
        max_y = max(y, max_y)
    # The algorithm executes until we visit bottom right
    while (max_x, max_y) in unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes:  # Iterate over the nodes
            if (
                current_min_node == None
                or shortest_path[node] < shortest_path[current_min_node]
            ):
                current_min_node = node
                x = current_min_node[0]
                y = current_min_node[1]
                # retrieve the current node's neighbors
                neighbours: dict = defaultdict()
                for key in weighted_graph.data[current_min_node].keys():
                    neighbours[key] = weighted_graph.data[current_min_node][key]
                if (movement_since_turn[0]) > 2 and (x + 1, y) in neighbours.keys():
                    del neighbours[(x + 1, y)]
                    movement_since_turn = (0, movement_since_turn[1])
                if movement_since_turn[0] < -2 and (x - 1, y) in neighbours.keys():
                    del neighbours[(x - 1, y)]
                    movement_since_turn = (0, movement_since_turn[1])
                if (movement_since_turn[1]) > 2 and (x, y + 1) in neighbours.keys():
                    del neighbours[(x, y + 1)]
                    movement_since_turn = (movement_since_turn[0], 0)
                if movement_since_turn[1] < -2 and (x, y - 1) in neighbours.keys():
                    del neighbours[(x, y - 1)]
                    movement_since_turn = (movement_since_turn[0], 0)
                # update distances for neighbours - weight of edge + current distance to get there
                for neighbour in neighbours:
                    # extract weight for neighbour node edge
                    for neighbour_weight in weighted_graph.data[current_min_node][
                        neighbour
                    ]:
                        tentative_value = shortest_path[current_min_node] + int(
                            neighbour_weight
                        )
                        direction = tuple(
                            map(lambda i, j: i + j, current_min_node, neighbour)
                        )
                        movement_since_turn = tuple(
                            map(lambda i, j: i + j, movement_since_turn, direction)
                        )
                        if tentative_value < shortest_path[neighbour]:
                            shortest_path[neighbour] = tentative_value
                            # We also update the best path to the current node
                            previous_nodes[neighbour] = current_min_node

        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)

    print(shortest_path[(max_x, max_y)])
    return shortest_path[(max_x, max_y)]
