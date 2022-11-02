def n_queen(n: int) -> [[int]]:
    def helper(row):
        if row == n:
            result.append(list(col_placement))
            return
        else:
            for col in range(n):
                if all(abs(col - c) not in (0, row - i) for i, c in enumerate(col_placement[:row])):
                    col_placement[row] = col
                    helper(row + 1)

    result: [[int]] = []
    col_placement: [int] = [0] * n
    # start with first row
    helper(0)
    return result


# print(n_queen(4))

# O(n*n!) - there are n! permutations for n elements
def allpermutations(A: [int]) -> [[int]]:
    def helper(i: int) -> None:
        if i == len(A):
            result.append(A.copy())
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            helper(i + 1)
            A[i], A[j] = A[j], A[i]

    result: [[int]] = []
    helper(0)
    return result


# A = [2, 3, 5, 7]
# p = allpermutations(A)
# print(len(p), p)

# time - O(n)
# space - O(1)
def next_biggest(A:[int]) -> None:
    inflectionpoint = -1
    i: int = len(A) - 2
    # longest non-decreasing sub array from last
    while i >= 0:
        if A[i] >= A[i + 1]:
            i -= 1
        else:
            inflectionpoint=i
            break

    if inflectionpoint == -1:
        return None
    # replace the inflection point item with the smallest item  greater than it in the non-decreasing sub array from last

    i = len(A) - 1
    while i > inflectionpoint:
        if A[i] > A[inflectionpoint]:
            A[i], A[inflectionpoint] = A[inflectionpoint], A[i]
            break
        else:
            i -= 1
    # reverse items after inflection point
    A[inflectionpoint + 1:] = reversed(A[inflectionpoint + 1:])
    return A

# A= [1,0,3,2]
# print(next_biggest(A))

def allpermutations2(A: [int]) -> [[int]]:
    result= []
    while True:
        result.append(A.copy())
        A= next_biggest(A)
        if not A:
            break
    return result
A = [2, 3, 5, 7]
p = allpermutations2(A)
print(len(p), p)