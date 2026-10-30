#!/usr/bin/env python3

import sys
from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for a character with a name and a health state."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Set the first name and the health state (alive by default)."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:
        """Switch is_alive from True to False."""
        if self.is_alive:
            self.is_alive = False
        else:
            print(f"{self.first_name} is already die.")

    @abstractmethod
    def get_gender(self) -> None:
        """Print the gender of the character."""
        pass


class Stark(Character):
    """Concrete character of the Stark family (male)."""

    def get_gender(self) -> None:
        """Print the gender of the character."""
        print(f"{self.first_name} is Male.")


class Fern(Character):
    """Concrete character Fern (female)."""

    def get_gender(self) -> None:
        """Print the gender of the character."""
        print(f"{self.first_name} is Female")


def main() -> None:
    """Show Stark and Fern, and check that Character is abstract."""
    ned = Stark("Ned")
    print(ned.__dict__)
    ned.get_gender()
    ned.die()
    print(ned.is_alive)
    ned.die()
    print("---")
    fern = Fern("Fern", False)
    print(fern.__dict__)
    fern.get_gender()
    print("---")
    try:
        Character("hodor")  # type: ignore[abstract]
    except TypeError as e:
        print(f"TypeError: {e}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
