from collections import defaultdict


def find_hash(input_text: str) -> int:
    """
    Manually hash characters in method specified in the problem.
    """
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


def find_hash_string(input_string: str) -> int:
    """
    As above but using strings from function rather than an input file.
    """
    total = 0
    current_value = 0
    for char in input_string:
        current_value += ord(char)
        current_value = current_value * 17
        current_value = current_value % 256
    total += current_value
    return total


find_hash("day-15/input.txt")


def sort_lenses(input_text: str) -> int:
    """
    The instructions were convoluted but essentially, add to a dict, or remove,
    based on whether - or = in list entry
    """
    boxes: dict = defaultdict(list)
    with open(input_text, "r") as file:
        strings: list[str] = file.read().split(",")
    for individual_string in strings:
        operator = None
        label = ""
        for char in individual_string:
            if char.isalpha():
                label += char  # initiate label
            if char == "-" or char == "=":
                operator = char  # assign operator
            if char.isdigit():
                focal_length = int(char)
        box_num = find_hash_string(label)
        if operator == "-":
            to_remove = None
            for lens in boxes[box_num]:  # remove lens from box if present
                current = lens.split(" ")[0]
                if current == label:
                    to_remove = lens
            if to_remove:
                boxes[box_num].remove(to_remove)
                if len(boxes[box_num]) == 0:
                    boxes.pop(box_num, 0)
        elif operator == "=":
            label_already_present: bool = False
            for idx, lens in enumerate(boxes[box_num]):  # check if label already in box
                if lens.split(" ")[0] == label:  # if text element (first half) == label
                    to_remove = lens
                    to_remove_idx = idx
                    label_already_present = True
            if label_already_present == True:
                boxes[box_num][to_remove_idx] = str(to_remove)[:-1] + str(focal_length)

            if label_already_present == False:
                boxes[box_num].append(label + " " + str(focal_length))
    total_focus_power = 0
    for box_num in boxes.keys():
        focusing_power: int = 0
        if boxes[box_num] != []:
            for idx, label in enumerate(boxes[box_num]):
                focusing_power += (box_num + 1) * (idx + 1) * int(label[-1])
        total_focus_power += focusing_power
    print(total_focus_power)
    return total_focus_power


sort_lenses("day-15/input.txt")
