def open_input_8(input_file_name: str) -> tuple:
    input_as_list = open(input_file_name, "r").readlines()
    nodes = {}  # dict will store node: left, right
    for line in input_as_list:
        if "(" not in line and line != "\n":
            directions: str = line.strip("\n")
        else:
            nodes[line[0:3]] = (line[7:10], line[12:15])
    return directions, nodes


day_8_input_directions, day_8_input_nodes = open_input_8("day-8/input.txt")


def day_8_part_1(directions: str, nodes: dict) -> int:
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


print(day_8_part_1(day_8_input_directions, day_8_input_nodes))
