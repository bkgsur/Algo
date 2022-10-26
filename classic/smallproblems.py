import functools
from typing import Dict, Tuple, TypeVar, Generic, List, cast
from functools import lru_cache
from sys import getsizeof
from secrets import token_bytes


T = TypeVar('T')


# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# print(fib(5))

memo: Dict[int, int] = {0: 0, 1: 1}


def fib2(n: int) -> int:
    if n not in memo:
        memo[n] = fib2(n - 1) + fib2(n - 2)
    return memo[n]


# print(fib2(50))


@lru_cache(maxsize=None)
def fib3(n: int) -> int:
    if n < 2:
        return n
    return fib3(n - 2) + fib3(n - 1)


# print(fib3(50))


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def __str__(self):
        return self._decompress()

    def _decompress(self) -> str:
        gene: str = ''
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError("Invalid bit:{}".format(bits))

        return gene[::-1]


def testcompression():
    s = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    compressed: CompressedGene = CompressedGene(s)
    # print(compressed.bit_string)
    ds = compressed._decompress()
    print(ds)
    print(s == ds, getsizeof(compressed.bit_string), getsizeof(ds),
          (getsizeof(compressed.bit_string) / getsizeof(ds)) * 100)


# testcompression()

class simpleencrypt:
    byteorder: str = 'big'
    key: int = None
    input: str = None

    def __init__(self, S: str):
        self.key = int.from_bytes(token_bytes(len(S)), self.byteorder)
        self.input = S

    def encrypt(self) -> int:
        return int.from_bytes(self.input.encode(), self.byteorder) ^ self.key

    def decrypt(self, product: int) -> str:
        extracted: int = product ^ self.key
        return extracted.to_bytes((extracted.bit_length() + 7) // 8, self.byteorder).decode()


def testsimpleencrypt(S: str) -> None:
    print(S)
    se: simpleencrypt = simpleencrypt(S)
    output: str = se.decrypt(se.encrypt())
    print('Y') if S == output else print('N', output)


# testsimpleencrypt('i am done!')


# using leibniz formula to calculate PI
# https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
def calculatepi(n: int) -> float:
    pi: float = 0

    items: [float] = [(4 / (1 + ((i - 1) * 2))) * (-1 if i % 2 == 0 else 1) for i in
                      range(1, n + 1)]
    pi = functools.reduce(lambda a1, a2: a1 + a2, items, 0)

    return pi


# print(calculatepi(1000000))

# Tower of Hanoi
class towerofhanoi(Generic[T]):
    class tower(Generic[T]):
        def __init__(self) -> None:
            self._container: List[T] = []

        def push(self, item: T) -> None:
            self._container.append(item)

        def pop(self) -> T:
            return self._container.pop()

        def __repr__(self) -> str:
            return repr(self._container)

    def __init__(self):

        self.tower_c: towerofhanoi.tower[T] = None
        self.tower_b: towerofhanoi.tower[T] = None
        self.tower_a: towerofhanoi.tower[T] = None
        self.n: int = None

    def build(self, num_discs: int = 3):
        self.n = num_discs
        self.tower_a = self.tower()
        self.tower_b = self.tower()
        self.tower_c = self.tower()
        for i in range(1, self.n + 1):
            self.tower_a.push(cast(T, i))

    def move(self, start: tower[T], end: tower[T], temp: tower[T], n: int) -> None:
        if n == 1:
            end.push(start.pop())
        else:
            self.move(start, temp, end, n - 1)
            self.move(start, end, temp, 1)
            self.move(temp, end, start, n - 1)

    def test(self) -> None:
        self.build()
        self.move(self.tower_a, self.tower_c, self.tower_b, self.n)


# t: towerofhanoi[chr] = towerofhanoi()
# t.test()
# print(t.tower_a, t.tower_c, t.tower_b)
