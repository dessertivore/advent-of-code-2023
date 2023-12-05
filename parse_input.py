def parse_input_func(input_file_name: str) -> list:
    input_as_list: list[str] = open(input_file_name, "r").readlines()
    ouput = [line.strip("\n") for line in input_as_list]
    return ouput
