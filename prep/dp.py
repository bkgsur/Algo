import itertools
import enchant
import helper


# 1
# https://www.geeksforgeeks.org/find-maximum-possible-stolen-value-houses/
# There are N houses built in a line, each of which contains some value in it.
# A thief is going to steal the maximal value of these houses, but he can’t steal in two adjacent houses because the owner of the stolen houses
# will tell his two neighbors left and right sides. The task is to find what is the maximum stolen value.
def thievery(houses):
    without_current = 0
    with_current = 0
    for i in range(len(houses) - 1, -1, -1):
        # with current
        with_current = houses[i]
        # add value from the house after next
        if i + 2 < len(houses):
            with_current += houses[i + 2]
        # without current
        # get value from next house
        if i + 1 < len(houses):
            without_current = houses[i + 1]
        # use existing array to store max value
        houses[i] = max(with_current, without_current)
    return houses[0]


# print('max theft value: ',thievery([2, 7, 9, 3, 1]))

# 2
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

# 3
def maxsubarraysum(A):
    min_sum = max_sum = 0
    for running_sum in itertools.accumulate(A):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)

    return max_sum


# print(maxsubarraysum([-904, -40, -523, -12, -335, -385, -124, -481, -31]))

# 4
def footballscore(score):
    points = [2, 3, 7]
    # make matrix to hold combos
    dp = [[0 for _ in range(score + 1)] for j in range(len(points))]
    helper.pm(dp)
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

    return dp[-1][-1]


# print(footballscore(12))

# 5
def climbstairs(n):
    if n == 1 or n == 2:
        return n
    minus_2 = 1
    minus_1 = 2
    for i in range(3, n + 1):
        m = minus_1 + minus_2
        minus_2 = minus_1
        minus_1 = m
    return m


# print(climbstairs(4))


# 6
def levensteindistance(word1, word2):
    print(word1)
    print(word2)

    dp = [[0 for _ in range(0, len(word2) + 1)] for _ in range(0, len(word1) + 1)]
    for i in range(len(word1) + 1):
        for j in range(len(word2) + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                currentletter = word1[i - 1]
                if currentletter == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], min(dp[i][j - 1], dp[i - 1][j]))

    # pm(dp)
    return dp[-1][-1]


# print(levensteindistance('Saturday', 'Sundays'))
# 7
def waytoend(n, m):
    dp = [[0 for _ in range(m)] for _ in range(n)]

    def helper(x, y):
        if x == 0 and y == 0:
            return 1
        if dp[x][y] == 0:
            ways_from_top = 0 if x == 0 else helper(x - 1, y)
            ways_from_left = 0 if y == 0 else helper(x, y - 1)
            dp[x][y] = ways_from_top + ways_from_left
        helper.pm(dp)
        return dp[x][y]

    return helper(n - 1, m - 1)


# print(waytoend(5, 5))
# 8
def choose_x(n, k):
    def helper(x, y):
        if y in (0, x):
            return 1
        if dp[x][y] == 0:
            without_x = helper(x - 1, y)
            with_x = helper(x - 1, y - 1)
            dp[x][y] = without_x + with_x
        return dp[x][y]

    dp = [[0 for _ in range(0, k + 1)] for _ in range(0, n + 1)]
    return helper(n, k)


# print(choose_x(5, 2))

# 9
def pattern_in_matix(A, S):
    def helper(x, y, offset):
        if len(S) == offset:
            return True
        if (0 <= x < len(A)) and (0 <= y < len(A[x])) and (
                A[x][y] == S[offset] and ((x, y, offset) not in visited)) and any(
            helper(x + a, y + b, offset + 1) for (a, b) in ((0, 1), (0, -1), (1, 0), (-1, 0))):
            return True
        visited.add((x, y, offset))

    visited = set()
    return any(helper(i, j, 0) for i in range(len(A)) for j in range(len(A[i])))


# print(pattern_in_matix([[1, 2, 3], [3, 4, 5], [5, 6, 7]], [1, 3, 4, 6]))

# 10
def knapsack(itemsvalue, itemsWeight, capacity):
    def helper(k, available_capacity):
        if available_capacity <= 0 or k < 0:
            return 0
        # print(k, available_capacity)
        if dp[k][available_capacity] == -1:
            with_item = 0 if available_capacity < itemsWeight[k] else itemsvalue[k] + helper(k, available_capacity -
                                                                                             itemsWeight[k])
            without_item = helper(k - 1, available_capacity)
            dp[k][available_capacity] = max(with_item, without_item)
        return dp[k][available_capacity]

    dp = [[-1 for _ in range(capacity + 1)] for _ in range(len(itemsvalue))]
    # pm(dp)
    return helper(len(itemsvalue) - 1, capacity)


def knapsack1(itemsvalue, itemsWeight, capacity):
    items = len(itemsvalue)
    # print(d)
    finalmax = 0

    for i in range(items):
        currentMax = 0
        k = capacity
        if itemsWeight[i] <= k:
            currentMax += itemsvalue[i]
            k -= itemsWeight[i]
            for j in range(items):
                if j != i and itemsWeight[j] <= k:
                    currentMax += itemsvalue[j]
                    k -= itemsWeight[j]

        finalmax = max(finalmax, currentMax)
    return finalmax


# print(knapsack([60, 50, 70, 30], [5, 3, 4, 2], 5))
# print(knapsack1([60, 50, 70, 30], [5, 3, 4, 2], 5))

# 11
def breakupwords(s):
    print('input: ', s, len(s))
    d = enchant.Dict("en_US")
    valid_word_length = [-1 for _ in range(len(s))]

    for i in range(len(s)):
        if d.check(s[:i + 1]):
            valid_word_length[i] = i + 1
        if valid_word_length[i] == -1:
            for j in range(i):
                if valid_word_length[j] != -1 and d.check(s[j + 1:i + 1]):
                    valid_word_length[i] = i - j
                    break
    print(valid_word_length)
    decompose = []
    if valid_word_length[-1] != -1:
        idx = len(s) - 1
        while idx >= 0:
            print(idx + 1, idx + 1 - valid_word_length[idx], s[idx + 1 - valid_word_length[idx]:idx + 1])
            decompose.append(s[idx + 1 - valid_word_length[idx]:idx + 1])
            idx -= valid_word_length[idx]

        decompose = decompose[::-1]

    print(decompose)


# breakupwords('bedbathandbeyond.com')

# 12

# Time Complexity: O(2^n)
# Space Complexity: O(n) , Because of the recursion stack.
def longest_subsequence(A: [int]) -> [int]:
    n: int = len(A)
    max_length = [1] * n
    for i in range(1, n):
        max_length[i] = max(1 + max([max_length[j] for j in range(0, i) if A[j] <= A[i]], default=0), max_length[i])

    return max(max_length)


# A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
# print(longest_subsequence(A))




