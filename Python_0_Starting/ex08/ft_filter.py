#!/usr/bin/env python3

import sys


def ft_filter(function, iterable):
    """\
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    for item in iterable:
        if (item if function is None else function(item)):
            yield item


def main() -> None:
    """Show ft_filter on the even numbers of range(10)."""
    print(list(ft_filter(lambda x: x % 2 == 0, range(10))))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
