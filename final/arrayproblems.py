# 11. Container With Most Water
def watercontainer(H=[]) -> (int, (int, int)):
    res = 0
    (l1, r1) = (0, 0)
    l = 0
    r = len(H) - 1
    while l < r:
        current = min(H[l], H[r]) * (r - l)
        if res < current:
            res = current
            (l1, r1) = (l, r)

        if l < r:
            l += 1
        else:
            r -= 1

    return res, (l1, r1)


# print(watercontainer([1, 8, 6, 2, 5, 4, 8, 3, 7]))


def movezerotofront(A: []) -> None:
    zeros = []
    l = -1
    nonzero = False

    for i in range(len(A)):
        if A[i] == 0:
            zeros.append(i)
        else:
            nonzero = True
        if not nonzero:
            l += 1
    if l == -1:
        l = 0
    #print(zeros, l)

    for i in zeros:
        if i - l > 0:
            A[i], A[l] = A[l], A[i]
            k =l+1

            while i-k>0:
                A[i], A[k] = A[k], A[i]
                k+=1
        l+=1


A = [0,1, 3, 0, 12, 17, 0, 6, 0]

print(A)
movezerotofront(A)
print(A)
