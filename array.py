import itertools


# fixed window
def maxsubarray(A, k):
    maxsum = 0
    if len(A) < k or k <= 0:
        return 0
    for i in range(len(A)):
        if (i < k):
            maxsum += A[i]
        else:
            maxsum = max(maxsum, maxsum + A[i] - A[i - k])
    return maxsum


# print(maxsubarray([4,2,1,7,8,1,2,8,1,0],3))

# sliding window
def smallestsubarraySize(A, k):
    i = 0
    j = 0
    minlength = 0
    currentsum = 0
    while len(A) > j >= i:
        currentsum = sum(A[i:j + 1])
        if currentsum >= k:
            if j - i + 1 == 1:
                return 1
            else:
                minlength = min(minlength, j - i + 1)
                i += 1
        else:
            j += 1
    return minlength


# print(smallestsubarraySize([4,2,2,7,8,1,2,8,10],8))

# sliding window - extra storage
def longestuniquechars(S, k):
    d = {}
    maxlength = 0
    U = []
    left = 0
    for i in range(len(S)):
        c = S[i]
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1
            U.append(c)
        if len(d) <= k:
            maxlength = max(maxlength, i - left + 1)
        else:
            d.pop(U[left])
            left += 1

    return maxlength


print(longestuniquechars(['A', 'A', 'A', 'H', 'H', 'I', 'B', 'C'], 2))
