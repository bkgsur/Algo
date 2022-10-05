import itertools


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
        print(min_sum, max_sum, running_sum)
    return max_sum


print(maxsubarray([-904, -40, -523, -12, -335, -385, -124, -481, -31]))
