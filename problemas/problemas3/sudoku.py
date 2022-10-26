from __future__ import annotations

import sys
from dataclasses import dataclass
from typing import TextIO
from algoritmia.schemes.bt_scheme import DecisionSequence, bt_solve

from sudoku_lib import *


# Position = tuple[int, int] # (row, col)
# Sudoku = list[list[int]]


def read_data(f: TextIO) -> Sudoku:
    return desde_cadenas(f.readlines())


def process_fast(s: Sudoku) -> Iterator[Sudoku]:
    @dataclass
    class Extra:
        sudoku: Sudoku
        vacias: set[Position]

    class SudokuDS(DecisionSequence):
        def is_solution(self) -> bool:
            return len(self.extra.vacias) == 0

        def successors(self) -> Iterator[SudokuDS]:

            # pos = primera_vacia(self.extra.sudoku)
            best_posibles = None
            pos = (-1, -1)
            for pos_v in self.extra.vacias:
                aux = posibles_en(self.extra.sudoku, pos_v)
                if best_posibles is None or len(aux) < len(best_posibles):
                    best_posibles = aux
                    pos = pos_v

            if pos is not None:
                r, c = pos
                for num in posibles_en(self.extra.sudoku, pos):
                    # solucion extra: from copy import deepcopy -> sudoku2 = deepcopy(self.extra.sudoku) # bastante lento
                    sudoku2 = [linea[:] for linea in self.extra.sudoku]  # ayuda -> ej copiar lista: m2 = m[:]
                    sudoku2[r][c] = num
                    vacias2 = set(self.extra.vacias)
                    vacias2.remove(pos)
                    yield self.add_decision(num, Extra(sudoku2, vacias2))

        def solution(self) -> Sudoku:
            return self.extra.sudoku

    initial_ds = SudokuDS(Extra(sudoku, set(vacias(sudoku))))
    return bt_solve(initial_ds)


def process_naiv(s: Sudoku) -> Iterator[Sudoku]:
    @dataclass
    class Extra:
        sudoku: Sudoku

    class SudokuDS(DecisionSequence):
        def is_solution(self) -> bool:
            return primera_vacia(self.extra.sudoku) is None

        def successors(self) -> Iterator[SudokuDS]:
            pos = primera_vacia(self.extra.sudoku)
            if pos is not None:
                r, c = pos
                for num in posibles_en(self.extra.sudoku, pos):
                    # solucion extra: from copy import deepcopy -> sudoku2 = deepcopy(self.extra.sudoku) # bastante lento
                    sudoku2 = [linea[:] for linea in self.extra.sudoku]  # ayuda -> ej copiar lista: m2 = m[:]
                    sudoku2[r][c] = num
                    yield self.add_decision(num, Extra(sudoku2))

        def solution(self) -> Sudoku:
            return self.extra.sudoku

    initial_ds = SudokuDS(Extra(sudoku))
    return bt_solve(initial_ds)


def show_results(sudokus: Iterator[Sudoku]):
    for s in sudokus:
        pretty_print(s)


process = process_fast
if __name__ == '__main__':
    sudoku = read_data(sys.stdin)
    sudokusS = process(sudoku)
    show_results(sudokusS)
