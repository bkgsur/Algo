import functools


def pm(a):
    s = [[str(e) for e in row] for row in a]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    print('=============================')


def gcd(x, y):
    # make sure y >x
    if x > y:
        return gcd(y, x)
    if x == 0:
        return y
    if not x & 1 and not y & 1:  # both even
        return gcd(x >> 1, y >> 1) << 1
    elif not x & 1 and y & 1:  # y is odd
        return gcd(x >> 1, y)
    elif x & 1 and not y & 1:  # x is odd
        return gcd(x, y >> 1)
    else:  # both odd
        return gcd(x, y - x)


# print(gcd(24, 300))

def missingleastpositive(A):
    for i in range(len(A)):
        while 1 <= A[i] <= len(A) and A[i] != A[A[i] - 1]:
            A[A[i] - 1], A[i] = A[i], A[A[i] - 1]

    return next((i + 1 for i, a in enumerate(A) if a != i + 1), len(A) + 1)


# print(missingleastpositive([3, 5, 4, -1, 5, 1, -1]))

# https://www.youtube.com/watch?v=Pw6lrYANjz4
def buysellk(prices, k):
    print(prices)
    # can hold only on stock at a time
    profits = [[0 for _ in range(len(prices))] for _ in range(k + 1)]
    for attempt in range(len(profits)):  # length = k+1
        profit_not_selling_today = 0
        profit_selling_today = 0
        for day in range(len(profits[attempt])):
            # no profits can be made with attempt=0  and  day = 0 (you cannot make profit buying and selling on day 1)
            if (attempt > 0 and day > 0):
                # Maximum of scenarios 1 and 2
                # 1. Profit made by not selling today - so profit from yesterday till current attempt
                # 2. profit is max of profit made selling today from current attempt(todays price)
                # + maximum profit made from previous attempt on any previous day- cost of buying on that previous day's price.
                profit_not_selling_today = profits[attempt][day - 1]
                # previous days
                max_previous_profit = float('-inf')
                for previous_day in range(0, day):
                    max_previous_profit = max(max_previous_profit,
                                              profits[attempt - 1][previous_day] - prices[previous_day])
                profit_selling_today = prices[day] + max_previous_profit
                profits[attempt][day] = max(profit_not_selling_today, profit_selling_today)
    pm(profits)
    return profits[-1][-1]


# print(buysellk([5,11,3,50,60,90],2))

def maxproductminusone(A):
    least_neg_index = None
    highest_neg_index = None
    least_non_neg_Index = None
    number_of_negatives = 0
    for i in range(len(A)):
        current = A[i]
        if current < 0:
            number_of_negatives += 1
            if least_neg_index is None or A[least_neg_index] > current:
                least_neg_index = i
            if highest_neg_index is None or A[highest_neg_index] < current:
                highest_neg_index = i
        else:
            if least_non_neg_Index is None or A[least_non_neg_Index] > current:
                least_non_neg_Index = i
    idx_to_skip = None
    if number_of_negatives == 0:
        idx_to_skip = least_non_neg_Index
    else:
        if number_of_negatives % 2 == 0:  # if even
            idx_to_skip = least_non_neg_Index
            if least_non_neg_Index is None:  # All numbers negative
                idx_to_skip = highest_neg_index
        else:  # if odd
            idx_to_skip = least_neg_index

    return functools.reduce(lambda p, a: p * a, (a for i, a in enumerate(A) if i != idx_to_skip), 1)


# print(maxproductminusone([3, 2, -1, 4, -1, 6]))


def maxcontiguousincreasingsubarray(A):
    i = 0
    j = i + 1
    maxi = 0
    maxj = 0
    while len(A) > j >= i:
        if A[j - 1] < A[j]:
            j += 1
        else:
            if j - 1 - i > maxj - maxi:
                maxi = i
                maxj = j - 1
            i = j
            j = i + 1

    return maxi, maxj


print(maxcontiguousincreasingsubarray([21, 1111, 13, 15, 113, 117, 119, 17, 23]))
