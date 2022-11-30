from typing import *
import sys


Solution = tuple[int, int, int]
# 0 suma, 1 begin, 2 end


def read_data(f: TextIO) -> list[int]:
    return [int(line) for line in f]


def process_tail(v: list[int]) -> Solution:
    def div_solve(start: int, end: int) -> Solution:
        # if problem.is_simple():
        #     return problem.trivial_solution
        # else:
        #     subproblemas = problem.divide()
        #     solutions = recursividad(...) for p in subproblemas
        #     return problem.combine(solutions)
        if end - start == 1:                    # is simple
            return v[start], start, start + 1   # trivial sol
        # divide
        h = (start + end) // 2
        # recursividad
        best_left = div_solve(start, h)
        best_right = div_solve(h, end)

        acumulado_l = 0
        i_max_l = h
        v_max_l = v[h]
        for i in range(h - 1, start - 1, - 1):
            acumulado_l = acumulado_l + v[i]
            if acumulado_l > v_max_l:
                i_max_l = i
                v_max_l = acumulado_l

        acumulado_r = 0
        i_max_r = h
        v_max_r = v[h]
        for i in range(h + 1, end):
            acumulado_r = acumulado_r + v[i]
            if acumulado_r > v_max_r:
                i_max_r = i
                v_max_r = acumulado_r

        best_center = (v_max_l + v_max_r - v[h], i_max_l, i_max_r)
        # combine & return
        return max(best_left, best_right, best_center)

    return div_solve(0, len(v))


def show_results(sol: Solution):
    print(sol[0])
    print(sol[1])
    print(sol[2])


# Cambia el comment en las siguientes lineas para alternar el tipo de process a utilizar
process = process_tail
# process = process_iter
if __name__ == '__main__':
    v0 = read_data(sys.stdin)
    solution0 = process(v0)
    show_results(solution0)
