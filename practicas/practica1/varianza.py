import sys
from typing import TextIO


def read_data(f: TextIO) -> list[int]:
    # En l tenemos una cadena por línea:
    lines: list[str] = f.readlines()
    # Transformamos cada línea en un entero:
    return [int(line) for line in lines]


def average(nums: list[int]) -> float:
    return sum(nums)/len(nums) # Theta(n)


def process(nums: list[int]) -> float:
    s = 0
    avg = average(nums)
    for num in nums:
        s += (num - avg) ** 2 # n veces, Theta(1) >= Theta(n)
    return s/len(nums)


def show_results(v: int):
    # Recorremos las listas con el bucle for
    print(v)


if __name__ == '__main__':
    nums = read_data(sys.stdin)
    v = process(nums)
    show_results(v)
