import collections
import math
import operator
import sys
import numpy as np

print(sys.version)


def coinchange(amount):
    change = 0
    p = [100, 25, 10, 5, 1]
    for i in p:
        if (i <= amount):
            change += amount // i
            amount = amount % i
    return change


# print(coinchange(176))

def pairTASK(times):
    pairedTasks = collections.namedtuple("pt", ('t1', 't2'))
    times.sort()
    return [pairedTasks(times[i], times[~i]) for i in range(len(times) // 2)]


# print(pairTASK([5,2,3,1]))

def leastwait(times):
    times.sort()
    waittime = 0
    for i in range(1, len(times)):
        waittime += (len(times) - i) * times[i - 1]
    return waittime


# print(leastwait([5,2,3,1]))

Intervals = collections.namedtuple("intervals", ('l', 'r'))
seq = [Intervals(0, 3), Intervals(2, 6), Intervals(3, 4), Intervals(6, 9)]


def leastvisit(intervals):
    intervals.sort(key=operator.attrgetter('r'))
    least_visit_time = float('-inf')
    numvisit = 0
    for interval in intervals:
        if (least_visit_time < interval.l):
            numvisit += 1
            least_visit_time = interval.r
    return numvisit


# print(leastvisit(seq))

p = collections.namedtuple('p', ('x', 'y'))
pts = [p(2, 2), p(2, 1), p(3, 4), p(1, 1)]
origin = p(1, 1)
angle = 90


def maxcoveredInPlane(origin, angle, points):
    onorigin = 0
    for p in points:
        if (origin.x == p.x and origin.y == p.y):
            onorigin += 1
            points.remove(p)
    # print(points)
    angles = getAngles(origin, points)
    print(angles)
    angles.sort()
    largestAngle = max(angles)
    for i in range(len(angles)):
        if ((angles[i] + 360 - largestAngle) < angle):
            angles.append(angles[i] + 360)

    maxpoints = 0
    start = 0
    for end in range(0, len(angles)):
        if ((angles[end] - angles[start]) < angle):
            maxpoints = max(maxpoints, end + 1 - start)
        else:
            start += 1
    return maxpoints + onorigin


def getAngles(origin, points):
    angles = []
    for p in points:
        opposite = origin.y - p.y
        adj = origin.x - p.x
        angle = math.atan(opposite / adj) * 180 / math.pi
        if (angle < 0):
            angle += 360
        angles.append(angle)
    return angles


# print(maxcoveredInPlane(origin, angle, pts))

# p is sorted
# O(n)
def hastwosum(p, k):
    i = 0
    j = len(p) - 1
    while i <= j:
        if p[i] + p[j] == k:
            return True
        elif p[i] + p[j] < k:
            i += 1
        else:
            j -= 1
    return False


# print(hastwosum([-2,1,2,4,7,11],13))

# O(n) * O(nlogn) = O(n^2)
def hasthreesum(p, k):
    p.sort()  # O(nlogn)
    return any(hastwosum(p, k - i) for i in p)


# print(hasthreesum([-2, 1, 2, 4, 7, 11], 1300))


# Solve the same problem when k, the number of elements to sum, is an additional input.
def hassum():
    r = len(A)
    # memo = [[[[False] * K] * t] * r]
    memo = [[[False for col in range(K + 1)] for col in range(t + 1)] for row in range(r + 1)]
    print(np.array(memo).shape)
    return subsetsum(memo, t, 0, 0, r, K)


def subsetsum(memo, target, i, s, size, k):
    print(i, s, k)
    if s == target and k == 0:
        memo[i][s][k] = True
        return memo[i][s][k]
    elif s < target and i < size:
        if memo[i][s][k]:
            return memo[i][s][k]
        memo[i][s][k] = subsetsum(memo, target, i + 1, s + A[i], size, k - 1) or subsetsum(memo, target, i + 1, s, size,
                                                                                           k)
    return False


A = [-2, 1, 2, 4, 7, 11]
t = 13
K = 2


# print('hassum', hassum())


def majoritysearch(inputstream):
    c = inputstream[0]
    ccount = 1
    for i in range(1, len(inputstream)):
        print(inputstream[i], c, ccount)
        if inputstream[i] == c:
            ccount += 1
        elif inputstream[i] != c:
            ccount -= 1
        if ccount <= 0:
            c = inputstream[i]
            ccount = 1
    return c


# print(majoritysearch(['b', 'a', 'c', 'a', 'a', 'b', 'a', 'a', 'c', 'a']))

MPG = 20
gallons = [50, 20, 5, 30, 25, 10, 10]
distances = [900, 600, 200, 400, 600, 200, 100]
cities = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


def gasup(cities, gallons, distances):
    maxdeifict = 0
    deficitcityIndex = 0
    currentdeficit = 0
    for i in range(1, len(gallons)):
        currentdeficit += gallons[i - 1] - distances[i - 1] // MPG
        if currentdeficit < maxdeifict:
            maxdeifict = currentdeficit
            deficitcityIndex = i
    print(deficitcityIndex)
    return cities[deficitcityIndex]


# print(gasup(cities, gallons, distances))


def max_water_trap(heights):
    maxtrap = 0
    i = 0
    j = len(heights) - 1
    while i < j:
        currenttrap = (j - i) * min(heights[i], heights[j])
        if currenttrap > maxtrap:
            maxtrap = currenttrap
        if heights[i] <= heights[j]:
            i += 1
        else:
            j -= 1
    return maxtrap


# print(max_water_trap([1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1]))


def largestreactangleArea(heights):
    maxArea = 0
    stack = []  # contains index, height pair
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height*(i - index))
            start = index
        stack.append((start, h))
    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
    return maxArea


print(largestreactangleArea([1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]))
