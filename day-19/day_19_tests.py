from day_19 import parse_into_dicts, go_through_ratings

test = parse_into_dicts("day-19/test_input.txt")

assert (go_through_ratings(test[0], test[1])) == 19114
