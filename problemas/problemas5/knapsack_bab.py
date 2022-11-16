from __future__ import annotations

import sys
from collections.abc import Iterator
from dataclasses import dataclass
from typing import TextIO
from algoritmia.schemes.bab_scheme import BoundedDecisionSequence, bab_max_solve

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

    class KnapsackBDS(BoundedDecisionSequence):
        def calculate_opt_bound(self) -> Value:
            # return self.extra.current_value + sum(values[len(self):])
            w = self.extra.current_weight
            v = self.extra.current_value
            for i in range(len(self), len(values)):
                if w + weights[i] <= capacity:
                    w += weights[i]
                    v += values[i]
                else:
                    trozo = (capacity - w) / weights[i]
                    w += weights[i] * trozo
                    v += values[i] * trozo
                    break
            return v

        def calculate_pes_bound(self) -> Value:
            # return self.extra.current_value + 0
            w = self.extra.current_weight
            v = self.extra.current_value
            for i in range(len(self), len(values)):
                if w + weights[i] <= capacity:
                    w += weights[i]
                    v += values[i]
            return v

        def is_solution(self) -> bool:
            return len(self) == len(values)

        def successors(self) -> Iterator[KnapsackBDS]:
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

    initial_ds = KnapsackBDS(Extra(0, 0))
    return bab_max_solve(initial_ds)


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
