input: list[str] = open("day-3/input.txt", "r").readlines()
input1 = [line.strip("\n") for line in input]


def populate_table(array: list[str]):
    input_table: list = [["" for _ in range(len(array[0]))] for _ in range(len(array))]
    for x in range(len(array)):
        for y in range(len(array[0])):
            input_table[x][y] = str(array[x][y])
    return input_table


input_table = populate_table(input1)


def check_diag(y, last_y, x, array) -> bool:
    num = False
    for dx in range(max(x - 1, 0), min(x + 2, len(array)), 1):
        for dy in range(max(y - 1, 0), min(last_y + 2, len(array[0])), 1):
            if (not array[dx][dy].isalnum()) and (array[dx][dy] != "."):
                num = True
            else:
                continue
    return num


def day3(array: list) -> int:
    x = 0
    total_sum = 0
    while x < len(array):
        y = 0
        while y < len(array[0]):
            if array[x][y].isdigit():
                first_y = y
                last_y = y
                z = last_y + 1
                total_num = str(array[x][first_y])
                while (
                    z < (len(array[0])) and array[x][z].isdigit()
                ):  # scan along x axis
                    last_y = z
                    total_num += str(array[x][z])
                    z += 1
                num: bool = check_diag(first_y, last_y, x, array)
                if num:
                    total_sum += int(total_num)
                y = last_y
            y += 1
        x += 1
    return total_sum


print(day3(input_table))
