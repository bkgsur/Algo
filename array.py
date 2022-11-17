import itertools
import random


# fixed window
def maxsubarray(A, k):
    # sub array with max sum of size k
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
    # smallest sub array of sum value k
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


# print(longestuniquechars(['A', 'A', 'A', 'H', 'H', 'I', 'B', 'C'], 2))


def evenodd(A: [int]) -> None:
    evenindex = 0
    oddindex = len(A) - 1
    while evenindex <= oddindex:
        if A[evenindex] % 2 == 0:  # even number
            evenindex += 1
        else:  # odd number
            A[evenindex], A[oddindex] = A[oddindex], A[evenindex]
            oddindex -= 1


# A= [ random.randint(1,50) for i in range(11)]
# print(A)
# evenodd(A)
# print(A)

def dutchflag(A: [int], pindex: int) -> None:
    p = A[pindex]
    print(A, p)
    smallest, middle, largest = 0, 0, len(A) - 1
    while middle <= largest:
        if A[middle] < p:
            A[smallest], A[middle] = A[middle], A[smallest]
            smallest += 1
            middle += 1
        elif A[middle] == p:
            middle += 1
        else:
            A[middle], A[largest] = A[largest], A[middle]
            largest -= 1


# A = [0,1,2,0,2,1,1]
# dutchflag(A,1)
# print(A)

def tictactoe(moves):
    if len(moves) < 5:
        return "Pending"

    def check(startIndex, player):
        cols = set()
        rows = set()
        diag = True
        move_count = 0
        for i in range(startIndex, len(moves), 2):
            move = moves[i]
            cols.add(move[1])
            rows.add(move[0])
            move_count += 1
            if diag:
                diag = move[0] == move[1] or (move[0] + move[1] == 2)
            # print(move,diag,cols,rows, player)
        if (diag == True or len(cols) == 1 or len(rows) == 1) and move_count == 3:
            return True
        return False

        if check(0, "A"):
            return "A"
        if check(1, "B"):
            return "B"
        if len(moves) == 9:
            return "Draw"
        return "Pending"


def incrementby1(A: [int]) -> None:
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] == 10:
            A[i - 1] += 1
            A[i] = 0
    if A[0] == 10:
        A[0] = 1
        A.append(0)


# A = [9, 9, 9]
# incrementby1(A)
# print(A)

def largestsubarray(A: [int]) -> (int, [int]):
    n = len(A)
    minIndex=-1
    maxIndex=-1
    maxsum = float('-inf')
    def helper(i,maxsum):
        print(maxsum)
        if i == n:
            return maxsum
        currentsum=0
        for j in range(i, n):
            currentsum+=A[j]
            if currentsum>maxsum:
                maxsum = currentsum

        helper(i+1, maxsum)
    maxsum = helper(0,maxsum)
    print(maxsum)



largestsubarray([-2, 1, 6, 8, -20, 7])
