import sys
from typing import TextIO


def read_data(f: TextIO) -> tuple[int, list[int]]:

    w = []
    C = int(f.readline())
    for line in f: # same: while a: a = int(f.readline())
        w.append(int(line))

    return C, w


# C = capacidad contenedor, w = lista con pesos y elementos
def process(C: int, w: list[int]) -> list[int]:
    vect_pos = [-1] * len(w) # crea un vector lleno de -1 de long len(w)
    ca: int = 0 # pos to add
    w_ca: int = 0 # peso de contenedor actual
    for i in range(len(w)):
        if not C - w_ca > w[i]: # no cabe
            ca += 1
            w_ca = 0
        w_ca += w[i]
        vect_pos[i] = ca

    return vect_pos


def show_results(l: list[int]):
    print(l)


if __name__ == '__main__':
    c, ls = read_data(sys.stdin)
    f_ls = process(c, ls)
    show_results(f_ls)
