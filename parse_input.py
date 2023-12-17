import re


def parse_input_func(input_file_name: str) -> list:
    input_as_list: list[str] = open(input_file_name, "r").readlines()
    ouput = [line.strip("\n") for line in input_as_list]
    return ouput


def parse_input_func_2(input_file_name: str) -> list:
    """
    Regex finds all continuous numbers and puts them in list.
    """
    input_as_list: list[str] = open(input_file_name, "r").readlines()
    output = [[int(j) for j in re.findall(r"(-?\d+)", line)] for line in input_as_list]
    return output


def parse_input_1_no_per_line(input_file_name: str) -> list:
    input_as_list: list[str] = open(input_file_name, "r").readlines()
    output = [re.sub(r"[^0-9]", "", line) for line in input_as_list]
    return output


def create_array(file_name: str) -> dict:
    """
    Create a grid, assign coordinates x,y to each character, save as a dict.
    """
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
