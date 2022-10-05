import sys
from typing import TextIO


def read_data(f: TextIO) -> list[int]:
    # En l tenemos una cadena por línea:
    lines: list[str] = f.readlines()
    # Transformamos cada línea en un entero:
    return [int(line) for line in lines]


def process(nums: list[int]) -> int:
    m = nums[0]
    for num in nums:
        if num < m:
            m = num
    return m


def show_results(m: int):
    # Recorremos las listas con el bucle for
    print(m)


if __name__ == '__main__':
    nums = read_data(sys.stdin)
    m = process(nums)
    show_results(m)
