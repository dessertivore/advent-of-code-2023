# def parse_as_list(file_name: str) -> list:
#     grid = []
#     with open(file_name, "r") as file:
#         lines: list[str] = file.read().split("\n\n")
#     for line in lines:
#         grid.append(line.split("\n"))
#     return grid


# def find_symmetry(grid: list) -> list:
#     pivots: list = [[], []]
#     # store data about each map's pivot point in a list. x pivots in [0], y pivots in [1]
#     for lava_map in grid:
#         y_pivot_idx: int = 1
#         x_pivot_idx: int = 1

#         pivot_found: bool = False
#         while y_pivot_idx < len(lava_map[1]) and not pivot_found:
#             for line in lava_map:
#                 left = line[:y_pivot_idx]
#                 right = line[y_pivot_idx:][::-1]  # reverse right side

#                 if left[: len(right)] == right[: len(left)]:
#                     pivot_found = True
#                 else:
#                     pivot_found = False
#                     y_pivot_idx += 1
#             if pivot_found:
#                 pivots[1].append(y_pivot_idx)
#                 break
#         while x_pivot_idx < len(lava_map) and not pivot_found:
#             upper = lava_map[:x_pivot_idx]
#             lower = lava_map[x_pivot_idx:]
#             for x in lower[: len(upper)][::-1]:
#                 for y in upper[: len(lower)]:
#                     if x == y:
#                         pivot_found = True
#                     else:
#                         pivot_found - False
#                         x_pivot_idx += 1
#                         break
#             if pivot_found:
#                 pivots[0].append(x_pivot_idx)


#     return pivots


# maps = parse_as_list("day-13/input.txt")
# symm = find_symmetry(maps)
# print(symm, len(symm[1]))


def parse_input(file_name: str) -> list:
    """
    Make dict of coordinates for each # within each map
    """
    lines: list[str] = open(file_name, "r").readlines()
    lava_coords: list = [[set()]]
    x_coord = 0
    map_number = 0
    for line in lines:
        if line == "\n":
            lava_coords[map_number].insert(
                0, (x_coord - 1, y_coord - 1)
            )  # make note of maximum x and y coords
            map_number += 1
            lava_coords.append([set()])
            x_coord = 0
            y_coord = 0

        else:
            y_coord = -1

            for char in line:
                y_coord += 1
                if char == "#":
                    lava_coords[map_number][0].add(
                        (x_coord, y_coord)
                    )  # add all coordinates of lava to a set for each map
            x_coord += 1
    return lava_coords[:-1]


def find_rotation(lava_coords: list) -> list:
    """
    Given a number of inputs, output the line of symmetry for each one, whether on x or y axis
    """
    pivots: list = [[], []]
    # store data about each map's pivot point in a list. x pivots in [0], y pivots in [1]
    for lava_map in lava_coords:
        max_coords: tuple = lava_map[0]  # i have stored max x and max y at index [0]
        y_pivot_idx: float = 0.5
        pivot_found: bool = False

        while y_pivot_idx < max_coords[1] and not pivot_found:
            for lava_coords in lava_map[1]:
                difference = y_pivot_idx - lava_coords[1]

                new_var = (lava_coords[0], int(y_pivot_idx + difference))
                if (
                    int(y_pivot_idx + difference) in range(0, max_coords[1] + 1)
                    and new_var not in lava_map[1]
                ):
                    pivot_found = False
                    y_pivot_idx += 1
                    break
                else:
                    pivot_found = True
        if pivot_found:
            pivots[1].append(y_pivot_idx)

        x_pivot_idx: float = 0.5

        while (
            x_pivot_idx < max_coords[0] and not pivot_found
        ):  # iterate through horizontal lines of symmetry if nil vertical ones
            for lava_coords in lava_map[1]:
                difference = x_pivot_idx - lava_coords[0]
                if (
                    int(x_pivot_idx + difference) in range(0, max_coords[0] + 1)
                    and (int(x_pivot_idx + difference), lava_coords[1])
                    not in lava_map[1]
                ):
                    pivot_found = False
                    x_pivot_idx += 1
                    break
                else:
                    pivot_found = True
            if pivot_found:
                pivots[0].append(x_pivot_idx)
    return pivots


def sum_pivots(pivots: list) -> int:
    """
    Sum of lines to left of vertical symmetry lines, and sum of 100*lines above horizontal ones.
    """
    total_x = 0
    total_y = 0
    for x_pivot in pivots[0]:
        total_x += int(x_pivot + 0.5)
    for y_pivot in pivots[1]:
        total_y += int(y_pivot + 0.5)
    total = total_y + (total_x * 100)
    return total


# print(sum_pivots(symm))
# maps1 = parse_input("day-13/input.txt")
# # print(maps[0])
# pivots = find_rotation(maps1)
# print(pivots)
# print(len(pivots[0]) + len(pivots[1]), pivots)
# print(sum_pivots(pivots))
