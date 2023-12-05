# to run code and access parent directory for parse function: PYTHONPATH=. poetry run python day-4/day_4.py

from parse_input import parse_input_func

input1 = parse_input_func("day-4/input4.txt")
input = [
    line.strip("Card ")
    .replace(": ", " ")
    .replace(" | ", " ")
    .replace("  ", " ")
    .split(" ")
    for line in input1
]


def day4(array: list, winning: int) -> int:
    """
    Input list of games. 'Winning' should be the number of cards in a winning set so that
    the function knows what indices to be searching through.
    """
    total = 0
    for z in array:
        counter = 0
        winning_list = z[1 : (winning + 1)]
        my_list = z[(winning + 1) :]
        for x in winning_list:
            for y in my_list:
                if x == y:
                    counter += 1
        total += int(2 ** (counter - 1))
    return total


print(day4(input, 10))


def day4_p2(array: list, winning: int) -> int:
    """
    Based on previous code, but with new functionality as needed for part 2.
    """
    scratchcards_owned: dict = {}
    for index in range(len(array)):
        scratchcards_owned[index] = 1
    for z in array:
        idx = array.index(z)
        counter = 0
        winning_list = z[1 : (winning + 1)]
        my_list = z[(winning + 1) :]
        for x in winning_list:
            for y in my_list:
                if x == y:
                    counter += 1  # count how many matches
        for i in range(idx + 1, min(idx + counter + 1, len(array))):
            scratchcards_owned[i] += scratchcards_owned[idx]
    return sum(scratchcards_owned.values())


print(day4_p2(input, 10))
