from day_5 import parse_input_as_dict, day5_pt1, day5_pt2


input1 = parse_input_as_dict("day-5/test_input.txt")

print(input1)
# print(day5_pt1(input1))


def test_day5() -> None:
    assert (day5_pt1(input1)) == 35


input1 = parse_input_as_dict("day-5/test_input.txt")


def test_day5_p2() -> None:
    assert (day5_pt2(input1)) == 46
