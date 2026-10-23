#!/usr/bin/env python3

from load_csv import load
import sys
import matplotlib.pyplot as plt


COUNTRY = [
    "Japan",
    "France"
]
SUFFIX = {
    "k": 1e3,
    "M": 1e6,
    "B": 1e9,
}


class LoadError(Exception):
    pass


def to_number(s: str) -> float:
    """
    change to float
    """
    if s[-1] in SUFFIX:
        res = float(s[:-1]) * SUFFIX[s[-1]]
    else:
        res = float(s)

    return res


def main() -> None:
    """
    main function
    """

    df = load("population_total.csv")
    if df is None:
        raise LoadError("Loading missed")

    df = df[df['country'].isin(COUNTRY)]
    df = df.set_index("country").T
    df = df.map(to_number)

    df.index = df.index.astype(int)
    df = df.loc[1800:2050]
    df.plot(
        title=f"{', '.join(COUNTRY)} Population Projections",
        xlabel="Year",
        ylabel="Population(milions)"
        )
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
