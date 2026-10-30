#!/usr/bin/env python3

import sys
from typing import Callable


def square(x: int | float) -> int | float:
    """Return the square of the argument."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return the exponentiation of the argument by itself."""
    return x ** x


def outer(x: int | float,
          function: Callable[[int | float], int | float]
          ) -> Callable[[], int | float]:
    """Return a function that applies the function to the previous result,
    starting from x, each time it is called."""
    def inner() -> int | float:
        """Apply the function to the previous result and return it."""
        nonlocal x
        x = function(x)
        return x

    return inner


def main() -> None:
    """Test outer with square and pow."""
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
