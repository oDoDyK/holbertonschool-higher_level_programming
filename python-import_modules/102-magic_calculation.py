#!/usr/bin/python3
from magic_calculation_102 import add, sub

if __name__ == "__main__":
    a = 10
    b = 5
    c = 2

    result = add(add(a, b), sub(a, c))
    print(result)
