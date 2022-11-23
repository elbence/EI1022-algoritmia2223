from __future__ import annotations

import sys
from collections.abc import Iterator
from dataclasses import dataclass
from typing import TextIO
from algoritmia.schemes.bt_scheme import ScoredDecisionSequence, bt_max_solve

Weight = int
Value = int
Decision = int  # 0 or 1
Decisions = tuple[Decision, ...]


def read_data(f: TextIO) -> tuple[Weight, list[Value], list[Weight]]:
    capacity = int(f.readline())
    values: list[Value] = []
    weights: list[Weight] = []
    for linea in f:
        v_txt, w_txt = linea.strip().split()  # primero quita blancos de los extremos y luego separa
        values.append(int(v_txt))
        weights.append(int(w_txt))
    return capacity, values, weights


def process(capacity: Weight, values: list[Value], weights: list[Weight]) -> tuple[Value, Weight, Decisions]:

    @dataclass
    class Extra:
        current_weight: Weight
        current_value: Value

    class KnapsackDS(ScoredDecisionSequence):
        # DecisionSequence
        def is_solution(self) -> bool:
            return len(self) == len(values)

        def successors(self) -> Iterator[KnapsackDS]:
            n = len(self)
            if n < len(values):
                if weights[n] + self.extra.current_weight <= capacity:
                    current_weight2 = self.extra.current_weight + weights[n]
                    current_value2 = self.extra.current_value + values[n]
                    yield self.add_decision(1, Extra(current_weight2, current_value2))  # se podia añadir nuevo peso, se añade
                # Se añade hijo sin peso despues para encontrar hijos mas pesados primer,
                # con esto el posterior recorredor deberia saltar el maximo de hijos posibles
                yield self.add_decision(0, self.extra)  # misma mochila sin añadir este obj

        def solution(self) -> tuple[Value, Weight, Decisions]:
            return self.extra.current_value, self.extra.current_weight, self.decisions()

        # StateDecisionSequence
        def state(self) -> tuple[int, int]:
            return len(self), self.extra.current_weight

        # ScoredDecisionSequence
        def score(self) -> int:
            return self.extra.current_value

    initial_ds = KnapsackDS(Extra(0, 0))
    best_sol = list(bt_max_solve(initial_ds))[-1]
    return best_sol


def show_results(total_value: Value, total_weight: Weight, decisions: Decisions):
    print(total_value)
    print(total_weight)
    # print('\n'.join(str(d) for d in decisions))
    for d in decisions:
        print(d)


if __name__ == '__main__':
    capacity0, values0, weights0 = read_data(sys.stdin)
    total_value0, total_weight0, decisions0 = process(capacity0, values0, weights0)
    show_results(total_value0, total_weight0, decisions0)
