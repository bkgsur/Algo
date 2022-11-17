# 1
import math


def firstappeareance(A: [int], t: int) -> int:
    l: int = 0
    r: int = len(A) - 1
    f: int = -1
    while l <= r:
        m: int = l + (r - l) // 2
        c: int = A[m]
        if c == t:
            f = m
            r = m - 1
        elif c < t:
            l = m + 1
        else:
            r = m - 1
    return f


# A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
# print(firstappeareance(A, 285))
# print(firstappeareance(A, 108))
# print(firstappeareance(A, 401))
# print(firstappeareance(A, 27))

# 2
def itemequalindex(A: [int]) -> int:
    l: int = 0
    r: int = len(A) - 1

    while l <= r:
        m: int = l + (r - l) // 2
        c: int = A[m]
        if c == m:
            return c
        elif c < m:
            l = m + 1
        else:
            r = m - 1
    return -1


# A = [-2, 0, 2, 3, 6, 7, 9]
# print(itemequalindex(A))

# 3
def smallest_cyclically_sorted(A: [int]) -> int:
    l: int = 0
    r: int = len(A) - 1
    n: int = len(A) - 1
    f: int = -1
    while l <= r:
        m: int = l + (r - l) // 2
        c: int = A[m]
        # check with the last entry of the array
        if c < A[n - 1]:
            f = c
            # it can get only smaller than this
            r = m - 1
        else:
            # move to right searching for the smallest one
            l = m + 1
    return f


# A = [378, 478, 550, 631 ,703 ,1203, 1220 ,1234 ,1279 ,1358]
# print(smallest_cyclically_sorted(A))

# largest integer whose square is less than or equal to the given integer.
# O(logk)
def squareroot(k: int) -> int:
    m: int = 0
    l: int = 0
    r: int = k

    while l <= r:
        m = l + (r - l) // 2
        if m ** 2 == k:
            return m
        elif m ** 2 < k:
            l = m + 1
        else:
            r = m - 1

    return l - 1


# print(squareroot(300))
# print(squareroot(16))

# O(log(k/s))  - s is tolerance
def squareroot(k: float) -> float:
    (l, r) = (0, 1.0) if k < 1.0 else (1.0, k)
    sq = 0
    while not math.isclose(l, r):
        m = l + (r - l) / 2
        if m ** 2 <= k:
            l = m
        else:
            r = m
    return l


# print(squareroot(16.))


def searchsortedarray(A: [[int]], k: int) -> bool:
    r: int = len(A)
    c: int = len(A[0])
    i: int = 0
    j: int = 0
    while i < r and j < c:
        if A[i][j] == k:
            return True
        elif A[i][j] < k:
            i += 1
        else:
            j += 1

    return False


A = [[-1, 2, 4, 4, 6], [1, 5, 5, 9, 21], [3, 6, 6, 9, 22], [3, 6, 8, 10, 24], [6, 8, 9, 12, 25], [8, 10, 12, 13, 40]]
print(searchsortedarray(A, 7))
print(searchsortedarray(A, 8))
