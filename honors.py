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


#print(gcd(24, 300))

def missingpositive(A):

    for i in range(len(A)):
        while 1 <= A[i] <= len(A) and A[i] != A[A[i] - 1]:
            A[A[i]-1], A[i]= A[i],  A[A[i]-1]

    return next((i + 1 for i, a in enumerate(A) if a != i + 1), len(A) + 1)


print(missingpositive([3, 5, 4, -1, 5, 1, -1]))
