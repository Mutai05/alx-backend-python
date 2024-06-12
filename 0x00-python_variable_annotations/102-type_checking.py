#!/usr/bin/env python3
"""
Module for zooming an array by a given factor.
"""
from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zoom in on the elements of the tuple by the given factor.

    Args:
        lst (Tuple[int, ...]): The tuple to be zoomed.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        List[int]: A list with elements repeated by the zoom factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple[int, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
