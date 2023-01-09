from dataclasses import dataclass
from typing import Tuple, Optional

from algoritmia.schemes.bt_scheme import ScoredDecisionSequence, bt_max_solve

Solution = list[int, Tuple[int, ...]]


def process(P: list[int], B: list[int], M: list[int], C: int) -> Optional[Solution]:
    @dataclass
    class Extra:
        current_c: int
        current_b: int

    class TiendaPS(ScoredDecisionSequence):
        def is_solution(self) -> bool:
            return len(self) == len(B) and self.extra.current_c <= C

        def solution(self):
            return self.extra.current_b, self.decisions()

        def successors(self):
            n = len(self)  # Decisión en la que nos encontramos
            if n < len(B):
                for i in range(M[n] + 1):
                    current_c2 = self.extra.current_c + i * P[n]
                    if current_c2 <= C:
                        current_b2 = self.extra.current_b + i * B[n]
                        yield self.add_decision(i, Extra(current_c2, current_b2))

        def state(self):
            return len(self), self.extra.current_c

        def score(self):
            return self.extra.current_b

    initial_ps = TiendaPS(Extra(0, 0))
    res = list(bt_max_solve(initial_ps))
    if len(res) > 0:
        return res[-1]
    else:
        return None


if __name__ == "__main__":
    B0 = [900, 550, 500]
    P0 = [1000, 600, 850]
    M0 = [2, 2, 5]
    C = 4000

    res = process(P0, B0, M0, C)
    if res is None:
        print("No se ha encontrado una solución")
    else:
        beneficio, decisiones = res
        print(f"Resultado beneficio {beneficio} decisiones {decisiones}")