import math


def open_input_8(input_file_name: str) -> tuple:
    input_as_list = open(input_file_name, "r").readlines()
    nodes: dict = {}  # dict will store node: left, right
    A_list: dict = {}
    for line in input_as_list:
        if "(" not in line and line != "\n":
            directions: str = line.strip("\n")
        elif len(line) > 1 and line[2] == "A":
            A_list[line[0:3]] = [
                line[0:3],
                "A",
            ]  # dict with current node, ending letter
            nodes[line[0:3]] = (line[7:10], line[12:15])
        elif len(line) > 1:
            nodes[line[0:3]] = (line[7:10], line[12:15])

    return directions, nodes, A_list


day_8_input_directions, day_8_input_nodes, day_8_A_List = open_input_8(
    "day-8/input.txt"
)


def day_8_part_1(directions: str, nodes: dict) -> int:
    """
    Start with location AAA. Using directions string, make your way to location ZZZ.
    Left direction is stored at entry 0, right direction is stored at 1.
    """
    current = "AAA"
    counter: int = 0
    while current != "ZZZ":
        for x in directions:
            counter += 1
            if x == "R":
                current = nodes[current][1]
            if x == "L":
                current = nodes[current][0]
    return counter


# print(day_8_part_1(day_8_input_directions, day_8_input_nodes))


def day_8_part_2(directions: str, nodes: dict, A_list: dict) -> int:
    """
    Start with locations xxA. Using directions string, make your way to location xxZ.
    Left direction is stored at entry 0, right direction is stored at 1.
    """
    counter_list: list = []
    for x in A_list:
        """
        Find how many steps each separate starting point ends up with.
        """
        counter = 0
        current = x
        while current[2] != "Z":
            for x in directions:
                counter += 1
                if x == "R":
                    current = nodes[current][1]
                if x == "L":
                    current = nodes[current][0]
        counter_list.append(counter)
    return math.lcm(*counter_list)  # find lowest common multiple of all counters


print(day_8_part_2(day_8_input_directions, day_8_input_nodes, day_8_A_List))
