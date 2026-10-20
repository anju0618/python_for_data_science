#!/usr/bin/env python3

import sys


def is_even(num: int) -> bool:
    """Return True if num is even."""

    if num % 2 == 0:
        return True
    else:
        return False


def put_ans() -> None:
    """Print whether the argument is even or odd."""
    argv = sys.argv[1:]
    if len(argv) == 0:
        return
    assert len(argv) == 1, "more than one argument is provided"
    try:
        num = int(argv[0])
    except ValueError:
        assert False, "argument is not an integer"

    if is_even(num):
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main() -> None:
    """Run put_ans and report errors."""
    try:
        put_ans()
    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
