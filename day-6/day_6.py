from parse_input import parse_input_func_2, parse_input_1_no_per_line
import math

input1 = parse_input_func_2("day-6/input.txt")


def day_6_pt_1(array: list) -> int:
    """
    For each race, find how many ways you could beat the record score.
    Multiply all of those together.
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


def day_6_pt_2(array: list) -> int:
    """
    For one big race, find how many ways you could beat the record score.
    Input should be in form [[race time][record distance]]
    Use of quadratic eq to solve for x, to find point at which dist travelled > record.
    Use previous part's loop to find lowest possible charging time to beat record.
    Output difference between those 2 numbers = number of ways to beat record.
    """
    race_time: int = int(array[0])
    record: int = int(array[1])
    print(race_time, record)
    turning_point = (
        math.ceil(((0 - race_time) + math.sqrt((race_time**2) - (4 * record))) / (-2))
        - 1
    )
    for time_charging in range(int(race_time)):
        travelled = (int(race_time) - time_charging) * time_charging
        if travelled > int(record):
            print(time_charging)
            break
    output = race_time - turning_point
    return output - time_charging


print(day_6_pt_2(parse_input_1_no_per_line("day-6/input.txt")))
