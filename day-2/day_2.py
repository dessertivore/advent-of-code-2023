import re

# convert txt to dict of games
input = open("day-2/input_file.txt", "r").readlines()


def parse_input(input: list) -> dict:
    dict = {}
    input_stripped = [(entry.strip("Game ")).strip("\n") for entry in input]
    """Remove Game and line breaks, then create list of all outputs"""
    for line in input_stripped:
        key, outcome = line.split(": ")
        split_outcome = []
        split_outcome = re.split(", |; ", outcome)
        dict[int(key)] = split_outcome
    return dict


day2_dict = parse_input(input)


def day2(games_list: dict) -> int:
    possible = []
    game = {"red": 12, "green": 13, "blue": 14}
    for game_id, game_output in games_list.items():
        possibility: bool = True
        for entry in game_output:
            num, colour = entry.split(" ")
            if int(num) > game[colour]:
                possibility = False
            else:
                continue
        if possibility:
            possible.append(game_id)
    return sum(possible)


print(day2(day2_dict))
