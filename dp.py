import itertools


def pm(a):
    s = [[str(e) for e in row] for row in a]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    print('=============================')


def thievery(houses):
    without_current = 0

    for i in range(len(houses) - 1, -1, -1):

        with_current = houses[i]
        if i + 2 < len(houses):
            with_current += houses[i + 2]
        if i + 1 < len(houses):
            without_current = houses[i + 1]
        houses[i] = max(with_current, without_current)
    return houses[0]


h = [2, 7, 9, 3, 1]


# print(thievery(h))


def fib(n):
    f_minus_2 = 0
    f_minus_1 = 1
    if n <= 1:
        return n
    for _ in range(2, n):
        f = f_minus_2 + f_minus_1
        f_minus_2 = f_minus_1
        f_minus_1 = f
    return f


# print(fib(10))


def maxsubarray(A):
    min_sum = max_sum = 0
    for running_sum in itertools.accumulate(A):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)

    return max_sum


# print(maxsubarray([-904, -40, -523, -12, -335, -385, -124, -481, -31]))


def footballscore(score):
    points = [2, 3, 7]
    # make matrix to hold combos
    dp = [[0 for _ in range(score + 1)] for j in range(len(points))]
    for i in range(len(dp)):
        dp[i][0] = 1
        current_point = points[i]
        # print(current_point)
        for j in range(1, score + 1):
            if j < current_point:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i][j - current_point]
            if i > 0:
                dp[i][j] += dp[i - 1][j]
    pm(dp)
    return dp[-1][-1]


# print(footballscore(12))


def climbstairs(n, k):
    # choices i to k steps per attempts
    dp = [[0 for j in range(0, n + 1)] for i in range(1, k + 1)]
    for i in range(0, k):
        dp[i][0] = 1
        current_step = i + 1
        for j in range(1, n + 1):
            if j >= current_step:
                dp[i][j] = dp[i][j - current_step]
            if i > 0:
                dp[i][j] += dp[i - 1][j]
    pm(dp)


print(climbstairs(3, 2))
