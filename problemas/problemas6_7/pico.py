from typing import *
import sys


def read_data(f: TextIO) -> list[int]:
    return [int(line) for line in f]


def process_tail(v: list[int]) -> int:
    def tail_def_solve(start: int, end: int) -> int:
        # if problem.is_simple():
        #     return problem.trivial_solution
        # else:
        #     smaller_problem = problem.decrease()
        #     return tail_def_solve(smaller_problem)
        if end - start == 1:    # is simple
            return start        # trivial sol
        if end - start == 2:    # is simple
            return start if v[start] > v[start + 1] else start + 1  # trivial sol
        # decrease
        h = (start + end) // 2
        if v[h - 1] < v[h]:
            start = h
        else:
            end = h
        # recall
        return tail_def_solve(start, end)

    return tail_def_solve(0, len(v))


def show_results(pos_pico: int):
    print(pos_pico)


# Cambia el comment en las siguientes lineas para alternar el tipo de process a utilizar
process = process_tail
# process = process_iter
if __name__ == '__main__':
    v0 = read_data(sys.stdin)
    pos_pico0 = process(v0)
    show_results(pos_pico0)
