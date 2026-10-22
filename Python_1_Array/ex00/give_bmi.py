#!/usr/bin/env python3

import sys


def check_numbers(values: list, name: str) -> None:
    """
    raise an error if values is not a list of int or float
    """
    if not isinstance(values, list):
        raise TypeError(f"{name} must be a list")
    for v in values:
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            raise TypeError(f"{name} must contain only int or float")


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    bmi = weight / (height)^2
    return bmi list(int or float)
    """
    check_numbers(height, "height")
    check_numbers(weight, "weight")
    if len(height) != len(weight):
        raise ValueError("length of height and weight is not match.")
    for h in height:
        if h <= 0:
            raise ValueError("height must be positive")

    res = []
    for h, w in zip(height, weight):
        res.append(w / h ** 2)

    return res


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    return True if bmi is above limit else return False
    """
    check_numbers(bmi, "bmi")
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("limit must be an int")

    res = []
    for b in bmi:
        res.append(b > limit)

    return res


def main() -> None:
    """
    test give_bmi and apply_limit
    """
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
