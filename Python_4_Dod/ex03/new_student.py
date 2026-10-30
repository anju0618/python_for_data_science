#!/usr/bin/env python3

import random
import string
import sys
from dataclasses import dataclass, field


def generate_id() -> str:
    """Return a random id of 15 lowercase letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A student with a name, a surname, a login and a random id."""

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self) -> None:
        """Create the login from the name and the surname."""
        self.login = self.name[0] + self.surname


def main() -> None:
    """Test Student, the login and the id can not be initialized."""
    student = Student(name="Edward", surname="agle")
    print(student)
    try:
        Student(name="Edward", surname="agle", id="toto")  # type: ignore
    except TypeError as e:
        print(f"TypeError: {e}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
