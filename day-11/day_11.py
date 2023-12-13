from collections import defaultdict


def day_11(star_map_file: str) -> (int, int):
    """
    Find shortest distance between galaxies in map, where galaxy is #.
    """
    galaxy_map: list = open(star_map_file, "r").readlines()
    galaxy_map = [[_ for _ in line.strip("\n")] for line in galaxy_map]
    line_count: int = 0
    galaxy_num: int = 1
    galaxy_dict: defaultdict = defaultdict()
    all_stops_y: dict = {}
    for i in range(len(galaxy_map)):  # set all_full_stops as true to start with
        all_stops_y[i] = True
    all_stops_x: defaultdict = defaultdict()
    for (
        line
    ) in (
        galaxy_map
    ):  # go through all characters in map and check for galaxies and empty lines/columns
        all_stops_x[line_count] = True
        char_count: int = 0
        for char in line:
            if char != ".":
                all_stops_x[line_count] = False
                all_stops_y[char_count] = False
            if char == "#":
                galaxy_dict[galaxy_num] = [
                    line_count,
                    char_count,
                ]  # add galaxies to a dictionary with their coords
                galaxy_num += 1
            char_count += 1
        # if all_stops:
        #     galaxy_map.insert(line_count, line)
        line_count += 1
    shortest_path: dict = {}
    for starting_galaxy in range(1, len(galaxy_dict.keys()) + 1):
        end: int = starting_galaxy + 1
        while end < len(galaxy_dict.keys()) + 1:
            # Find range of coordinates within path, add to dist if row/column is empty

            dist = abs(galaxy_dict[end][1] - galaxy_dict[starting_galaxy][1]) + abs(
                galaxy_dict[end][0] - galaxy_dict[starting_galaxy][0]
            )  # subtract coord1 from coord2 to find dist
            max_x = max(galaxy_dict[end][0], galaxy_dict[starting_galaxy][0])
            max_y = max(galaxy_dict[end][1], galaxy_dict[starting_galaxy][1])
            min_x = min(galaxy_dict[end][0], galaxy_dict[starting_galaxy][0])
            min_y = min(galaxy_dict[end][1], galaxy_dict[starting_galaxy][1])
            # find range of x and y values in path
            for x in range(min_x, max_x):
                if all_stops_x[x]:
                    dist += 1000000 - 1
            for y in range(
                min_y, max_y
            ):  # add extra distance for each empty row/column
                if all_stops_y[y]:
                    dist += 1000000 - 1
                    # change this to 1 for part 1, instead of 1000000 - 1

            shortest_path[(starting_galaxy, end)] = dist
            end += 1
        starting_galaxy += 1
    return galaxy_num, sum(shortest_path.values())


print(day_11("day-11/input.txt"))
