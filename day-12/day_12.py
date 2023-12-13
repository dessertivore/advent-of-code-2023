import re


def parse_input(file_name: str) -> tuple:
    """
    Get 2 lists.  The individual spring maps and the lists of broken springs.
    """
    lines: list[str] = open(file_name, "r").readlines()
    spring_map: list = []
    groups_broken: list = []
    for line in lines:
        spring_map.append([x for x in line if x == "#" or x == "." or x == "?"])
        groups_broken.append([int(y) for y in line if y.isdigit()])
    return spring_map, groups_broken


# full_maps, groups = parse_input("day-12/input.txt")
def find_number_possibilities(
    individual_spring_map: list, groups_broken: list, total=0
) -> int:
    """
    Not finished.
    """
    print(
        len(individual_spring_map),
        individual_spring_map,
        groups_broken,
        len(groups_broken),
    )
    if (
        len(groups_broken) == 1
        and len(individual_spring_map) == groups_broken[0]
        and "." not in individual_spring_map
    ):  # base case
        return 1
    else:
        idx = 0
        while idx < len(individual_spring_map) - 1:
            if individual_spring_map[idx] == ".":
                individual_spring_map.pop(idx)
            elif individual_spring_map[idx] == "#":
                new_idx: int = int(groups_broken[0]) + 1  # add 1 to remove trailing .
                total = find_number_possibilities(
                    individual_spring_map[new_idx:],
                    groups_broken[1:],
                    total=total,
                )

            idx += 1
    return total


def find_all(all_springs: list, groups_broken: list):
    idx = 0
    total = 0
    while idx < len(all_springs) - 1:
        total += find_number_possibilities(all_springs[idx], groups_broken[idx])
        idx += 1
    return total


# print(find_number_possibilities(full_maps, groups))
