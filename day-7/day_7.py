def parse_input_7(input_file_name: str) -> list:
    """
    Separate each hand into list of cards and its bid. Convert all cards to numbers so
    they are easier to compare.
    """
    input_as_list: list[str] = open(input_file_name, "r").readlines()
    output = [line.split() for line in input_as_list]
    converter_dict = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}
    for line in output:
        line[0] = [*(line[0])]
        x = 0
        while x < len(line[0]):
            if line[0][x] in converter_dict.keys():
                line[0][x] = converter_dict[(line[0][x])]  # convert letters to ints
                # for part 1, J is 11, not 1
            else:
                line[0][x] = int(line[0][x])
            x += 1
        line[0], line[1] = line[1], line[0]
    return output


input7 = parse_input_7("day-7/input.txt")


def day_7_pt_1(array: list) -> int:
    a = 0
    score_dict: dict = {
        (1, 5): 7,
        (2, 4): 6,
        (2, 3): 5,
        (3, 3): 4,
        (3, 2): 3,
        (4, 2): 2,
    }
    # score cards to compare against each other
    # [x][0] is how many different cards in hand
    # [x][1] is highest number of 1 card type
    while a < len(array):
        """
        Iterate through each hand.
        """
        y = 0
        hand: dict = {}
        while y < len(array[a][1]):
            """
            Count number of matching cards.
            """
            current_card = array[a][1][y]
            if not current_card in hand:
                hand[current_card] = 1
            else:
                hand[current_card] += 1
            y += 1
        if (len(hand), max(hand.values())) in score_dict.keys():
            """
            Give each hand type a score to compare against each other.
            """
            score = score_dict[(len(hand), max(hand.values()))]
        array[a].append(score)
        # add to input array the score for that hand
        a += 1
    print(array)
    sorted_hands: list = sorted(array, key=lambda x: x[1])
    # sort the list by strongest cards - this is needed for part 1
    sorted_hands2 = sorted(sorted_hands, key=lambda x: x[2])
    # sort by strongest hands (highest score). For part 1, use sorted_hands in place of array here
    rank = 1
    total = 0
    for hand in sorted_hands2:
        total = total + (
            rank * int(hand[0])
        )  # multiply rank by bid, and find sum of all
        rank += 1
    return total


# print(day_7_pt_1(input7))


def day_7_pt_2(array: list) -> int:
    a = 0
    score_dict: dict = {
        (1, 5): 7,
        (2, 4): 6,
        (2, 3): 5,
        (3, 3): 4,
        (3, 2): 3,
        (4, 2): 2,
    }
    # score cards to compare against each other
    # [x][0] is how many different cards in hand
    # [x][1] is highest number of 1 card type
    while a < len(array):
        """
        Iterate through each hand.
        """
        y = 0
        hand: dict = {}
        while y < len(array[a][1]):
            """
            Count number of matching cards.
            """
            current_card = array[a][1][y]
            if not current_card in hand:
                hand[current_card] = 1
            else:
                hand[current_card] += 1
            y += 1
        if 1 in hand.keys() and hand[1] != 5:
            """
            Add number of jokers to whichever card is most frequent in the pack
            (and which is not a joker).
            Unless all cards are jokers, in which case do not change.
            """
            joker_val = hand.pop(1)
            for card_frequencies in hand.keys():
                if hand[card_frequencies] == max(hand.values()):
                    hand[card_frequencies] += joker_val
        if (len(hand), max(hand.values())) in score_dict.keys():
            """
            Give each hand type a score to compare against each other.
            """
            score = score_dict[(len(hand), max(hand.values()))]
        else:
            score = 1
        array[a].append(score)
        # add to input array the score for that hand
        a += 1
    sorted_hands: list = sorted(array, key=lambda x: x[1])
    # sort the list by strongest cards - this is needed for part 1
    sorted_hands2 = sorted(sorted_hands, key=lambda x: x[2])
    # sort by strongest hands (highest score). For part 1, use sorted_hands in place of array here
    rank = 1
    total = 0
    for hand in sorted_hands2:
        total = total + (
            rank * int(hand[0])
        )  # multiply rank by bid, and find sum of all
        rank += 1
    return total


print(day_7_pt_2(input7))
