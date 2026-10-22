#!/usr/bin/env python3

import sys


def slice_me(family: list, start: int, end: int) -> list:
    """
    print the shape of a 2D list, then the shape after slicing rows
    family[start:end].
    return the sliced 2D list (list of lists).
    """
    if not isinstance(family, list):
        raise TypeError("family must be list type.")
    if not family:
        raise ValueError("family is empty")
    for row in family:
        if not isinstance(row, list):
            raise TypeError("family must be a 2D list")
        if len(row) != len(family[0]):
            raise ValueError("all rows must have the same length")
    for n in (start, end):
        if isinstance(n, bool) or not isinstance(n, int):
            raise TypeError("start and end must be int")

    cols = len(family[0])
    print(f"My shape is : ({len(family)}, {cols})")
    sliced = family[start:end]
    print(f"My new shape is : ({len(sliced)}, {cols})")
    return sliced


def main() -> None:
    """
    test slice_me
    """
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


# numpy version
# import numpy as np


# def slice_me(family: list, start: int, end: int) -> list:
#     """
#     print the shape of a 2D list, then the shape after slicing rows
#     family[start:end].
#     return the sliced 2D list (list of lists).
#     """
#     if not isinstance(family, list):
#         raise TypeError("family must be list type.")
#     if not family:
#         raise ValueError("family is empty")
#     for n in (start, end):
#         if isinstance(n, bool) or not isinstance(n, int):
#             raise TypeError("start and end must be int")

#     array = np.array(family)
#     if array.ndim != 2:
#         raise ValueError("family must be a 2D list")

#     print(f"My shape is : {array.shape}")
#     sliced = array[start:end]
#     print(f"My new shape is : {sliced.shape}")
#     return sliced.tolist()
