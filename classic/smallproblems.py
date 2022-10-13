from typing import Dict
from functools import lru_cache
from sys import getsizeof


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
    s = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA"*100
    compressed: CompressedGene  = CompressedGene(s)
    print(compressed.bit_string)
    ds= compressed._decompress()
    print(ds)
    print(s==ds, getsizeof(compressed.bit_string),getsizeof(ds),(getsizeof(compressed.bit_string)/getsizeof(ds))*100)


testcompression()
