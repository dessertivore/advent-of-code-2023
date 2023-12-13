from day_12 import find_number_possibilities, parse_input, find_all

full_maps, groups = parse_input("day-12/test_input.txt")
print((full_maps, groups))


def test_with_solved_case() -> None:
    assert (
        find_number_possibilities(["#", ".", "#", ".", "#", "#", "#"], [1, 1, 3]) == 1
    )


def test_2() -> None:
    assert (
        find_number_possibilities(["?", "?", "?", ".", "#", "#", "#"], [1, 1, 3]) == 1
    )
