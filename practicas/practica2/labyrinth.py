import random
import sys
from typing import TextIO

from algoritmia.datastructures.graphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet

Vertex = tuple[int, int]
Edge = tuple[Vertex, Vertex]


def read_data(f: TextIO) -> tuple[int, int]:
    rows = int(f.readline())
    cols = int(f.readline())
    return rows, cols


def process(rows: int, cols: int) -> UndirectedGraph:
    # print("Starting")

    # paso 1
    vertices: list[Vertex] = []
    for r in range(rows):
        for c in range(cols):
            vertices.append((r, c))

    # print(f'DEBUG: vertices {vertices}')

    # paso 2
    mfs = MergeFindSet()
    for vrt in vertices:
        mfs.add(vrt)

    # paso 3
    edges: list[Edge] = []
    for r, c in vertices:
        if r > 0:
            edges.append(((r, c), (r - 1, c)))
        if c > 0:
            edges.append(((r, c), (r, c - 1)))

    # print(f'DEBUG: edges {edges}')
    random.shuffle(edges)
    # print(f'DEBUG: edges {edges}')

    # paso 4
    corridors: list[Edge] = []

    # paso 5
    for v1, v2 in edges:
        if mfs.find(v1) != mfs.find(v2):
            mfs.merge(v1, v2)
            corridors.append((v1, v2))

    # paso 6
    return UndirectedGraph(E = corridors)


def show_results(labyrinth: UndirectedGraph):
    print(labyrinth)


if __name__ == "__main__":
    random.seed(42)
    rows, cols = read_data(sys.stdin)
    labyrinth = process(rows, cols)
    show_results(labyrinth)
