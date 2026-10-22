#!/usr/bin/env python3

import sys

import matplotlib.pyplot as plt
import numpy as np

from load_image import ft_load


def zoom(array: np.ndarray) -> None:
    """
    cut a square (at most 400x400) out of the center of the image,
    keep a single color channel, print its shape and pixels,
    then display it with the x and y scale.
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
    zoomed = array[top: top + size, left: left + size, 0: 1]

    print(f"New shape after slicing: {zoomed.shape}")
    print(zoomed)

    plt.imshow(zoomed[:, :, 0], cmap="gray")
    plt.xlabel("x (pixel)")
    plt.ylabel("y (pixel)")
    plt.show()


def main() -> None:
    """
    load animal.jpeg and zoom on it
    """
    pic = ft_load("animal.jpeg")
    print(pic)
    zoom(pic)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
