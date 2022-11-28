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

# 283. Move Zeros
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
    # print(zeros, l)

    for i in zeros:
        if i - l > 0:
            A[i], A[l] = A[l], A[i]
            k = l + 1

            while i - k > 0:
                A[i], A[k] = A[k], A[i]
                k += 1
        l += 1


# A = [0,1, 3, 0, 12, 17, 0, 6, 0]
#
# print(A)
# movezerotofront(A)
# print(A)

# 26. Remove Duplicates from Sorted Array
# Given a sorted arraynums, remove the duplicates in-place such that each element appear only _once _and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    fast = 0
    slow = 0
    length = 1
    while fast < len(nums):
        if nums[fast] == nums[slow]:
            fast += 1
        else:
            slow += 1
            print(slow, fast)
            nums[slow] = nums[fast]
            fast += 1
            length += 1
    print(nums)
    return length


# print(removeDuplicates([1, 2, 2]))
# print(removeDuplicates([1, 1, 2]))


# print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

def merge(nums1, m, nums2, n):
    i = m-1
    j = n-1
    total = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[total] = nums1[i]
            i -= 1
        else:
            nums1[total] = nums2[j]
            j -= 1
        total -= 1

    if i < 0:
        while j >= 0:
            nums1[total] = nums2[j]
            j -= 1
    if j < 0:
        while i >= 0:
            nums1[total] = nums1[i]
            i -= 1
    return nums1

print(merge([1,2,3,0,0,0],3,[2,5,6],3))
