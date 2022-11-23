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


print(findpeakelement([1, 2, 7, 8, 9, 6, 4]))
print(findpeakelement([11, 0, 11, 13, 5, 6, 4]))
