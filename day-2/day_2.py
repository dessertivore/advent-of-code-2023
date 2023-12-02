import re

# convert txt to dict of games
input = open("day-2/input_file.txt", "r").readlines()


def parse_input(input: list) -> dict:
    dict = {}
    # Remove 'Game' and line breaks, then create list of all outputs in dict
    input_stripped = [(entry.strip("Game ")).strip("\n") for entry in input]
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


def d2_part2(input: dict, key: int) -> int:
    min = {"red": 0, "green": 0, "blue": 0}
    game_list = input[key]
    for entry in game_list:
        num, colour = entry.split(" ")
        if int(num) > min[colour]:
            min[colour] = int(num)
        else:
            continue
    power = min["red"] * min["green"] * min["blue"]
    return power


def total_d2_part2(input: dict) -> int:
    x = 1
    total = 0
    while x <= len(input):
        total += d2_part2(input, x)
        x += 1
    return total


print(total_d2_part2(day2_dict))
