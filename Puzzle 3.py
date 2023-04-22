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
