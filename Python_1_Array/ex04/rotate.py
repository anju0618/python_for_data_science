#!/usr/bin/env python3

import sys

import matplotlib.pyplot as plt
import numpy as np

from load_image import ft_load


def cut_square(array: np.ndarray) -> np.ndarray:
    """
    cut a square (at most 400x400) out of the center of the image
    and keep a single color channel.
    return an array of shape (size, size, 1).
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("array must be a numpy array")
    if array.ndim != 3:
        raise ValueError("array must be 3 dimensional (height, width, color)")

    h, w = array.shape[:2]
    if h == 0 or w == 0:
        raise ValueError("image is empty")
    size = min(400, h, w)

    top = (h - size) // 2
    left = (w - size) // 2
    return array[top: top + size, left: left + size, 0: 1]


def transpose(array: np.ndarray) -> np.ndarray:
    """
    transpose a 2D array by hand: result[j][i] = array[i][j].
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("array must be a numpy array")
    if array.ndim != 2:
        raise ValueError("array must be 2 dimensional")

    rows, cols = array.shape
    result = np.empty((cols, rows), dtype=array.dtype)
    for i in range(rows):
        for j in range(cols):
            result[j, i] = array[i, j]
    return result


def main() -> None:
    """
    load animal.jpeg, cut a square, transpose it and display it
    """
    pic = ft_load("animal.jpeg")
    square = cut_square(pic)
    print(f"The shape of image is: {square.shape}")
    print(square)

    rotated = transpose(square[:, :, 0])
    print(f"New shape after Transpose: {rotated.shape}")
    print(rotated)

    plt.imshow(rotated, cmap="gray")
    plt.xlabel("x (pixel)")
    plt.ylabel("y (pixel)")
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
