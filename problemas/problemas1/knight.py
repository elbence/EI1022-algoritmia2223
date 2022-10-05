import sys
from typing import TextIO

from algoritmia.datastructures.graphs import UndirectedGraph
from algoritmia.algorithms.traversers import bf_vertex_traverser

Vertex = tuple[int, int]
Edge = tuple[Vertex, Vertex]
Path = list[Vertex]


def knight_graph(rows: int, cols: int) -> UndirectedGraph:
    vertices: list[Vertex] = []
    for r in range(rows):
        for c in range(cols):
            vertices.append((r, c))

    edges: list[Edge] = []

    # FOLLOWING DRY:
    # Instead of 4 if comparison iterate all the occurences
    for r, c in vertices:
        for ir, ic in [(1, -2), (2, -1), (2, 1), (1, 2)]:
            r2 = r+ir
            c2 = c+ic
            if rows > r2 >= 0 and cols > c2 >= 0:
                edges.append(((r, c), (r2, c2)))

    return UndirectedGraph(E=edges)


def read_data(f: TextIO) -> tuple[int, int, int, int]:
    rows = int(f.readline())
    cols = int(f.readline())
    first_row = int(f.readline())
    first_col = int(f.readline())
    return rows, cols, first_row, first_col


def process(rows: int,
            cols: int,
            first_row: int,
            first_col: int) -> tuple[UndirectedGraph[Vertex], int]:
    g: UndirectedGraph[Vertex] = knight_graph(rows, cols)
    vertices = list(bf_vertex_traverser(g, (first_row, first_col)))
    return g, len(vertices)


def show_results(num: int):
    print(num)


if __name__ == '__main__':
    rows0, cols0, first_row0, first_col0 = read_data(sys.stdin)
    grap0, num0 = process(rows0, cols0, first_row0, first_col0)
    show_results(num0)
