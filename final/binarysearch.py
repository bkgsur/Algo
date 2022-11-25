def firstbadversion(n) -> int:
    def isbadversion(k):
        if k in (1, 2, 3):
            return False
        else:
            return True

    i = 1
    j = n
    while i <= j:
        m = i + (j - i) // 2
        if isbadversion(m):
            j = m - 1
        else:
            i = m + 1

    return i


# print(firstbadversion(5))

# 162. Find Peak Element
# O(logn)
def findpeakelement(A: [int]) -> int:
    print(A)
    low = 0
    high = len(A) - 1
    while low < high:
        mid = low + (high - low) // 2
        if A[mid] < A[mid + 1]:
            low = mid
        elif A[mid] < A[mid - 1]:
            high = mid
        else:
            return mid
    return -1


#
# print(findpeakelement([1, 2, 7, 8, 9, 6, 4]))
# print(findpeakelement([11, 0, 11, 13, 5, 6, 4]))

# 183.Wood Cut

def woodcut(A, k) -> int:
    l = 1
    r = max(A)

    def parts(m):
        sum = 0
        if m == 0:
            return sum
        else:
            for l in A:
                sum += l // m

        return sum

    while l <= r:
        mid = l + (r - l) // 2
        pieces = parts(mid)
        # print(pieces)
        if pieces >= k:

            l = mid + 1
        else:
            r = mid - 1
    if r == 0:
        return 0

    pieces = parts(r)
    # print(pieces,l,r)
    if pieces >= k:
        return r
    else:
        return 0


# print(woodcut([232,124,456],7))

# 33. Search in Rotated Sorted Array

def searchsortedarray(A, k) -> int:
    l = 0
    r = len(A) - 1
    final = A[r]
    while l <= r:
        mid = l + (r - l) // 2
        # print(mid,l,r,A[mid])
        if A[mid] == k:
            return mid
        elif A[mid] > k:
            if k > final:
                r = mid - 1
            else:
                l = mid
        else:
            l = mid + 1
    return -1


A = [4, 5, 6, 7, 0, 1, 2]


# print(searchsortedarray(A,4))
# print(searchsortedarray(A,8))
# print(searchsortedarray(A,0))
# print(searchsortedarray(A,7))


# 410 - Split Array Largest Sum
# T = n*log (sum of array)
# log (sum) because the binary search is based on this sum.
# n - for each binary search attempt - we loop through the n elements to find is split valid
def splitarraylargestsum(A, k) -> int:
    def validsplit(splitValue):
        sumsplit = 0
        count = 1
        for num in A:
            sumsplit += num
            if sumsplit > splitValue:
                count += 1
                sumsplit = num
                if count > k:
                    return False

        return True

    minpossiblesum = max(A)  # initial  possible sum and we will improve on this
    sumArray = sum(A)  # initially assume this is the min largest sum . It could also be float inf

    l = minpossiblesum
    r = sumArray
    res = r
    while l <= r:
        mid = l + (r - l) // 2
        isvalidsplit = validsplit(mid)
        print("left - {}, right - {}, mid - {}, valid - {}".format(l, r, mid, isvalidsplit))
        if isvalidsplit:  # the mid value is the current min largest sum
            res = mid
            r = mid - 1
        else:
            l = mid + 1

    return res


# A = [7, 2, 5, 10, 8]
# print(splitarraylargestsum(A, 3))

# 658. Find K Closest Elements
# A is sorted
# T - log n-k
def kcloseset(A,k,target):
    l =0
    r = len(A)-k-1
    while l<r:
        mid = l + (r-l)//2
        if target - A[mid]> A[mid]-target:
            l = mid+1
        else:
            r = mid

    return A[l:l+k]
A = [1,2,3,4,5]
# k=4
# print(kcloseset(A,2,5))
# print(kcloseset(A,k,-1))



