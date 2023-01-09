from algoritmia.utils import infinity

Score = int


def process(P: list[int], B: list[int], M: list[int], C: int):
    def S(c: int, n: int) -> Score:
        print(f"{c} - {n}")

        if n == 0 and c == 0:  # Caso base
            return 0
        if n == 0 and c < 0:
            return -infinity
        if n == 0 and c > 0:  # Caso base
            return -infinity

        if n > 0 and c > 0:  # n es decisiones , que es una solucion? 0 1 2 neveras
            res = []
            for d in range(M[n] + 1):  # M[n] haces un for de la lista + 1 por culpa del range
                c_prev, n_prev = c - d * P[n - 1], n - 1
                res.append(S(c_prev, n_prev) + d * B[n])
            return max(res)  # devuelves el maximo

    return S(C, len(M))


if __name__ == "__main__":
    B0 = [900, 550, 500]
    P0 = [1000, 600, 850]
    M0 = [2, 2, 5]
    C = 4000

    res = process(P0, B0, M0, C)
    print(res)
