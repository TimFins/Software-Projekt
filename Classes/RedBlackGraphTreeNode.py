from Classes.GraphTreeNode import GraphTreeNode
from Enums.RedBlackTreeColor import RedBlackTreeColor


class RedBlackGraphTreeNode(GraphTreeNode):
    def __init__(self, value, color=RedBlackTreeColor.RED, right_child=None, left_child=None):
        super().__init__(value, right_child, left_child)
        self.set_color(color)

    def get_color(self):
        return self._color

    def set_color(self, color):
        if isinstance(color, str):
            try:
                color = RedBlackTreeColor(color)
            except ValueError:
                raise ValueError(f"Invalid color '{color}'. Must be 'red' or 'black'.")

        if not isinstance(color, RedBlackTreeColor):
            raise TypeError("Color must be an instance of RedBlackTreeColor Enum.")

        self._color = color

    def __repr__(self):
        return f"RedBlackGraphTreeNode(value={self._value}, color={self._color})"

    @classmethod
    def _create_node_from_json(cls, data):
        if "color" not in data:
            raise ValueError("Invalid JSON format: RedBlackGraphTreeNode requires a 'color' key")

        return cls(data["value"], data["color"])

    def to_json(self):
        return {
            "value": self._value,
            "color": self._color.value,
            "left": self._left.to_json() if self._left else None,
            "right": self._right.to_json() if self._right else None,
        }

    def print_tree(self, level=0, prefix="Root: "):
        print(" " * (level * 4) + prefix + f"{self._value} ({self._color})")
        self._print_child(self._left, level, "L--> ")
        self._print_child(self._right, level, "R--> ")