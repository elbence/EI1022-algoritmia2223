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
    vect_pos = [-1] * len(w)  # crea un vector lleno de -1 de long len(w)
    pesos_contenedores: list[int] = [0]
    indices = range(len(w))
    # ordena los indices segun key, en este caso resulta en los valores de mayor a menor
    sorted_indices = sorted(indices, key=lambda i: - w[i])
    for i in sorted_indices:
        # recorrer pesos_contenedores
        for o in range(len(pesos_contenedores)):
            # si encuentra
            if C - pesos_contenedores[o] >= w[i]:
                vect_pos[i] = o
                pesos_contenedores[o] += w[i]
                break
        if vect_pos[i] == -1: # no anyadido
            pesos_contenedores.append(w[i])
            vect_pos[i] = len(pesos_contenedores) - 1

    return vect_pos


def show_results(l: list[int]):
    print(l)


if __name__ == '__main__':
    c, ls = read_data(sys.stdin)
    f_ls = process(c, ls)
    show_results(f_ls)
