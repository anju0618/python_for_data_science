#!/usr/bin/env python3

"""
Color filters for an RGB image of shape (height, width, 3).

To keep only one color, the other two colors are set to 0.

ft_invert: 255 - every value, so dark becomes light (negative).
ft_red:    keep red. green and blue become 0 (assign 0).
ft_green:  keep green. red and blue become 0 (assign 0).
ft_blue:   keep blue. red and green become 0 (assign 0).
ft_grey:   mean of red, green and blue (divide by 3, then sum),
           copied on all 3 channels.
"""

import sys

import matplotlib.pyplot as plt
import numpy as np

from load_image import ft_load


def check_image(array: np.ndarray) -> None:
    """
    raise an error if array is not an RGB image (height, width, 3)
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("array must be a numpy array")
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("array must have the shape (height, width, 3)")


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    (operators used: =, -)
    """
    check_image(array)
    result = 255 - array
    show_image(result, "Invert")
    return result


def ft_red(array) -> np.ndarray:
    """
    Keeps only the red channel of the image received.
    (operator used: =)
    """
    check_image(array)
    result = array.copy()
    result[:, :, 1] = 0
    result[:, :, 2] = 0
    # version with "*" (multiply by [1, 0, 0]):
    # result = array * np.array([1, 0, 0], dtype=array.dtype)
    show_image(result, "Red")
    return result


def ft_green(array) -> np.ndarray:
    """
    Keeps only the green channel of the image received.
    (operator used: =)
    """
    check_image(array)
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 2] = 0
    # version with "-" (value - itself = 0):
    # result[:, :, 0] = result[:, :, 0] - array[:, :, 0]
    # result[:, :, 2] = result[:, :, 2] - array[:, :, 2]
    show_image(result, "Green")
    return result


def ft_blue(array) -> np.ndarray:
    """
    Keeps only the blue channel of the image received.
    (operator used: =)
    """
    check_image(array)
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    show_image(result, "Blue")
    return result


def ft_grey(array) -> np.ndarray:
    """
    Turns the image received into greyscale:
    every channel gets the mean of red, green and blue.
    (operators used: =, /)
    """
    check_image(array)
    grey = (array / 3).sum(axis=2)
    result = np.empty_like(array)
    result[:, :, :] = grey.astype(array.dtype)[:, :, np.newaxis]
    show_image(result, "Grey")
    return result


def show_image(image: np.ndarray, title: str) -> None:
    """
    display an image in a window with its title
    """
    plt.imshow(image)
    plt.title(title)
    plt.show()


def main() -> None:
    """
    load landscape.jpg, display it, then apply and display each filter
    """
    array = ft_load("landscape.jpg")
    print(array)

    show_image(array, "Original")
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
    print(ft_invert.__doc__)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
