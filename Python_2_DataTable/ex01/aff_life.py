#!/usr/bin/env python3

from load_csv import load
import sys
import matplotlib.pyplot as plt


COUNTRY = [
    "Japan",
]


class LoadError(Exception):
    pass


def main() -> None:
    """
    main function
    """

    df = load("life_expectancy_years.csv")
    if df is None:
        raise LoadError("Loading missed")

    df = df[df['country'].isin(COUNTRY)]
    df = df.set_index("country").T

    df.index = df.index.astype(int)
    df.plot(
        title=f"{', '.join(COUNTRY)} Life expectancy Projections",
        xlabel="Year",
        ylabel="Life expectancy"
        )
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
