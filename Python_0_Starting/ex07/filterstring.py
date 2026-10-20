#!/usr/bin/env python3

import sys


def filter_words(text: str, length: int) -> list[str]:
    """Return the words of text longer than length."""
    return [w for w in text.split() if (lambda x: len(x) > length)(w)]


def main() -> None:
    """Print the words of S longer than N."""
    try:
        argv = sys.argv[1:]
        assert len(argv) == 2, "the arguments are bad"
        try:
            length = int(argv[1])
        except ValueError:
            raise AssertionError("the arguments are bad")
        print(filter_words(argv[0], length))
    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
