#!/usr/bin/env python3

# Pillow is used to read the image, not cv2:
# cv2 is heavy and reads in BGR order instead of RGB.
import sys

import numpy as np
from PIL import Image


def check_path(path: str) -> None:
    """
    raise an error if path is not a valid jpg/jpeg file path
    """
    if not isinstance(path, str):
        raise TypeError("path must be a str")
    if not path:
        raise ValueError("path is empty")
    if not path.lower().endswith((".jpg", ".jpeg")):
        raise ValueError("only JPG and JPEG formats are supported")


def ft_load(path: str) -> np.ndarray:
    """
    load a jpg/jpeg image, print its shape
    and return its pixels as an RGB numpy array (height, width, 3).
    """
    check_path(path)

    try:
        with Image.open(path) as img:
            rgb_data = np.array(img.convert("RGB"))
    except FileNotFoundError as e:
        raise FileNotFoundError(f"file not found: {path}") from e
    except OSError as e:
        raise ValueError(f"cannot read image: {path}") from e

    print(f"The shape of image is: {rgb_data.shape}")
    return rgb_data


def main() -> None:
    """
    test ft_load
    """
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
