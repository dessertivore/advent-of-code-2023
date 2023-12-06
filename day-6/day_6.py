from parse_input import parse_input_func_2

input1 = parse_input_func_2("day-6/input.txt")


def day_6_pt_1(array: list) -> int:
    """
    For each race, find how many ways you could beat the record score.
    Multiple all of those together.
    Input should be in form [[allowed times][record distances]]
    """
    multiplier = 1
    index = 0
    while index <= len(array[1]) - 1:
        allowed_time = array[0][index]
        record_distance = array[1][index]
        print(allowed_time, record_distance)
        counter = 0
        for time_charging in range(int(allowed_time)):
            travelled = (int(allowed_time) - time_charging) * time_charging
            if travelled > int(record_distance):
                counter += 1
        multiplier = multiplier * counter
        index += 1
    return multiplier


print(day_6_pt_1(input1))
