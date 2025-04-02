from enum import Enum


class RedBlackTreeColor(Enum):
    """Enum containing the colors of a red-black tree (red and black).
    """
    RED = "RED"
    BLACK = "BLACK"


def convert_color_enum_to_string(color: RedBlackTreeColor | str) -> str:
    """Converts RedBlackTreeColor to string for e.g., cleaner printing. If argument is already a string, it is not modified.
    """
    if isinstance(color, RedBlackTreeColor):
        return color.value
    else:
        return color
