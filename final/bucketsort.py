# 791. Custom Sort String
# SandTare strings composed of lowercase letters. InS, no letter occurs more than once.
# Swas sorted in some custom order previously. We want to permute the characters ofTso that they match the order thatSwas sorted. More specifically, ifxoccurs beforeyinS, thenxshould occur beforeyin the returned string.
# Return any permutation ofT(as a string) that satisfies this property.
import collections
import math
import heapq


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


# print(topkfrequent([1, 1, 1, 2, 2, 4, 4, 4, 4], 2))

# 1057. Campus Bikes
# On a campus represented as a 2D grid, there are Nworkers and Mbikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.
#
# Our goal is to assign a bike to each worker. Among the available bikes and workers,
# we choose the (worker, bike) pair with the shortest Manhattan distance between each other, and assign the bike to that worker.
# (If there are multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index; if there are multiple ways to do that, we choose the pair with the smallest bike index). We repeat this process until there are no available workers.
#
# The Manhattan distance between two points p1and p2is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|. Return a vector ansof length N, where ans[i]is the index (0-indexed) of the bike that the i-th worker is assigned to.


def assignBikes(workers, bikes):
    distances = []
    for worker_index, (wx, wy) in enumerate(workers):
        distances.append([])
        for bike_index, (bx, by) in enumerate(bikes):
            distance = abs(wx - bx) + abs(wy - by)
            distances[-1].append((distance, worker_index, bike_index))
        distances[-1].sort(reverse=True)
    results = [None] * len(workers)
    used_bikes = set()
    # smallest distance for each worker
    least_distances = [distances[i].pop() for i in range(len(workers))]
    heapq.heapify(least_distances)

    while len(used_bikes) < len(workers):
        print(least_distances)
        dist, worker_index, bike_index = heapq.heappop(least_distances)
        if bike_index not in used_bikes:
            results[worker_index] = bike_index
            used_bikes.add(bike_index)
        else:
            heapq.heappush(least_distances, distances[worker_index].pop())

    return results


print(assignBikes([[0, 0], [1, 1], [2, 0]], [[1, 0], [2, 2], [2, 1]]))
