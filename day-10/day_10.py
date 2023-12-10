from collections import defaultdict


class Graph:
    def __init__(self, num_nodes: int, edges: list):
        self.num_nodes = num_nodes
        self.data: defaultdict = defaultdict(lambda: set())
        # default dict will create empty set at that key if key does not exist yet
        for n1, n2 in edges:
            # create unidirectional edge list - for each node creates a set of nodes
            # it is attached to (using (n1,n2) from each tuple)
            self.data[n1].add(n2)

    def add_edge(self, new_edge: tuple):
        if len(new_edge) != 2:
            raise ValueError("Node must be tuple of 2")
        # unpack tuple
        n1, n2 = new_edge
        self.num_nodes += 1
        self.data[n1].add(n2)


def day_10_parse_nodes(file_name: str) -> tuple[Graph, int]:
    """
    Convert each pipe to location coordinates (x,y) and connect it to other pipes.
    """
    converter_dict: dict = {
        "|": [(0, -1), (0, 1)],
        "-": [(1, 0), (-1, 0)],
        "L": [(0, -1), (1, 0)],
        "J": [(0, -1), (-1, 0)],
        "7": [(0, 1), (-1, 0)],
        "F": [(0, 1), (1, 0)],
        ".": [(0, 0)],
    }
    input_as_list: list[str] = open(file_name, "r").readlines()
    y_coord = -1  # will start at coordinates 0,0 once +1 at start
    pipe_map = None
    for line in input_as_list:
        y_coord += 1
        x_coord = -1  # re initialise x at every line
        for char in line:
            x_coord += 1
            coord: tuple = (x_coord, y_coord)
            if char == "S":
                root = coord
            if char in converter_dict:
                edges: list = converter_dict[char]
                for edge in edges:
                    next_pipe = tuple(
                        map(sum, zip(coord, edge))
                    )  # add the tuples together
                    if pipe_map is None:
                        pipe_map = Graph(2, [(coord), (next_pipe)])
                    else:
                        if edge == (0, 0):
                            continue
                        else:
                            pipe_map.add_edge((coord, next_pipe))
    root_edges = []
    """
    We do not know what pipe type root is, so we assume it is connected to all pipes which
    connect to it.
    """
    for node in pipe_map.data.keys():
        if root in pipe_map.data[node]:
            root_edges.append(node)
    for root_edge in root_edges:
        pipe_map.add_edge((root, root_edge))
    return pipe_map, root


def day_10_p_1(graph_input: Graph, root):
    """
    Breadth first search to find furthest node
    """
    # create a queue list
    queue = []
    # create set of discovered nodes
    discovered: set = set()
    # create list of distance of each node from root
    distance: defaultdict = defaultdict(int)
    # when discovered, mark that list entry with the root number/value
    discovered.add(root)
    discovery_order = [root]
    # then add the node (in this case the root) to the queue
    queue.append(root)
    # the root is distance 0 from itself
    distance[root] = 0

    while len(queue) > 0:
        # take value from front of queue
        current = queue.pop(0)

        # go through all the entries in list self.data for current node
        for node in graph_input.data[current]:
            if node not in discovered:
                # its distance is 1+distance of parent node from root
                # breadth first search always goes to closest nodes first so as long as
                # this was previously undiscovered, it is correct
                distance[node] = 1 + distance[current]
                # add it to discovery order list
                discovery_order.append(node)
                discovered.add(node)
                # add this node to the queue to examine its connected nodes too
                queue.append(node)
    max_distance = max(distance.values())
    return max_distance


input1, input2 = day_10_parse_nodes("day-10/input.txt")
print(day_10_p_1(input1, input2))
