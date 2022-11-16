from __future__ import annotations

import sys
from collections.abc import Iterator
from dataclasses import dataclass
from math import ceil
from typing import TextIO, Iterable

from algoritmia.schemes.bab_scheme import BoundedDecisionSequence, bab_min_solve


def read_data(f: TextIO) -> tuple[int, list[int]]:

    w = []
    C = int(f.readline())
    for line in f: # same: while a: a = int(f.readline())
        w.append(int(line))

    return C, w


# C = capacidad contenedor, w = lista con pesos y elementos
def process(C: int, w: list[int]) -> list[int]:
    @dataclass
    class Extra:
        pesos_contenedores: list[int]

    class BinpackingBDS(BoundedDecisionSequence):

        def calculate_opt_bound(self) -> int:  # num contenedores
            resto = sum(w[len(self):])
            for nc in range(len(self.extra.pesos_contenedores)):
                resto -= C - self.extra.pesos_contenedores[nc]
                if resto <= 0:
                    return len(self.extra.pesos_contenedores)
            nc_extra = ceil(resto / C)
            return len(self.extra.pesos_contenedores) + nc_extra

        def calculate_pes_bound(self) -> int:  # num contenedores
            pesos_contenedores2 = self.extra.pesos_contenedores[:]
            for i in range(len(self), len(w)):
                for nc in range(len(self.extra.pesos_contenedores)):
                    if pesos_contenedores2[nc] + w[i] <= C:
                        pesos_contenedores2[nc] += w[i]
                        break
                else:
                    pesos_contenedores2.append(w[i])
            return len(pesos_contenedores2)

        def is_solution(self) -> bool:
            return len(self) == len(w)

        def successors(self) -> Iterator[BinpackingBDS]:
            i = len(self)  # num decisiones tomadas
            if i < len(w):
                # Un hijo por contenedor existente en el que quepa
                for nc in range(len(self.extra.pesos_contenedores)):
                    if self.extra.pesos_contenedores[nc] + w[i] <= C:
                        pesos_contenedores2 = self.extra.pesos_contenedores[:]
                        pesos_contenedores2[nc] += w[i]
                        yield self.add_decision(nc, Extra(pesos_contenedores2))
                # Un hijo en un contenedor nuevo
                pesos_contenedores2 = self.extra.pesos_contenedores[:]
                pesos_contenedores2.append(w[i])
                yield self.add_decision(len(self.extra.pesos_contenedores), Extra(pesos_contenedores2))

        def solution(self) -> list[int]:
            return list(self.decisions())

    initial_ds = BinpackingBDS(Extra([0]))
    return bab_min_solve(initial_ds)


def process_old(C: int, w: list[int]) -> list[int]:
    vect_pos = [-1] * len(w)  # crea un vector lleno de -1 de long len(w)
    pesos_contenedores: list[int] = [0]

    for i in range(len(w)):
        # recorrer pesos_contenedores
        # bucle modificable por un for: ... else: ... -> solo se ejecuta si no se realiza un break en el for
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
    for value in l:
        print(value)


if __name__ == '__main__':
    c, ls = read_data(sys.stdin)
    f_ls = process(c, ls)
    show_results(f_ls)
