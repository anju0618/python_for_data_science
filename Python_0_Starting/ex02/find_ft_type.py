#!/usr/bin/env python3
from typing import Any


def all_thing_is_obj(object: Any) -> int:
    """Print the type of object and return 42."""
    if isinstance(object, list):
        print(f"List : {type(object)}")
        return 42

    elif isinstance(object, tuple):
        print(f"Tuple : {type(object)}")
        return 42

    elif isinstance(object, set):
        print(f"Set : {type(object)}")
        return 42

    elif isinstance(object, dict):
        print(f"Dict : {type(object)}")
        return 42

    elif isinstance(object, str):
        print(f"{object} is in the kitchen : {type(object)}")
        return 42

    else:
        print("Type not found")
        return 42
