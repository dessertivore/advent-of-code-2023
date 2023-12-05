import re, math


def parse_input_as_dict(input_file_name: str) -> dict:
    """
    Parse input file into a dictionary. Assumes that all dict names are on new line.
    Assumes that numbers in dict are separated by spaces.
    Assumes that dict entries are separated by double spacing.
    """
    new_dict: dict = {}
    input_as_list: list[str] = open(input_file_name, "r").readlines()
    for line in input_as_list:
        updated = line.strip("\n")
        if re.search("[a-zA-Z]", line):
            updated = updated.strip(": ")
            new_dict[updated] = []
            current = updated
        elif re.search("[0-9]", line):
            make_list = re.split(" ", updated)
            make_list = [eval(i) for i in make_list]
            new_dict[current] += make_list
        else:
            continue
    return new_dict


input = parse_input_as_dict("day-5/input.txt")


def day5_pt1(input_dict: dict) -> int:
    seed_dict: dict = {}
    for x in input_dict["seeds"]:
        seed_dict[x] = [0] * 8
    input_dict.pop("seeds")
    for x in seed_dict:
        seed_dict[x][0] = x
        map_no = 1
        for entry in input_dict.values():
            map_counter = 0
            while map_counter in range(0, len(entry)):
                if seed_dict[x][map_no - 1] in range(
                    entry[map_counter + 1],
                    (entry[map_counter + 1] + entry[map_counter + 2] + 1),
                ):
                    difference = seed_dict[x][map_no - 1] - entry[map_counter + 1]
                    seed_dict[x][map_no] = entry[map_counter] + difference
                    break
                else:
                    seed_dict[x][map_no] = seed_dict[x][map_no - 1]
                map_counter += 3
            map_no += 1
    min: int = math.inf
    for z in seed_dict.values():
        if z[-1] < min:
            min = z[-1]
    return min


print(day5_pt1(input))
