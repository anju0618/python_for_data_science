#!/usr/bin/env python3
import sys


NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def encode(text: str) -> str:
    """Return the Morse code of text, or raise AssertionError."""
    text = text.upper()
    assert all(c in NESTED_MORSE for c in text), "the arguments are bad"
    return " ".join(NESTED_MORSE[c] for c in text)


def main() -> None:
    """Print the Morse code of the argument."""
    try:
        argv = sys.argv[1:]
        assert len(argv) == 1, "the arguments are bad"
        print(encode(argv[0]))
    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
