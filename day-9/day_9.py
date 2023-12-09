from parse_input import parse_input_func_2

day_9_input = parse_input_func_2("day-9/input.txt")


def day_9_part_1(input_array: list) -> int:
    """
    For each list of numbers, predict what the next number in the sequence will be.
    Find the sum of all of the numbers found.
    """
    nums_list: list = (
        []
    )  # this will be where predicted numbers will be stored, to sum later
    for y in input_array:
        difference: dict = {
            0: y
        }  # this dict will be used to find difference between each number in list, to calculate pattern
        not_all_zero = True
        level = 1  # start at level 1, as level 0 initialised above already
        while not_all_zero:
            idx = 0  # keep track of the number of levels needed for each list
            difference[level] = []
            while (
                idx < len(difference[level - 1]) - 1
            ):  # find difference between each number in list
                difference[level].append(
                    difference[level - 1][idx + 1] - difference[level - 1][idx]
                )

                idx += 1
            if sum(difference[level]) == 0:
                not_all_zero = False
                # once all numbers in current level are 0, pattern has been found, so can start predicting next number in list
            else:
                level += 1
        while level > 1:
            level -= 1
            total = (difference[level][-1]) + (
                difference[level - 1][-1]
            )  # sum the last number on current line with last number on line above
            difference[level - 1].append(total)
        nums_list.append(
            difference[level - 1][-1]
        )  # this is a list of all the extrapolated values
    return sum(nums_list)


# print(day_9_part_1(day_9_input))


def day_9_part_2(input_array: list) -> int:
    """
    As above, but reverse each list so that the number being found is actually the first one.
    """
    nums_list: list = []
    for y in input_array:
        reversed_y = list(reversed(y))
        difference: dict = {0: reversed_y}
        not_all_zero = True
        level = 1
        while not_all_zero:
            idx = 0  # keep track of the number of levels needed for each list
            difference[level] = []
            while (
                idx < len(difference[level - 1]) - 1
            ):  # find difference between each number in list
                difference[level].append(
                    difference[level - 1][idx + 1] - difference[level - 1][idx]
                )

                idx += 1
            if sum(difference[level]) == 0:
                not_all_zero = False
            else:
                level += 1
        while level > 1:
            level -= 1
            total = (difference[level][-1]) + (
                difference[level - 1][-1]
            )  # sum the last number on current line with last number on line above
            difference[level - 1].append(total)
        nums_list.append(
            difference[level - 1][-1]
        )  # this is a list of all the extrapolated values
    return sum(nums_list)


# print(day_9_part_2(day_9_input))
