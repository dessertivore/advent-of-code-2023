from parse_input import create_array
from collections import defaultdict
import math


def find_rocks_and_round_rocks(input_map: dict) -> tuple:
    max_x = 0
    max_y = 0
    round_rocks: set = set()
    rocks: set = set()

    for coord, item in input_map.items():
        max_x = max(max_x, coord[0])
        max_y = max(max_y, coord[1])
        if item == "O":
            round_rocks.add(coord)
        if item == "#":
            rocks.add(coord)
    return round_rocks, rocks, max_x, max_y


def move_rocks_north(round_rocks: set, rocks: set) -> set:
    """
    Move all round rocks ("O") as far up as possible.
    """
    new_round_rocks: set = set()
    for round_rock in round_rocks:
        x = round_rock[0]
        y = round_rock[1]
        closest_rock_x = 0
        no_rocks_in_way = True
        for (
            rock
        ) in (
            rocks
        ):  # go through all the cube rocks and find the one closest on x axis, and on same y axis
            if rock[1] == y and rock[0] < x:
                closest_rock_x = max(closest_rock_x, rock[0])
                no_rocks_in_way = False
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
    load_per_row: dict = defaultdict(lambda: 0)
    for round_rock in round_rocks:
        load_per_row[round_rock[0]] += 1
    total_load = 0
    print(load_per_row, round_rocks)
    for coord, rock_num in load_per_row.items():
        multiplier = max_x + 1 - coord
        total_load += rock_num * multiplier
    return total_load


# day_14_map: dict = create_array("day-14/input.txt")
# round_rocks, rocks, max_x, max_y = find_rocks_and_round_rocks(day_14_map)
# new_round_rocks = move_rocks(round_rocks, rocks)
# print(calculate_load(new_round_rocks, max_x))


def move_rocks_down(round_rocks: set, rocks: set, max_x: int) -> set:
    """
    Move all round rocks ("O") as far down as possible.
    """
    new_round_rocks: set = set()
    for round_rock in round_rocks:
        x = round_rock[0]
        y = round_rock[1]
        closest_rock_x = max_x
        no_rocks_in_way = True
        for (
            rock
        ) in (
            rocks
        ):  # go through all the cube rocks and find the one closest on x axis, and on same y axis
            if rock[1] == y and rock[0] > x:
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


def move_rocks_right(round_rocks: set, rocks: set, max_y: int) -> set:
    """
    Move all round rocks ("O") as far down as possible.
    """
    new_round_rocks: set = set()
    for round_rock in round_rocks:
        x = round_rock[0]
        y = round_rock[1]
        closest_rock_y = max_y
        no_rocks_in_way = True
        for (
            rock
        ) in (
            rocks
        ):  # go through all the cube rocks and find the one closest on x axis, and on same y axis
            if rock[0] == x and rock[1] > y:
                closest_rock_y = min(closest_rock_y, rock[1])
                no_rocks_in_way = False
        if no_rocks_in_way:  # if no rocks in way, go to x=0, unless another rock there
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


def move_rocks_left(round_rocks: set, rocks: set) -> set:
    """
    Move all round rocks ("O") as far down as possible.
    """
    new_round_rocks: set = set()
    for round_rock in round_rocks:
        x = round_rock[0]
        y = round_rock[1]
        closest_rock_y = 0
        no_rocks_in_way = True
        for (
            rock
        ) in (
            rocks
        ):  # go through all the cube rocks and find the one closest on x axis, and on same y axis
            if rock[0] == x and rock[1] < y:
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


def spin_cycle(round_rocks: set, rocks: set, max_x: int, max_y: int, num_spin: int):
    x = 0
    current_round_rocks = round_rocks
    current_spin = 0
    while x <= num_spin:
        x += 1
        if current_spin % 4 == 0:
            current_round_rocks = move_rocks_north(current_round_rocks, rocks)
        if current_spin % 4 == 1:
            current_round_rocks = move_rocks_right(current_round_rocks, rocks, max_y)
        if current_spin % 4 == 2:
            current_round_rocks = move_rocks_down(current_round_rocks, rocks, max_x)
        if current_spin % 4 == 3:
            current_round_rocks = move_rocks_left(current_round_rocks, rocks)
        current_spin += 1
        print(calculate_load(current_round_rocks, max_y))
    return calculate_load(current_round_rocks, max_y)
