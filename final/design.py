import heapq
import string


# 348. Design Tic-Tac-Toe

class tictac:
    def __init__(self, size: int) -> None:
        self.n = size

    def play(self, moves: [(int, int, int)]) -> int:
        rows: [int] = [0] * self.n
        cols: [int] = [0] * self.n
        diagcount: int = 0
        antidiagonal: int = 0
        for move in moves:

            row = move[0]
            col = move[1]
            player = move[2]

            if player == 1:
                rows[row] += 1
                cols[col] += 1
                if row == col:
                    diagcount += 1
                if row + col == self.n - 1:
                    antidiagonal += 1
                if rows[row] == self.n or cols[col] == self.n or diagcount == self.n or antidiagonal == self.n:
                    return 1
            elif player == 2:
                rows[row] -= 1
                cols[col] -= 1
                if row == col:
                    diagcount -= 1
                if row + col == self.n - 1:
                    antidiagonal -= 1
                if rows[row] == -self.n or cols[col] == -self.n or diagcount == -self.n or antidiagonal == -self.n:
                    return 2


# t = tictac(3)
# print(t.play([(0, 0, 1), (1, 1, 1), (2, 2, 1)]))

# =============================================================
# 346. Moving Average from Data Stream

class MovingAverage:

    def __init__(self, size: int):
        self.n = size
        self.S: [int] = [0] * size
        self.i = 0
        self.count = 0

    def next(self, val: int) -> float:
        if self.count < self.n:
            self.count += 1
        self.S[self.i] = val
        self.i = (self.i + 1) % 3
        return float(sum(self.S) / self.count)


# m = MovingAverage(3);
# print(m.next(1), m.i)
# print(m.next(10), m.i)
# print(m.next(3), m.count,m.S)
# print(m.next(5), m.count, m.S)
# print(m.next(7), m.count, m.S)
# print(m.next(12), m.i, m.S)

# =============================================================
# 281. Zigzag Iterator
def zigzagiterator(A: [[]]) -> []:
    index: int = 0
    i: int = 0
    output: [int] = []
    totalelements = 0
    while True:
        totalelements = 0
        for l in A:
            totalelements += len(l)
            if i < len(l):
                output.append(l[i])
            index += 1
        i += 1
        if len(output) == totalelements:
            break

    return output


# print(zigzagiterator([[], [1, 2, 3], [4, 5, 6, 7], [8, 9], []]))


# 341. Flatten Nested List Iterator

def flattenlists(A: [[]]) -> []:
    print(A)
    S = []
    Output = []
    for l in A:
        if isinstance(l, int):
            S.append(l)
        else:
            for e in l:
                S.append(e)

    return S


# print(flattenlists([[1,1],2,[4,5]]))

# 622. Design Circular Queue

class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.S = []
        self.n = k

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.S) < self.n:
            self.S.append(value)
            return True
        return False

    def deQueue(self):
        """
        :rtype: bool
        """
        if len(self.S) > 0:
            self.S.remove(self.S[-1])
            return True
        return False

    def Front(self):
        """
        :rtype: int
        """
        if len(self.S) > 0:
            return self.S[0]
        else:
            return -1

    def Rear(self):
        """
        :rtype: int
        """
        if len(self.S) > 0:
            return self.S[-1]
        else:
            return -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        return len(self.S) == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.S) == self.n


# myCircularQueue = MyCircularQueue(3);
# print(myCircularQueue.enQueue(1))#; // return True
# print(myCircularQueue.enQueue(2))#; // return True
# print(myCircularQueue.enQueue(3))#; // return True
# print(myCircularQueue.enQueue(4))#; // return False
# print(myCircularQueue.Rear())#;     // return 3
# print(myCircularQueue.isFull())#;   // return True
# print(myCircularQueue.deQueue())#;  // return True
# print(myCircularQueue.enQueue(4))#; // return True
# print(myCircularQueue.Rear())#;     // return 4

# ========================================

# 295. Find Median from Data Stream

class MedianFinder:
    def __init__(self):

        self.left, self.right = [], []

    def addNum(self, num):
        heapq.heappush(self.left, - heapq.heappushpop(self.right, num))
        # if odd num of elements - then right has the smallest of the right
        if len(self.right) < len(self.left):
            heapq.heappush(self.right, -heapq.heappop(self.left))

    def findMedian(self):
        if len(self.right) > len(self.left):
            return float(self.right[0])
        else:
            return (self.right[0] - self.left[0]) / 2.0

m = MedianFinder()
for i in [2,3,4]:
    m.addNum(i)
    print(m.findMedian())
