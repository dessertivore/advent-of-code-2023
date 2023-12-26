from parse_input import create_array
from collections import defaultdict


def find_rocks_and_round_rocks(input_map: dict) -> tuple:
    """
    Convert parsed input (as list) into set/dict of immovable and movable rocks. In this case,
    movable rocks are O and immovable rocks are #.
    """
    max_x = 0
    max_y = 0
    round_rocks: set = set()
    rocks_by_x: dict = defaultdict(lambda: [])
    rocks_by_y: dict = defaultdict(lambda: [])
    for coord, item in input_map.items():
        max_x = max(max_x, coord[0])
        max_y = max(max_y, coord[1])
        if item == "O":
            round_rocks.add(coord)
        if item == "#":
            rocks_by_x[coord[0]].append(coord)
            rocks_by_y[coord[1]].append(coord)

    return round_rocks, rocks_by_x, rocks_by_y, max_x, max_y


def move_rocks_north(round_rocks: set, rocks_by_y: dict) -> set:
    """
    Move all round rocks ("O") as far up as possible.
    """
    new_round_rocks: set = set()
    for round_rock in round_rocks:
        x = round_rock[0]
        y = round_rock[1]
        closest_rock_x = 0
        no_rocks_in_way = True
        if y in rocks_by_y.keys():  # check if any rocks on same y coord
            for rock in rocks_by_y[y]:
                # go through all the cube rocks and find the one closest on x axis, and on same y axis
                if rock[0] < x:
                    no_rocks_in_way = False
                    closest_rock_x = max(closest_rock_x, rock[0])
        if no_rocks_in_way:  # if no rocks in way, go to x=0, unless another rock there
            while (
                closest_rock_x,
                y,
            ) in new_round_rocks:  # if there is already a rock in that place, it will have to go behind it
                closest_rock_x += 1
            new_round_rocks.add((closest_rock_x, y))
        else:
            while (
                closest_rock_x + 1,
                y,
            ) in new_round_rocks:  # if there is already a rock in that place, it will have to go behind it
                closest_rock_x += 1
            new_round_rocks.add((closest_rock_x + 1, y))
    return new_round_rocks


def calculate_load(round_rocks: set, max_x: int) -> int:
    """
    Calculate load on beams as specified in advent problem.
    Distance from bottom of beams dictates what load multiplier is.
    """
    load_per_row: dict = defaultdict(lambda: 0)
    for round_rock in round_rocks:
        load_per_row[round_rock[0]] += 1
    total_load = 0
    for coord, rock_num in load_per_row.items():
        multiplier = max_x + 1 - coord
        total_load += rock_num * multiplier
    return total_load


def move_rocks_south(round_rocks: set, rocks_by_y: dict, max_x: int) -> set:
    """
    Move all round rocks ("O") as far down as possible.
    """
    new_round_rocks: set = set()
    for round_rock in round_rocks:
        x = round_rock[0]
        y = round_rock[1]
        closest_rock_x = max_x
        no_rocks_in_way = True
        if y in rocks_by_y.keys():
            for rock in rocks_by_y[y]:
                # go through all the cube rocks and find the one closest on x axis, and on same y axis
                if rock[0] > x:
                    closest_rock_x = min(closest_rock_x, rock[0])
                    no_rocks_in_way = False
        if no_rocks_in_way:  # if no rocks in way, go to x=0, unless another rock there
            while (
                closest_rock_x,
                y,
            ) in new_round_rocks:  # if there is already a rock in that place, it will have to go behind it
                closest_rock_x -= 1
            new_round_rocks.add((closest_rock_x, y))
        else:
            while (
                closest_rock_x - 1,
                y,
            ) in new_round_rocks:  # if there is already a rock in that place, it will have to go behind it
                closest_rock_x -= 1
            new_round_rocks.add((closest_rock_x - 1, y))
    return new_round_rocks


def move_rocks_east(round_rocks: set, rocks_by_x: dict, max_y: int) -> set:
    """
    Move all round rocks ("O") as far right as possible.
    """
    new_round_rocks: set = set()
    for round_rock in round_rocks:
        x = round_rock[0]
        y = round_rock[1]
        closest_rock_y = max_y
        no_rocks_in_way = True
        if x in rocks_by_x.keys():
            for rock in rocks_by_x[x]:
                # go through all the cube rocks and find the one closest on x axis, and on same y axis
                if rock[1] > y:
                    closest_rock_y = min(closest_rock_y, rock[1])
                    no_rocks_in_way = False
        if (
            no_rocks_in_way
        ):  # if no rocks in way, go to y=max_y, unless another rock there
            while (
                x,
                closest_rock_y,
            ) in new_round_rocks:  # if there is already a rock in that place, it will have to go behind it
                closest_rock_y -= 1
            new_round_rocks.add((x, closest_rock_y))
        else:
            while (
                x,
                closest_rock_y - 1,
            ) in new_round_rocks:  # if there is already a rock in that place, it will have to go behind it
                closest_rock_y -= 1
            new_round_rocks.add((x, closest_rock_y - 1))
    return new_round_rocks


def move_rocks_west(round_rocks: set, rocks_by_x: dict) -> set:
    """
    Move all round rocks ("O") as far left as possible.
    """
    new_round_rocks: set = set()
    for round_rock in round_rocks:
        x = round_rock[0]
        y = round_rock[1]
        closest_rock_y = 0
        no_rocks_in_way = True
        if x in rocks_by_x.keys():
            for rock in rocks_by_x[
                x
            ]:  # go through all the cube rocks and find the one closest on x axis, and on same y axis
                if rock[1] < y:
                    closest_rock_y = max(closest_rock_y, rock[1])
                    no_rocks_in_way = False
        if no_rocks_in_way:  # if no rocks in way, go to x=0, unless another rock there
            while (
                x,
                closest_rock_y,
            ) in new_round_rocks:  # if there is already a rock in that place, it will have to go behind it
                closest_rock_y += 1
            new_round_rocks.add((x, closest_rock_y))
        else:
            while (
                x,
                closest_rock_y + 1,
            ) in new_round_rocks:  # if there is already a rock in that place, it will have to go behind it
                closest_rock_y += 1
            new_round_rocks.add((x, closest_rock_y + 1))
    return new_round_rocks


def spin_cycle(
    round_rocks: set,
    rocks_by_x: dict,
    rocks_by_y: dict,
    max_x: int,
    max_y: int,
    num_spin: int,
):
    """
    Spin the rocks in a circle a specified number of times. Calculate load after this.
    Load numbers repeat, therefore no need to actually spin this number of times.
    Instead, find the repeating sequence of loads, and extrapolate what the load after
    x spins must be.
    """
    current_round_rocks = round_rocks
    current_spin = 0
    load_tracker: list = []
    match_found = False
    while current_spin <= 300:
        current_spin += 1
        current_round_rocks = move_rocks_north(current_round_rocks, rocks_by_y)
        current_round_rocks = move_rocks_west(current_round_rocks, rocks_by_x)
        current_round_rocks = move_rocks_south(current_round_rocks, rocks_by_y, max_x)
        current_round_rocks = move_rocks_east(current_round_rocks, rocks_by_x, max_y)
        current_load = calculate_load(current_round_rocks, max_x)
        load_tracker.append(current_load)
        if current_load in load_tracker:
            if match_found == False and current_spin > 200:
                # spin for arbitrary large number of cycles to allow for pattern to commence
                # before checking for match
                match_found = True
                load_tracker.clear()
                load_tracker = [
                    current_load
                ]  # empty load tracker once load found so match can be found with code below
                start_load_tracker = current_spin
    max_len = int(len(load_tracker) / 2)
    for x in range(2, max_len):
        if load_tracker[0:x] == load_tracker[x : 2 * x]:
            repeat_num = x
            break
            # find how often the load calculation result repeats
            # use this info to extrapolate which spin cycle will give same load result as wanted num spins
    len_partial_spin_captured: int = (
        start_load_tracker + len(load_tracker)
    ) % repeat_num  # find how far into spin cycle the tracker finishes
    spin_cycle_equivalent_to_desired_spins = num_spin % repeat_num
    print(
        load_tracker,
        len_partial_spin_captured,
        spin_cycle_equivalent_to_desired_spins,
        repeat_num,
    )
    return load_tracker[
        -(
            len_partial_spin_captured
            + repeat_num
            - spin_cycle_equivalent_to_desired_spins
        )
    ]  # -1 from index as counting backward from end of list


day_14_map: dict = create_array("day-14/input.txt")
round_rocks, rocks_by_x, rocks_by_y, max_x, max_y = find_rocks_and_round_rocks(
    day_14_map
)
new_round_rocks = move_rocks_north(round_rocks, rocks_by_x)
# print(calculate_load(new_round_rocks, max_x))
print(spin_cycle(round_rocks, rocks_by_x, rocks_by_y, max_x, max_y, 1000000000))
