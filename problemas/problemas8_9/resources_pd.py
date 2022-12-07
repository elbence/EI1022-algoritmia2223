from typing import Optional
import sys


Vector = list[int]
Matrix = list[list[int]]
Solution = tuple[int, Optional[Vector]]


def read_data(f) -> tuple[int, int, Vector, Matrix]:
    U = int(f.readline())
    N = int(f.readline())
    m = [int(w) for w in f.readline().split()]
    v = [[int(w) for w in l.split()] for l in f.readlines()]
    return U, N, m, v


def process(impl: int, U: int, N: int, m: Vector, v: Matrix) -> Solution:
    if impl == 0:
        return resources_direct(U, N, m, v)
    elif impl == 1:
        return resources_memo(U, N, m, v)
    elif impl == 2:
        return resources_memo_path(U, N, m, v)
    elif impl == 3:
        return resources_iter(U, N, m, v)
    elif impl == 4:
        return resources_iter_red(U, N, m, v)


def resources_direct(U: int, N: int, m: Vector, v: Matrix) -> Solution:
    raise NotImplementedError("resources_direct")


def resources_memo(U: int, N: int, m: Vector, v: Matrix) -> Solution:
    raise NotImplementedError("resources_memo")


def resources_memo_path(U: int, N: int, m: Vector, v: Matrix) -> Solution:
    raise NotImplementedError("resources_memo_path")


def resources_iter(U: int, N: int, m: Vector, v: Matrix) -> Solution:
    raise NotImplementedError("resources_iter")


def resources_iter_red(U: int, N: int, m: Vector, v: Matrix) -> Solution:
    raise NotImplementedError("resources_iter_red")


def show_results(s: int, ds: Optional[Vector]):
    print(s)
    if ds is not None:
        for d in ds:
            print(d)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        impl = 0
    else:
        impl = int(sys.argv[1])
    data = read_data(sys.stdin)
    sol = process(impl, *data)
    show_results(*sol)
