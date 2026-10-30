#!/usr/bin/env python3

import sys
from typing import Any, Callable


def callLimit(limit: int) -> Callable[[Callable[..., Any]],
                                      Callable[..., Any]]:
    """Return a decorator that blocks the calls of a function above limit."""
    count = 0

    def callLimiter(function: Callable[..., Any]) -> Callable[..., Any]:
        """Decorate the function with the call limit."""
        def limit_function(*args: Any, **kwds: Any) -> Any:
            """Call the function, or print an error above the limit."""
            nonlocal count
            if count >= limit:
                print(f"Error: {function} called too many times")
                return None
            count += 1
            return function(*args, **kwds)

        return limit_function

    return callLimiter


def main() -> None:
    """Test callLimit."""
    @callLimit(3)
    def f() -> None:
        """Print f()."""
        print("f()")

    @callLimit(1)
    def g() -> None:
        """Print g()."""
        print("g()")

    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
