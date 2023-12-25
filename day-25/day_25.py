import re


class Graph:
    def __init__(self, all_nodes: list):
        self.num_nodes: int = len(all_nodes)
        self.data: list = all_nodes
        self.nodes: set = set()
        self.neighbours: dict = {}
        for node in all_nodes:  # connect coords, avoid # as not passable
            self.nodes.add(node[0])
            self.neighbours[node[0]] = set()
            for neighbour in node[1:]:
                self.neighbours[node[0]].add(neighbour)


def parse_input_1_node_per_line(input_file_name: str) -> Graph:
    input_as_list: list[str] = open(input_file_name, "r").readlines()
    output = [re.findall("[a-z]+", line) for line in input_as_list]
    made_into_graph: Graph = Graph(output)
    return made_into_graph


def bfs(graph_input: Graph, root):
    """
    Bog standard breadth first search to check for connections eventually.
    """
    # create a queue list
    queue = []
    discovered: dict = {}
    distance: dict = {}
    parent: dict = {}
    for node in graph_input.nodes:
        discovered[node] = False
        distance[node] = None
        parent[node] = None
    # mark each node as undiscovered
    # create list of distance of each node from root
    # create list of parents for each node

    # when discovered, mark that list entry with the root number/value
    discovered[root] = root
    discovery_order = [root]
    # then add the node (in this case the root) to the queue
    queue.append(root)
    # the root is distance 0 from itself
    distance[root] = 0

    while len(queue) > 0:
        # take value from front of queue
        current = queue.pop(0)

        # go through all the entries in list self.data for current node
        for node in graph_input.neighbours[current]:
            if discovered[node] is False:
                # its distance is 1+distance of parent node from root
                # breadth first search always goes to closest nodes first so as long as
                # this was previously undiscovered, it is correct
                distance[node] = 1 + distance[current]
                # add it to discovery order list
                discovery_order.append(node)
                discovered[node], parent[node] = node, current
                # add this node to the queue to examine its connected nodes too
                queue.append(node)
    return discovered, distance, parent, discovery_order


def check_connection(graph_input: Graph):
    """
    Check which nodes are connected. Will need to add a few bits to this e.g. rotating
    through all nodes as start root and adding outcome about length of list of undiscovered nodes etc.
    """
    discovered_nodes = bfs(graph_input, 0)[0]
    for x in discovered_nodes:
        if x is False:
            return False

    return True
