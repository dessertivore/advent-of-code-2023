from parse_input import create_array
from collections import defaultdict


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
        for (
            x_coord,
            y_coord,
        ) in grid.keys():  # connect coords, avoid # as not passable
            neighbours_set: set = set()
            if (
                grid[(x_coord, y_coord)] == ">"
                and grid[(x_coord, y_coord + 1)] != "#"
                and y_coord < self.max_y
            ):
                neighbours_set.add((x_coord, y_coord + 1))
            if (
                grid[(x_coord, y_coord)] == "<"
                and grid[(x_coord, y_coord - 1)] != "#"
                and y_coord > 0
            ):
                neighbours_set.add((x_coord, y_coord - 1))
            if (
                grid[(x_coord, y_coord)] == "v"
                and grid[(x_coord + 1, y_coord)] != "#"
                and x_coord < self.max_x
            ):
                neighbours_set.add((x_coord + 1, y_coord))
            if grid[(x_coord, y_coord)] == ".":
                if x_coord < self.max_x and grid[(x_coord + 1, y_coord)] != "#":
                    neighbours_set.add((x_coord + 1, y_coord))
                if x_coord > 0 and grid[(x_coord - 1, y_coord)] != "#":
                    neighbours_set.add((x_coord - 1, y_coord))
                if y_coord < self.max_y and grid[(x_coord, y_coord + 1)] != "#":
                    neighbours_set.add((x_coord, y_coord + 1))
                if y_coord > 0 and grid[(x_coord, y_coord - 1)] != "#":
                    neighbours_set.add((x_coord, y_coord - 1))
            if x_coord == self.max_x and y_coord == self.max_y - 1:
                neighbours_set.add((0, 1))
            self.neighbours[(x_coord, y_coord)] = neighbours_set


def find_start(grid: Graph, start_node="S"):
    for key, value in grid.data.items():
        if key[0] == 0 and value == start_node:
            return key
    pass


# Function to traverse the DAG
# and apply Dynamic Programming
# to find the longest path
def dfs(
    grid: Graph, start_node: tuple, dp: dict, visited: set, visited_order: list = []
):
    # Mark as visited
    visited.add(start_node)
    visited_order.append(start_node)
    # Traverse for all its children
    for neighbour in grid.neighbours[start_node]:
        # If not visited
        if neighbour not in visited:
            dfs(grid, neighbour, dp, visited, visited_order)

            # Store the max of the paths
            dp[start_node] = max(dp[start_node], 1 + dp[neighbour])
            if neighbour == (grid.max_x, grid.max_y - 1):
                break


# Function that returns the longest path
def find_scenic_walk(grid: Graph, start_node: tuple):
    """
    This does not work :( To retry at later date.
    """
    # Dp stored as dict
    dp: dict = defaultdict(lambda: 0)
    visited: set = set()
    visited_order: list = []
    # Visited array to know if the node
    # has been visited previously or not

    # Call DFS for every unvisited vertex
    # for i in grid.data.keys():
    #     node = i
    #     if node not in visited:
    dfs(grid, start_node, dp, visited, visited_order)

    ans = 0

    # Traverse and find the maximum of all dp[i]
    for i in dp.keys():
        ans = max(ans, dp[i])

    return ans, len(visited)
