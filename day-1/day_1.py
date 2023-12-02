# convert input file into an array of strings
day1_input = open("day-1/input_file.txt", "r").readlines()


def replace_text_number(array: str) -> str:
    """
    convert all written numbers into digits.
    keep first and last letters in place in case they are needed for another written number.
    some numbers do not need first and last letters preserved as they are not the first or
    last letters of any other numbers (e.g. four - no other number ends in f, so no need
    to preserve this)
    """

    array = array.replace("one", "o1e")
    array = array.replace("two", "t2o")
    array = array.replace("three", "t3e")
    array = array.replace("four", "f4r")
    array = array.replace("five", "f5e")
    array = array.replace("six", "s6x")
    array = array.replace("seven", "s7n")
    array = array.replace("eight", "e8t")
    array = array.replace("nine", "n9e")
    return array


# find first and last digits
def day1(array: str) -> int:
    array = replace_text_number(array)
    # store response as a string for now so that the numbers can be 'added' together
    response = ""
    for x in array:
        if x.isdigit():
            response = response + x
            break
        else:
            continue
    # to find last digit, reverse the string before iterating through it
    for y in reversed(array):
        if y.isdigit():
            response = response + y
            break
        else:
            continue
    # convert response into an integer before returning it
    return int(response)


# find sum of all inputs
def day1sum(array: list) -> int:
    totalsum = 0
    for x in array:
        totalsum += day1(x)
    return totalsum


print(day1sum(day1_input))
