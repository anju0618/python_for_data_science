#!/usr/bin/env python3

import sys


def counter(s: str) -> dict[str, int]:
    """Count upper, lower, punctuation, space and digit characters."""

    res = {
        "upp": 0,
        "low": 0,
        "pun": 0,
        "spc": 0,
        "dig": 0,
    }

    for c in s:
        if c.isupper():
            res["upp"] += 1
        elif c.islower():
            res["low"] += 1
        elif c.isspace():
            res["spc"] += 1
        elif c.isdigit():
            res["dig"] += 1
        elif not c.isalnum():
            res["pun"] += 1

    return res


def put_ans() -> None:
    """Count the characters of the argument or of stdin and print them."""

    argv = sys.argv[1:]

    if len(argv) == 0:
        print("What is the text to count?")
        s = sys.stdin.readline()
        if not s:
            return
        res = counter(s)

    elif len(argv) == 1:
        s = argv[0]
        res = counter(s)

    elif len(argv) > 1:
        raise AssertionError("More than one argument is provided")

    print(f"The text contains {len(s)} characters:")
    print(f"{res['upp']} upper letters")
    print(f"{res['low']} lower letters")
    print(f"{res['pun']} punctuation marks")
    print(f"{res['spc']} spaces")
    print(f"{res['dig']} digits")


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
