#!/usr/bin/env python3

import sys

from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Set the family name, the eyes and the hairs of the Baratheon."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def get_gender(self) -> None:
        """Print the gender of the character."""
        print(f"{self.first_name} is Male.")

    def __str__(self) -> str:
        """Return the family name, the eyes and the hairs as a string."""
        return self.__repr__()

    def __repr__(self) -> str:
        """Return the family name, the eyes and the hairs as a string."""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Set the family name, the eyes and the hairs of the Lannister."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def get_gender(self) -> None:
        """Print the gender of the character."""
        print(f"{self.first_name} is Female.")

    def __str__(self) -> str:
        """Return the family name, the eyes and the hairs as a string."""
        return self.__repr__()

    def __repr__(self) -> str:
        """Return the family name, the eyes and the hairs as a string."""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    @classmethod
    def create_lannister(cls, first_name: str,
                         is_alive: bool = True) -> "Lannister":
        """Create a Lannister from a first name and a health state."""
        return cls(first_name, is_alive)


def main() -> None:
    """Show the Baratheon and Lannister families."""
    robert = Baratheon("Robert")
    print(robert.__dict__)
    print(robert.__str__)
    print(robert.__repr__)
    print(robert.is_alive)
    robert.die()
    print(robert.is_alive)
    print(robert.__doc__)
    print("---")
    cersei = Lannister("Cersei")
    print(cersei.__dict__)
    print(cersei.__str__)
    print(cersei.is_alive)
    print("---")
    jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {jaine.first_name, type(jaine).__name__}, "
          f"Alive : {jaine.is_alive}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
