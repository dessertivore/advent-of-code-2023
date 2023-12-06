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
    output = [re.findall(r"(\d+)", line) for line in input_as_list]
    return output


def parse_input_1_no_per_line(input_file_name: str) -> list:
    input_as_list: list[str] = open(input_file_name, "r").readlines()
    output = [re.sub(r"[^0-9]", "", line) for line in input_as_list]
    return output
