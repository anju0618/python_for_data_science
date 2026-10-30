#!/usr/bin/env python3

import sys
from typing import Any


def get_numbers(args: tuple[Any, ...]) -> list[float]:
    """Return the arguments as a sorted list, raise if they are not numbers."""
    if not args:
        raise ValueError("no number given")
    for a in args:
        if isinstance(a, bool) or not isinstance(a, (int, float)):
            raise TypeError("only int or float are allowed")
    return sorted(args)


def get_mean(numbers: list[float]) -> float:
    """Return the mean of a list of numbers."""
    return sum(numbers) / len(numbers)


def get_median(numbers: list[float]) -> float:
    """Return the median of a sorted list of numbers."""
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    return (numbers[n // 2 - 1] + numbers[n // 2]) / 2


def get_percentile(numbers: list[float], percent: float) -> float:
    """Return a percentile of a sorted list (linear interpolation)."""
    pos = (len(numbers) - 1) * percent / 100
    low = int(pos)
    high = min(low + 1, len(numbers) - 1)
    return float(numbers[low] + (numbers[high] - numbers[low]) * (pos - low))


def get_variance(numbers: list[float]) -> float:
    """Return the variance of a list of numbers."""
    mean = get_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)


def get_std(numbers: list[float]) -> float:
    """Return the standard deviation of a list of numbers."""
    return get_variance(numbers) ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Print the statistics (mean, median, quartile, std, var) asked in
    kwargs values about the numbers given in args."""
    try:
        numbers: list[float] | None = get_numbers(args)
    except (TypeError, ValueError):
        numbers = None
    functions = {
        "mean": get_mean,
        "median": get_median,
        "quartile": lambda n: [get_percentile(n, 25), get_percentile(n, 75)],
        "std": get_std,
        "var": get_variance,
    }
    for name in kwargs.values():
        if name not in functions:
            continue
        if numbers is None:
            print("ERROR")
        else:
            print(f"{name} : {functions[name](numbers)}")


def main() -> None:
    """Test ft_statistics."""
    ft_statistics(1, 42, 360, 11, 64,
                  toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
