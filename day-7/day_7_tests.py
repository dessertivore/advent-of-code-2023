from day_7 import parse_input_7, day_7_pt_1, day_7_pt_2

input_7 = parse_input_7("day-7/test_input.txt")

# assert (day_7_pt_1(input_7)) == 6440
# the above will no longer work as code has been changed to reflect J's new value


def test_part_2() -> None:
    assert (day_7_pt_1(input_7)) == 5905
