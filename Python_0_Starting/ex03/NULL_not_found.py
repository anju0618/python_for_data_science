#!/usr/bin/env python3

from typing import Any


def NULL_not_found(object: Any) -> int:
    """Print the label, value and type of a null-like value.

    Return 0 if the value is recognised, 1 otherwise.
    """
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, bool) and not object:
        print(f"Fake: {object} {type(object)}")
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object} {type(object)}")
    elif isinstance(object, int) and not isinstance(object, bool) \
            and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, str) and object == "":
        print(f"Empty: {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0
