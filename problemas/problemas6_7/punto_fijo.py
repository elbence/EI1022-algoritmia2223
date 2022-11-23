from typing import *
import sys


def read_data(f: TextIO) -> list[int]:
    return [int(line) for line in f]


def process_tail(v: list[int]) -> Optional[int]:
    def tail_def_solve(start: int, end: int) -> Optional[int]:
        # if problem.is_simple():
        #     return problem.trivial_solution
        # else:
        #     smaller_problem = problem.decrease()
        #     return tail_def_solve(smaller_problem)

        if end - start == 1:
            return start if v[start] == start else None
        else:
            # decrease
            mid: int = (start + end) // 2
            if v[mid] == mid:
                return mid
            elif v[mid] < mid:
                start = mid
            else:
                end = mid

            return tail_def_solve(start, end)

    return tail_def_solve(0, len(v))


def process_iter(v: list[int]) -> Optional[int]:
    def iter_def_solve(start: int, end: int) -> Optional[int]:
        #     while not problem.is_simple():
        #         problem = problem.decrease()
        #     return problem.trivial_solution()

        while not (end - start) == 1:
            mid: int = (start + end) // 2
            if v[mid] == mid:
                return mid
            elif v[mid] < mid:
                start = mid
            else:
                end = mid
        return start if v[start] == start else None

    return iter_def_solve(0, len(v))


def show_results(pos_pico: Optional[int]):
    print("No hay punto fijo") if pos_pico is None else print(pos_pico)


# Cambia el comment en las siguientes lineas para alternar el tipo de process a utilizar
process = process_tail
# process = process_iter
if __name__ == '__main__':
    v0 = read_data(sys.stdin)
    pos_pico0 = process(v0)
    show_results(pos_pico0)
