from parse_input import parse_input_func_2


def lineLineIntersection(A, B, C, D, minimum, maximum):
    """
    Finds intersect of 2 lines based on start and end coordinate. Found online.
    """
    # Line AB represented as a1x + b1y = c1
    a1 = B[1] - A[1]
    b1 = A[0] - B[0]
    c1 = a1 * (A[0]) + b1 * (A[1])

    # Line CD represented as a2x + b2y = c2
    a2 = D[1] - C[1]
    b2 = C[0] - D[0]
    c2 = a2 * (C[0]) + b2 * (C[1])

    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        # The lines are parallel.
        return False

    else:
        x = (b2 * c1 - b1 * c2) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        if (
            min(A[0], B[0] <= int(x) not in range(min(A[0], B[0]), max(A[0], B[0])))
            or int(x) not in range(min(C[0], D[0]), max(C[0], D[0]))
            or int(y) not in range(min(A[1], B[1]), max(A[1], B[1]))
            or int(y) not in range(min(C[1], D[1]), max(C[1], D[1]))
            or int(x) not in range(minimum, maximum + 1)
            or int(y) not in range(minimum, maximum + 1)
        ):  # check if coordinates of intersect are within within test plot and are in future
            return False
        else:
            return (x, y)


def find_collision_course(
    hail_list: list, minimum: int, maximum: int, time: int = 90000000000000000000000000
) -> int:
    """
    For a list of hail particles, their coordinates and velocities, check if they will intersect
    in a specific timeframe and a specific test area of specified coordinates.
    Time is set to an arbitrary high number.
    """
    lines: dict = {}
    intersections: dict = {}
    counter = 0
    for (
        hail
    ) in (
        hail_list
    ):  # this bit initialises the start and endpoint of each trajectory for given timeframe
        x1, y1 = hail[0], hail[1]
        x_velocity = hail[3]
        y_velocity = hail[4]
        x_future, y_future = x1 + (x_velocity * time), y1 + (y_velocity * time)
        lines[(x1, y1)] = (x_future, y_future)
    for initial, endpoint in lines.items():
        for (
            initial_2,
            endpoint_2,
        ) in (
            lines.items()
        ):  # cycle through all combinations of hail particles which could collide
            if (
                initial_2 in intersections.keys()
                and initial in intersections[initial_2]
            ):  # don't recalculate if lines have already been found to have a collision
                continue
            else:
                intersection = lineLineIntersection(
                    initial, endpoint, initial_2, endpoint_2, minimum, maximum
                )
                if (
                    intersection
                ):  # intersection coordinates themselves are currently not stored
                    counter += 1  # lines which intersect are saved in a dict but also added to a counter
                    if initial not in intersections.keys():
                        intersections[initial] = {initial_2}
                    else:
                        intersections[initial].add(initial_2)

    return counter


day_24_input = parse_input_func_2("day-24/input.txt")
print(find_collision_course(day_24_input, 200000000000000, 400000000000000))
