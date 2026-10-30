#!/usr/bin/env python3

import sys

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Joffrey Baratheon, a king that is both a Baratheon and a Lannister."""

    @property
    def eyes_color(self) -> str:
        """Eyes color of the king."""
        return self.eyes

    @eyes_color.setter
    def eyes_color(self, color: str) -> None:
        """Change the eyes color of the king."""
        self.eyes = color

    @property
    def hairs_color(self) -> str:
        """Hairs color of the king."""
        return self.hairs

    @hairs_color.setter
    def hairs_color(self, color: str) -> None:
        """Change the hairs color of the king."""
        self.hairs = color

    def set_eyes(self, color: str) -> None:
        """Set the eyes color of the king."""
        self.eyes_color = color

    def get_eyes(self) -> str:
        """Return the eyes color of the king."""
        return self.eyes_color

    def set_hairs(self, color: str) -> None:
        """Set the hairs color of the king."""
        self.hairs_color = color

    def get_hairs(self) -> str:
        """Return the hairs color of the king."""
        return self.hairs_color


def main() -> None:
    """Show that the properties of the king can be changed."""
    joffrey = King("Joffrey")
    print(joffrey.__dict__)
    joffrey.set_eyes("blue")
    joffrey.set_hairs("light")
    print(joffrey.get_eyes())
    print(joffrey.get_hairs())
    print(joffrey.__dict__)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
