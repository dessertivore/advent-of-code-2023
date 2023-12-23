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
        for (
            x_coord,
            y_coord,
        ) in grid.keys():  # connect garden plots, avoid # as not passable
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
    """
    Use memoisation to calculate how many different plots elf could end up on given
    a certain number of steps.
    Use a set so that there is no doubling up of coordinates saved.
    """
    places_possible: set = set()
    if steps_to_use == 0:
        return {start_node}
    else:
        for neighbour in graph.neighbours[start_node]:
            # check if this neighbour has already been visited with this number of remaining steps
            if ((steps_to_use - 1), neighbour) in memoisation_dict.keys():
                place = memoisation_dict[((steps_to_use - 1), neighbour)]
            else:  # if not, create list of possible locations to visit and save to dict
                memoisation_dict[((steps_to_use - 1), neighbour)] = reach_of_elf(
                    graph, (steps_to_use - 1), neighbour, memoisation_dict
                )
                place = memoisation_dict[((steps_to_use - 1), neighbour)]
            places_possible.update(place)
        return places_possible


# day_21_map: dict = create_array("day-21/input.txt")
# map_graph = Graph(day_21_map)
# start = find_start(day_21_map)
# print(len(reach_of_elf(map_graph, 64, start)))


def part_2(map: dict, steps_to_use: int, start_node, memoisation_dict: dict = {}):
    """
    Use memoisation to calculate how many different plots elf could end up on given
    a certain number of steps.
    Use a set so that there is no doubling up of coordinates saved.
    Do not use Graph class, but instead initialise neighbours in this function,
    as it is an infinite Graph otherwise.
    Need to fix this so all coordinates can be mapped to appropriate coordinate of initial
    map without having to plot the infinite farm.
    Use of modulo but still answer is wrong. To come back to later!
    """
    places_possible: set = set()
    if steps_to_use == 0:
        return {start_node}
    else:
        max_x = 0
        max_y = 0
        for x, y in map:
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        (
            x_coord,
            y_coord,
        ) = start_node  # connect garden plots, avoid # as not passable
        neighbours_set: set = set()
        if x_coord < 0:
            equivalent_x = max_x - (abs(x_coord) % max_x)
        elif x_coord >= 0:
            equivalent_x = x_coord % max_x
        if y_coord < 0:
            equivalent_y = max_y - (abs(y_coord) % max_y)
        elif y_coord >= 0:
            equivalent_y = y_coord % max_y
        if equivalent_x == max_x:
            if map[(0, equivalent_y)] != "#":
                neighbours_set.add((x_coord + 1, y_coord))
        elif map[(equivalent_x + 1, equivalent_y)] != "#":
            neighbours_set.add((x_coord + 1, y_coord))
        if equivalent_x == 0:
            if map[(max_x, equivalent_y)] != "#":
                neighbours_set.add((x_coord - 1, y_coord))
        elif map[(equivalent_x - 1, equivalent_y)] != "#":
            neighbours_set.add((x_coord - 1, y_coord))
        if equivalent_y == max_y:
            if map[(equivalent_x, 0)] != "#":
                neighbours_set.add((x_coord, y_coord + 1))
        elif map[(equivalent_x, equivalent_y + 1)] != "#":
            neighbours_set.add((x_coord, y_coord + 1))
        if equivalent_y == 0:
            if map[(equivalent_x, max_y)] != "#":
                neighbours_set.add((x_coord, y_coord - 1))
        elif map[(equivalent_x, equivalent_y - 1)] != "#":
            neighbours_set.add((x_coord, y_coord - 1))

        for neighbour in neighbours_set:
            # check if this neighbour has already been visited with this number of remaining steps
            if ((steps_to_use - 1), neighbour) in memoisation_dict.keys():
                place = memoisation_dict[((steps_to_use - 1), neighbour)]
            else:  # if not, create list of possible locations to visit and save to dict
                memoisation_dict[((steps_to_use - 1), neighbour)] = part_2(
                    map, (steps_to_use - 1), neighbour, memoisation_dict
                )
                place = memoisation_dict[((steps_to_use - 1), neighbour)]
            places_possible.update(place)
        return places_possible
