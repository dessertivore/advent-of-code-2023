from collections import defaultdict


def create_array(file_name: str) -> dict:
    input_as_list: list[str] = open(file_name, "r").readlines()
    output = [line.strip("\n") for line in input_as_list]
    grid: dict = {}
    x = 0
    for line in output:
        y = 0
        for char in line:
            grid[(x, y)] = char
            y += 1
        x += 1
    return grid


def follow_map(grid: dict, root=[(0, 1), (0, 0)]) -> int:
    # map where light beam goes to
    mapping_dict = {  # from the left
        (0, 1): {
            "/": (-1, 0),
            "\\": (1, 0),
            ".": "previous_direction",
            "|": [(1, 0), (-1, 0)],
            "-": "previous_direction",
        },
        # from the right
        (0, -1): {
            "/": (1, 0),
            "\\": (-1, 0),
            ".": "previous_direction",
            "|": [(1, 0), (-1, 0)],
            "-": "previous_direction",
        },
        # from above
        (1, 0): {
            "/": (0, -1),
            "\\": (0, 1),
            ".": "previous_direction",
            "|": "previous_direction",
            "-": [(0, -1), (0, 1)],
        },
        # from below
        (-1, 0): {
            "/": (0, 1),
            "\\": (0, -1),
            ".": "previous_direction",
            "|": "previous_direction",
            "-": [(0, -1), (0, 1)],
        },
    }
    # make map dict for where direction light beam comes from and what it has hit
    discovered: dict = defaultdict(
        list
    )  # store list of discovered coordinates and in which directions they were approached
    queue: list = []
    queue.append(root)
    discovered_order = []
    # queue items show current direction and current coord
    # starting coords are initialised as 0,0
    while len(queue) > 0:
        current = queue.pop(0)  # current coordinate
        current_coordinate = current[1]
        discovered_order.append(current_coordinate)
        current_direction = current[0]
        if (
            current_coordinate in grid.keys()
            and current_direction not in discovered[current_coordinate]
        ):
            character = grid[current_coordinate]
            # if we have already been to this tile, in this direction, move on to next queue item
            # to avoid infinite loop
            discovered[current_coordinate].append(current_direction)
            # mark current coordinate as discovered in that direction
            directions = mapping_dict[current_direction][
                character
            ]  # find next direction to go in
            if directions == "previous_direction":
                directions = current_direction
            if isinstance(directions, list):
                for direction in directions:
                    next_coord = tuple(
                        map(lambda i, j: i + j, current_coordinate, direction)
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
                    map(lambda i, j: i + j, current_coordinate, directions)
                )
                queue.append(
                    [
                        directions,
                        next_coord,
                    ]
                )
    return len(discovered.keys())


day_16_input = create_array("day-16/input.txt")
follow_map(day_16_input)


def part_2(grid: dict):
    """
    Cycle through all possible roots and find maximum number of energised tiles.
    """
    max_x = 0
    max_y = 0
    for key in grid.keys():  # find maximum xs and ys from grid dict
        max_x = max(max_x, key[0])
        max_y = max(max_y, key[1])
    # initialise a set of roots and directions to start the beam from
    roots = []

    y_coords_to_use = [0, (max_y - 1)]
    direction = (0, 1)
    # if y = 0, go right
    # if x is 0, go down
    # if y is max, go left
    # if x is max, go up
    for x in range(max_x):
        if x == 0 or x == (max_x - 1):
            # at edges, cycle through all y
            for y in range(max_y):
                if y == 0:
                    direction = (0, 1)
                elif y == max_y - 1:
                    direction = (0, -1)
                elif x == 0:
                    direction = (1, 0)
                elif x == max_x - 1:
                    direction = (-1, 0)
                roots.append([direction, (x, y)])
        else:
            # otherwise, only cycle through first and last y coord
            for y in y_coords_to_use:
                if y == 0:
                    direction = (0, 1)
                elif y == max_y - 1:
                    direction = (0, -1)
                roots.append([direction, (x, y)])
    max_energises = 0
    for root in roots:
        max_energises = max(follow_map(grid, root), max_energises)
    print(max_energises)
    return max_energises


part_2(day_16_input)
