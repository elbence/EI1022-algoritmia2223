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
Decision = int  # 0 - 1 (grab - don't grab)
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
    def S(c: int, n: int) -> Score:
        if n == 0:
            return 0

        if w[n-1] <= c:  # n already > 0
            return max(S(c, n-1),  # don't grab object
                       S(c - w[n-1], n-1) + v[n-1])  # grab object
        else:  # object didn't fit
            return S(c, n-1)  # don't grab object

    return S(C, len(v)), None


def knapsack_memo(w: list[int], v: list[int], C: int) -> Solution:
    def S(c: int, n: int) -> Score:
        if n == 0:
            return 0

        if (c, n) not in mem:
            if w[n - 1] <= c:  # n already > 0
                mem[c, n] = max(S(c, n - 1),  # don't grab object
                                S(c - w[n - 1], n - 1) + v[n - 1])  # grab object
            else:  # object didn't fit
                mem[c, n] = S(c, n - 1)  # don't grab object
        return mem[c, n]

    mem: dict[SParams, Score] = {}
    return S(C, len(v)), None


# Costes:
# Espacial = O(C*N) ; numero de celdas que se generan
# Temporal = O(1) * C(espacial) ; coste rellenado 1 celda * numero de celdas
def knapsack_memo_path(w: list[int], v: list[int], C: int) -> Solution:
    def S(c: int, n: int) -> Score:
        if n == 0:
            return 0

        if (c, n) not in mem:
            if w[n - 1] <= c:  # n already > 0
                mem[c, n] = max((S(c, n - 1),
                                 (c, n - 1), 0),  # don't grab object
                                (S(c - w[n - 1], n - 1) + v[n - 1],
                                 (c - w[n - 1], n - 1), 1))  # grab object
            else:  # object didn't fit
                mem[c, n] = S(c, n - 1), (c, n - 1), 0  # don't grab object
        return mem[c, n][0]

    mem: dict[SParams, tuple[Score, SParams, Decision]] = {}
    score: Score = S(C, len(v))
    # retrieve taken path (decisions)
    decisions: list[Decision] = []
    c, n = C, len(v)
    while n > 0:
        _, (c, n), d = mem[c, n]
        decisions.append(d)

    decisions.reverse()
    return score, decisions


def knapsack_iter(w: list[int], v: list[int], C: int) -> Solution:
    mem: dict[SParams, tuple[Score, SParams, Decision]] = {}

    for c in range(C+1):
        mem[c, 0] = 0, (-1, -1), -1

    for n in range(1, len(v)+1):
        for c in range(C + 1):
            if w[n - 1] <= c:
                mem[c, n] = max((mem[c, n - 1][0],
                                 (c, n - 1), 0),  # don't grab object
                                (mem[c - w[n - 1], n - 1][0] + v[n - 1],
                                 (c - w[n - 1], n - 1), 1))  # grab object
            else:  # object didn't fit
                mem[c, n] = mem[c, n - 1][0], (c, n - 1), 0  # don't grab object

    score: Score = mem[C, len(v)][0]
    # retrieve taken path (decisions)
    decisions: list[Decision] = []
    c, n = C, len(v)
    while n > 0:
        _, (c, n), d = mem[c, n]
        decisions.append(d)

    decisions.reverse()
    return score, decisions


def knapsack_iter_red(w: list[int], v: list[int], C: int) -> Solution:
    previous: list[Score] = [-1] * (C + 1)
    current: list[Score] = [-1] * (C + 1)

    for c in range(C + 1):
        current[c] = 0

    for n in range(1, len(v) + 1):
        previous, current = current, previous
        for c in range(C + 1):
            if w[n - 1] <= c:
                current[c] = max(previous[c],
                                 previous[c - w[n-1]] + v[n-1])
            else:  # object didn't fit
                current[c] = previous[c]

    score: Score = current[C]
    return score, None


if __name__ == "__main__":
    if len(sys.argv) == 1:
        impl = 0
    else:
        impl = int(sys.argv[1])
    C, v, w = read_data(sys.stdin)
    res = process(impl, C, v, w)
    show_results(res)
