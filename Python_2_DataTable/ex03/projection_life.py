#!/usr/bin/env python3

from load_csv import load
import sys
import matplotlib.pyplot as plt
import pandas as pd


class LoadError(Exception):
    pass


def main() -> None:
    """
    main function
    """

    income_df = load("income_per_person_gdppercapita"
                     "_ppp_inflation_adjusted.csv")
    expectancy_df = load("life_expectancy_years.csv")

    if income_df is None or expectancy_df is None:
        raise LoadError("Loading missed")

    gdp = income_df.set_index("country")["1900"]
    life = expectancy_df.set_index("country")["1900"]

    df = pd.concat([gdp, life], axis=1, keys=["gdp", "life"])
    df = df.dropna()

    corr = df["gdp"].corr(df["life"])
    print(f"Correlation: {corr:.2f}")

    plt.scatter(df["gdp"], df["life"], label="1900")
    plt.xscale('log')
    plt.title("Life Expectancy vs GDP per capita (1900)")
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life Expectancy")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
