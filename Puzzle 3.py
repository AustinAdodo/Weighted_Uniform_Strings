# has to be passable from top lest to bottom right
def solution(maze, n):
    result = False
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if i == 0 and maze[1][1] == 0:
                result = True
            if i > 0 and result == True and maze[i - 1][j] == 0 and maze[i][j] == 0:
                result = True
            if i > 0 and maze[len(maze) - 1][len(maze[i]) - 1] != 0:
                result = False
                continue
    return result


def calculate_height(arr, index):
    if index >= len(arr) or arr[index] is None:
        return 0
    left_height = calculate_height(arr, 2 * index + 1)
    right_height = calculate_height(arr, 2 * index + 2)
    return 1 + max(left_height, right_height)


# counting the number of cells of a 2d array that contains a one and is the neighbour of a given cell with
#  given coordinates

def matrix_coordinates():
    w, h = [int(i) for i in input().split()]
    x, y = [int(i) for i in input().split()]
    count = 0
    for i in range(h):
        row = input()
    for i in range(row):
        for j in range(row[i]):
            if i == x and row[i][j] == 1 or j == y and row[i][j] == 1:
                count += 1
    return count


def string_rotation(s: str):
    s = s_1
    new_string = s[-1] + s[:-1]
    if new_string == s:
        return False
    while new_string != s:
        new_string = new_string[-1] + new_string[::-1]
        if new_string == s_2:
            return True
    return False


def make_change(s):
    s = input()
    # 4 3
    # 1 1
    # 1000
    # 0001
    # 0100
    dollars = float(s)
    cents = round(dollars * 100)
    dollars_coins = cents // 100
    cents %= 100
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    cents %= 5
    pennies = cents
    print(f"{dollars_coins} dollar coin(s)")
    print(f"{quarters} quarter(s)")
    print(f"{dimes} dime(s)")
    print(f"{nickels} nickel(s)")
    print(f"{pennies} penny/pennies")


make_change("3.76")


def solution1(tree):
    a = list(filter(lambda x: x == -1, tree))
    if len(tree) == 0:
        return 0
    if len(a) == len(tree) - 1:
        return 1
    return calculate_height(tree, 0)


def solution2(word, cipher):
    result = ""
    if len(word) == 0:
        return 0
    word1 = [str(i) for i in word]
    cipher1 = [str(i) for i in cipher]
    for i in word:
        result += cipher1[cipher1.index(i)]
    return "".join(result)
    # return "".join([cipher1[cipher1.index(i)] for i in word1])
