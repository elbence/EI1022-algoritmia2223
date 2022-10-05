import sys
from typing import TextIO


def read_data(f: TextIO) -> list[int]:
    # En l tenemos una cadena por línea:
    lines: list[str] = f.readlines()
    # Transformamos cada línea en un entero:
    return [int(line) for line in lines]


def process(data: list[int]) -> bool:
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] == data[j]:
                return True
    return False


def show_result(result: bool):
    print("No hay repetidos" if not result else "Hay repetidos")


if __name__ == '__main__':
    nums = read_data(sys.stdin)
    result = process(nums)
    show_result(result)
