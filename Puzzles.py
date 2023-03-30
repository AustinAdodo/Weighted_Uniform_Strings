def pickingNumbers(a):
    b = list(dict.fromkeys(sorted(a)))
    maxArray = [a.count(b[i]) + a.count(b[i + 1]) for i in range(len(b) - 1) if abs(b[i] - b[i + 1]) <= 1] + [
        a.count(b[j]) for j in range(len(b))]
    return max(maxArray) if len(maxArray) > 0 else len(a)


def balancedStringSplit1(self, s: str) -> int:
    result = 0
    arr = s.split("RL")
    check2 = len(s.split("LR")) - 1
    for item in arr:
        if len(item.split("r")) - 1 == len(item.split("L")) - 1:
            result += 1
    return result if result > 0 else check2


# "RLRRLLRLRL"
def balancedStringSplit(s: str) -> int:
    result = 0
    arr = [i for i in s]  # arr[:0] = s
    # rangeS = iter(arr)
    rangeS = enumerate(arr)
    for i, item in rangeS:
        # if i + 1 <= len(s) - 1 and (s[i] + s[i + 1] == "LR" or s[i] + s[i + 1] == "RL"):
        b = i + 1
        a = arr[i + 1] if i + 1 <= len(arr) - 1 else ""
        if item + a == "LR" or item + a == "RL":
            result += 1
            next(rangeS, None)
            continue
    return result
