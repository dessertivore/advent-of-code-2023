from day_3 import day3, populate_table, check_diag

input: list[str] = open("day-3/test_input.txt", "r").readlines()
input1 = [line.strip("\n") for line in input]

input2 = populate_table(input1)


assert (check_diag(0, 2, 0, input2)) == True

assert day3(input2) == 4361
