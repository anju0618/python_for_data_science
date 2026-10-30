#!/usr/bin/env python3

import sys


class calculator:
    """Calculate the dot product, the sum and the difference of 2 vectors."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Print the dot product of the 2 vectors."""
        print(f"Dot product is: {sum(a * b for a, b in zip(V1, V2))}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Print the sum of the 2 vectors."""
        print(f"Add Vector is : {[float(a + b) for a, b in zip(V1, V2)]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Print the difference of the 2 vectors."""
        print(f"Sous Vector is: {[float(a - b) for a, b in zip(V1, V2)]}")


def main() -> None:
    """Show the calculation of 2 vectors."""
    a: list[float] = [5, 10, 2]
    b: list[float] = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
