# 791. Custom Sort String
# SandTare strings composed of lowercase letters. InS, no letter occurs more than once.
# Swas sorted in some custom order previously. We want to permute the characters ofTso that they match the order thatSwas sorted. More specifically, ifxoccurs beforeyinS, thenxshould occur beforeyin the returned string.
# Return any permutation ofT(as a string) that satisfies this property.
import collections


def customsort(S, T) -> str:
    d = {}
    for c in T:
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1

    ans = ''
    for c in S:
        for i in range(d.get(c, 0)):
            ans += c
        d[c] = 0
    # chars not in S but in T
    for i in range(26):
        for j in range(d.get(chr(i + 97), 0)):
            ans += chr(i + 97)
    return ans


# print(customsort('abc', 'dcbaaakjhkh'))

# 347. Top K Frequent Elements
# Given a non-empty array of integers, return the k most frequent elements.

def topkfrequent(A, k) -> []:
    m = [0] * (len(A) + 1)
    for i in range(len(m)):
        m[i] = []
    cnt = collections.Counter(A)
    for v in cnt:
        m[cnt[v]].append(v)
    ans = []
    for l in m[::-1]:
        ans += l
        if len(ans) >= k:
            break
    return ans


print(topkfrequent([1, 1, 1, 2, 2, 4, 4, 4, 4], 2))
