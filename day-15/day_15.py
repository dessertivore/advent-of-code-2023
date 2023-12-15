from collections import defaultdict


def find_hash(input_text: str) -> int:
    total = 0
    with open(input_text, "r") as file:
        strings: list[str] = file.read().split(",")
    for individual_string in strings:
        current_value = 0
        for char in individual_string:
            current_value += ord(char)
            current_value = current_value * 17
            current_value = current_value % 256
        total += current_value
    print(total)
    return total


# find_hash("day-15/input.txt")


def sort_lenses(input_text: str) -> dict:
    boxes: dict = defaultdict(list)
    with open(input_text, "r") as file:
        strings: list[str] = file.read().split(",")
    for individual_string in strings:
        current_value = 0
        operator = None
        label = ""
        for char in individual_string:
            if char.isalpha():
                current_value += ord(char)
                current_value = current_value * 17
                current_value = current_value % 256
                label += char
            elif char == "-" or char == "=":
                operator = char
            elif char.isdigit():
                focal_length = int(char)
        if operator == "-":
            for lens in boxes[current_value]:  # remove lens from box if present
                current = ""
                for char in lens:
                    if char.isalpha():
                        current += char
                if current == label:
                    boxes[current_value].remove(lens)
        elif operator == "=":
            replaced: bool = False
            for idx, lens in enumerate(
                boxes[current_value]
            ):  # check if label already in box
                if lens[0:2] == label:
                    replaced = True
                    break
            if replaced == True:
                boxes[current_value].remove(lens)
                boxes[current_value].insert(idx, label + " " + str(focal_length))
            # if len(boxes[current_value]) != 0:
            if replaced == False:
                if len(boxes[current_value]) > focal_length:
                    boxes[current_value][focal_length] = label + " " + str(focal_length)
                else:
                    boxes[current_value].append(label + " " + str(focal_length))
    total_focus_power = 0
    for box_num in boxes.keys():
        focusing_power = 0
        for idx, label in enumerate(boxes[box_num]):
            focusing_power += (box_num + 1) * (idx + 1) * int(label[-1])
        total_focus_power += focusing_power
    print(total_focus_power)
    return boxes, total_focus_power


sort_lenses("day-15/input.txt")
