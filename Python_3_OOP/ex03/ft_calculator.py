#!/usr/bin/env python3

import sys


class calculator:
    """Calculate a vector with a scalar. The vector is updated in place."""

    def __init__(self, vector: list[float]) -> None:
        """Store the vector."""
        self.vector = vector

    def __add__(self, scalar: float) -> None:
        """Add the scalar to each element and print the vector."""
        self.vector = [v + scalar for v in self.vector]
        print(self.vector)

    def __mul__(self, scalar: float) -> None:
        """Multiply each element by the scalar and print the vector."""
        self.vector = [v * scalar for v in self.vector]
        print(self.vector)

    def __sub__(self, scalar: float) -> None:
        """Subtract the scalar from each element and print the vector."""
        self.vector = [v - scalar for v in self.vector]
        print(self.vector)

    def __truediv__(self, scalar: float) -> None:
        """Divide each element by the scalar and print the vector."""
        try:
            self.vector = [v / scalar for v in self.vector]
        except ZeroDivisionError:
            print("Error: division by zero")
            return
        print(self.vector)


def main() -> None:
    """Show the calculation of a vector with a scalar."""
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    v3 / 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
