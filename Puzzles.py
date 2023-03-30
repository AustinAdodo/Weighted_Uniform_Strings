def pickingNumbers(a):
    b = list(dict.fromkeys(sorted(a)))
    maxArray = [a.count(b[i]) + a.count(b[i + 1]) for i in range(len(b) - 1) if abs(b[i] - b[i + 1]) <= 1] + [
        a.count(b[j]) for j in range(len(b))]
    return max(maxArray) if len(maxArray) > 0 else len(a)


# Better Solution
def balancedStringSplit(self, s: str) -> int:
    res = cnt = 0
    for c in s:
        cnt += 1 if c == 'L' else -1
        if cnt == 0:
            res += 1
    return res


# "RLRRLLRLRL"
def balancedStringSplit(s: str) -> int:
    result = 0
    arr = [i for i in s]  # arr[:0] = s
    # rangeS = iter(arr)
    rangeS = enumerate(arr)
    for i, item in rangeS:
        b = i + 1
        a = arr[i + 1] if i + 1 <= len(arr) - 1 else ""
        if item + a == "LR" or item + a == "RL":
            result += 1
            next(rangeS, None)
            continue
    return result


# using memoization solve the rolling dice problem.
def dieSimulator(self, n, A):
    dp = [[0] * 7 for _ in range(n + 1)]
    dp[0][-1] = 1
    for i in range(1, n + 1):
        for j in range(6):
            dp[i][j] = dp[i - 1][-1]
            if i > A[j]: dp[i][j] -= dp[i - A[j] - 1][-1] - dp[i - A[j] - 1][j]
        dp[i][-1] = sum(dp[i]) % (10 ** 9 + 7)
    return dp[-1][-1]
