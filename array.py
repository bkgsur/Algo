import itertools
import random

# fixed window
def maxsubarray(A, k):
    #sub array with max sum of size k
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
    #smallest sub array of sum value k
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


def evenodd(A:[int])->None:
    evenindex=0
    oddindex= len(A)-1
    while evenindex<=oddindex:
        if A[evenindex]%2 ==0: # even number
            evenindex+=1
        else: # odd number
            A[evenindex], A[oddindex] = A[oddindex], A[evenindex]
            oddindex-=1

# A= [ random.randint(1,50) for i in range(11)]
# print(A)
# evenodd(A)
# print(A)


def incrementbyone(A:[int])->None:
    A[-1]+=1

    for i in range(len(A)-1,0,-1):
        print(A, i, A[i])
        if A[i]==10:
            A[i-1]+=1
            A[i]=0
    if(A[0]==10):
        A[0]=1
        A.append(0)

# A = [9,9,9]
# print(A)
# incrementbyone(A)
# print(A)

def multiply(n1:[int],n2:[int])->[int]:
    result = [0]* (len(n1)+ len(n2))
    print(result, len(result))
    for i in reversed(range(len(n1))):
        for j in reversed(range(len(n2))):
            print(i,j,i+j+1)

multiply([1,2,3],[4,5,6])

