from day_13 import parse_input, find_rotation, sum_pivots

test = parse_input("day-13/test_input.txt")
pivots = find_rotation(test)


def test_symmetry_finding() -> None:
    assert (find_rotation(test)) == [[3.5], [4.5]]


def test_summing_pivots() -> None:
    assert sum_pivots([[3.5], [4.5]]) == 405


def test_summing_pivots_2() -> None:
    assert sum_pivots(pivots) == 405
