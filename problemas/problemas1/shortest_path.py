import sys
from typing import TextIO
from algoritmia.datastructures.graphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo

from labyrinth import create_labyrinth

Vertex = tuple[int, int]
Edge = tuple[Vertex, Vertex]
Path = list[Vertex]


def bf_search(g: UndirectedGraph[Vertex],
              source: Vertex,
              target: Vertex) -> list[Edge]:
    res: list = []
    queue: Fifo = Fifo()
    seen = set()
    queue.push((source, source))  # arista fantasma inicial
    seen.add(source)
    while len(queue) > 0:
        u, v = queue.pop()
        res.append((u, v))
        if v == target:
            return res
        for suc in g.succs(v):
            if suc not in seen:
                queue.push((v, suc))
                seen.add(suc)
    return res  # lista rellenada pero target no encontrado
    # return []  # lista vacia si no encontrado target


def path_recover(edges: list[Edge],
                 target: Vertex) -> list[Vertex]:
    bp = {}
    for e in edges:
        u, v = e
        bp[v] = u

    path = [target]
    while v != bp[v]:
        v = bp[v]
        path.append(v)

    path.reverse()
    return path


def read_data(f: TextIO) -> tuple[int, int]:
    rows = int(f.readline())
    cols = int(f.readline())
    return rows, cols


def process(rows: int, cols: int) -> tuple[UndirectedGraph[Vertex], Path]:
    g: UndirectedGraph = create_labyrinth(rows, cols)
    edges = bf_search(g, (0, 0), (rows - 1, cols - 1))
    path = path_recover(edges, (rows - 1, cols - 1))
    return g, path


def show_results(path: Path):
    for v in path:
        print(v)


if __name__ == '__main__':
    rows0, cols0 = read_data(sys.stdin)
    graph0, path0 = process(rows0, cols0)
    show_results(path0)
