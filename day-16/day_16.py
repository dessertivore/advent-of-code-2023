from parse_input import parse_input_func


class Graph:
    def __init__(self, num_nodes: int, edges: list):
        self.num_nodes = num_nodes
        self.data: list = [[] for x in range(num_nodes)]
        for n1, n2 in edges:
            # create uni edge list - for each node creates a list of nodes
            # it is attached to (using (n1,n2) from each tuple)
            self.data[n1].append(n2)


def create_array(file_name: str) -> dict:
    grid: dict = {}
    x = 0
    for line in parse_input_func(file_name):
        y = 0
        for char in line:
            grid[(x, y)] = char
            y += 1
        x += 1
    return grid


def follow_map(grid: dict) -> int:
    # map where light beam goes to
    mapping_dict = {  # from the left
        (0, 1): {
            "/": (-1, 0),
            r"\\": (1, 0),
            ".": "previous_direction",
            "|": [(1, 0), (-1, 0)],
            "-": "previous_direction",
        },
        # from the right
        (0, -1): {
            "/": (1, 0),
            r"\\": (-1, 0),
            ".": "previous_direction",
            "|": [(1, 0), (-1, 0)],
            "-": "previous_direction",
        },
        # from above
        (1, 0): {
            "/": (0, -1),
            r"\\": (0, 1),
            ".": "previous_direction",
            "|": "previous_direction",
            "-": [(0, -1), (0, 1)],
        },
        # from below
        (-1, 0): {
            "/": (0, 1),
            r"\\": (0, -1),
            ".": "previous_direction",
            "|": "previous_direction",
            "-": [(0, -1), (0, 1)],
        },
    }
    # make map dict for where direction light beam comes from and what it has hit
    discovered = {set}
    queue: list = []
    queue.append([(0, 1), (0, 0)])
    discovered_order = []
    # queue items show current direction and current coord
    # starting coords are initialised as 0,0
    while len(queue) > 0:
        current = queue.pop(0)  # current coordinate
        current_coordinate = current[1]
        discovered_order.append(current_coordinate)
        current_direction = current[0]
        if current_coordinate in grid.keys():
            character = grid[current_coordinate]
        else:
            break
        discovered.add(current_coordinate)  # mark current coordinate as discovered
        directions = mapping_dict[current_direction][
            character
        ]  # find next direction to go in
        if directions == "previous_direction":
            directions = current_direction
        if isinstance(directions, list):
            for direction in directions:
                next_coord = tuple(
                    map(lambda i, j: i + j, current_coordinate, current_direction)
                )
                queue.append(
                    [
                        direction,
                        next_coord,
                    ]
                )
                # add to queue list with direction of light and coordinate of next place light goes to
        else:
            next_coord = tuple(
                map(lambda i, j: i + j, current_coordinate, current_direction)
            )
            queue.append(
                [
                    directions,
                    next_coord,
                ]
            )
    return len(discovered), discovered_order
