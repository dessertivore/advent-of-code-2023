from day_1 import day1, day1sum, replace_text_number

# check that function works with strings that don't contain written numbers
assert day1("1abc2") == 12
assert day1("pqr3stu8vwx") == 38
assert day1("a1b2c3d4e5f") == 15
assert day1("treb7uchet") == 77

test = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".splitlines()

assert day1sum(test) == 142

# check that text to number converter works
assert day1("two1nine") == 29
assert day1("eightwothree") == 83
assert day1("abcone2threexyz") == 13
assert day1("xtwone3four") == 24
assert day1("4nineeightseven2") == 42
assert day1("zoneight234") == 14
assert day1("7pqrstsixteen") == 76
