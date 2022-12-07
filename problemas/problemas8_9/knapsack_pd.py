from typing import Optional
import sys


def read_data(f) -> tuple[int, list[int], list[int]]:
    W = int(f.readline())
    v = []
    w = []
    for line in f.readlines():
        p = line.strip().split()
        v.append(int(p[0]))
        w.append(int(p[1]))
    return W, v, w


Score = int
Decision = int
Solution = tuple[Score, Optional[list[Decision]]]

SParams = tuple[int, int]

Mem = dict[SParams, Score]
MemPath = dict[SParams, tuple[Score, SParams, Decision]]

def process(impl: int, C: int, v: list[int], w: list[int]) -> Solution:
    if impl == 0:
        return knapsack_direct(w, v, C)
    elif impl == 1:
        return knapsack_memo(w, v, C)
    elif impl == 2:
        return knapsack_memo_path(w, v, C)
    elif impl == 3:
        return knapsack_iter(w, v, C)
    elif impl == 4:
        return knapsack_iter_red(w, v, C)


def show_results(sol: Solution):
    tv, decisions = sol
    print(tv)
    if decisions is not None:
        for d in decisions:
            print(d)


def knapsack_direct(w: list[int], v: list[int], C: int) -> Solution:
    raise NotImplementedError("knapsack_direct")


def knapsack_memo(w: list[int], v: list[int], C: int) -> Solution:
    raise NotImplementedError("knapsack_memo")


def knapsack_memo_path(w: list[int], v: list[int], C: int) -> Solution:
    raise NotImplementedError("knapsack_memo_path")


def knapsack_iter(w: list[int], v: list[int], C: int) -> Solution:
    raise NotImplementedError("knapsack_iter")


def knapsack_iter_red(w: list[int], v: list[int], C: int) -> Solution:
    raise NotImplementedError("knapsack_iter_red")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        impl = 0
    else:
        impl = int(sys.argv[1])
    C, v, w = read_data(sys.stdin)
    res = process(impl, C, v, w)
    show_results(res)
