input: list[str] = open("day-3/input.txt", "r").readlines()
input1 = [line.strip("\n") for line in input]


def populate_table(array: list[str]):
    """
    Create a table where each row x corresponds to 1 line in the input file.
    """
    input_table: list = [["" for _ in range(len(array[0]))] for _ in range(len(array))]
    for x in range(len(array)):
        for y in range(len(array[0])):
            input_table[x][y] = str(array[x][y])
    return input_table


input_table = populate_table(input1)


def check_diag(y, last_y, x, array) -> bool:
    """
    Check all adjacent cells around number for symbols.
    """
    num = False
    for dx in range(max(x - 1, 0), min(x + 2, len(array)), 1):
        for dy in range(max(y - 1, 0), min(last_y + 2, len(array[0])), 1):
            if (not array[dx][dy].isalnum()) and (array[dx][dy] != "."):
                num = True
            else:
                continue
    return num


def day3(array: list) -> int:
    """
    Find all numbers in the input file. Check if they have a symbol in adjacent cell.
    If they do, add them to totalsum.
    """
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


def check_ratio(x: int, y: int, array: list) -> int:
    """
    Check if asterisk is a gear and calculate ratio
    """
    num_list = []
    ratio = 0
    dx = max(x - 1, 0)
    while dx < min(x + 2, len(array)):
        dy = max(y - 1, 0)
        while dy < min(y + 2, len(array[0])):
            if array[dx][dy].isdigit():
                num = ""
                first_y = dy
                last_y = dy
                while first_y >= 0 and array[dx][first_y - 1].isdigit():
                    first_y -= 1
                while last_y < len(array[0]) - 1 and array[dx][last_y + 1].isdigit():
                    last_y += 1
                for z in range(first_y, last_y + 1):
                    num += array[dx][z]
                print(num)
                num_list.append(num)
                dy = last_y
            dy += 1
        dx += 1
    if len(num_list) == 2:
        print(num_list)
        int1 = num_list[0]
        int2 = num_list[1]
        ratio = int(int1) * int(int2)
    return ratio


def day3_asterisk(array: list) -> int:
    """
    Find asterisks and sum ratios.
    """
    x = 0
    total_ratio = 0
    while x < len(array):
        y = 0
        while y < len(array[0]):
            if array[x][y] == "*":
                ratio: int = check_ratio(x, y, array)
                total_ratio += ratio
            y += 1
        x += 1
    return total_ratio


print(day3_asterisk(input_table))
