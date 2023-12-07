def parse_input_7(input_file_name: str) -> list:
    """
    Separate each hand into list of cards and its bid. Convert all cards to numbers so
    they are easier to compare.
    """
    input_as_list: list[str] = open(input_file_name, "r").readlines()
    output = [line.split() for line in input_as_list]
    for line in output:
        line[0] = [*(line[0])]
        x = 0
        while x < len(line[0]):
            if line[0][x] == "A":
                line[0][x] = 14
            elif line[0][x] == "K":
                line[0][x] = 13
            elif line[0][x] == "Q":
                line[0][x] = 12
            elif line[0][x] == "J":
                line[0][x] = 11
            elif line[0][x] == "T":
                line[0][x] = 10
            else:
                line[0][x] = int(line[0][x])
            x += 1
        line[0], line[1] = line[1], line[0]
    return output


input7 = parse_input_7("day-7/input.txt")


def day_7_pt_1(array: list) -> int:
    a = 0
    while a < len(array):
        y = 0
        hand: dict = {}
        while y < len(array[a][1]):
            """
            Count number of matching cards
            """
            current_card = array[a][1][y]
            if not current_card in hand:
                hand[current_card] = 1
            else:
                hand[current_card] += 1
            y += 1
        if len(hand) == 1:
            """
            Give each hand type a score to compare against each other
            """
            score = 7
        elif len(hand) == 2:
            if 4 in (hand.values()):
                score = 6
            if 3 in (hand.values()):
                score = 5
        elif len(hand) == 3:
            if 3 in hand.values():
                score = 4
            if 2 in hand.values():
                score = 3
        elif len(hand) == 4:
            score = 2
        else:
            score = 1
        array[a].append(score)
        # add to input array the score for that hand
        a += 1
    sorted_hands: list = sorted(array, key=lambda x: x[1])
    # sort the list by strongest cards
    sorted_hands2 = sorted(sorted_hands, key=lambda x: x[2])
    # then sort by strongest hands

    rank = 1
    total = 0
    for hand in sorted_hands2:
        total = total + (
            rank * int(hand[0])
        )  # multiply rank by bid, and find sum of all
        rank += 1
    return total


print(day_7_pt_1(input7))
