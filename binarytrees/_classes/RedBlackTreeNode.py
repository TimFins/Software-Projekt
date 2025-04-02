from __future__ import annotations
from binarytrees._classes.BinaryTreeNode import BinaryTreeNode
from binarytrees._enums.RedBlackTreeColor import RedBlackTreeColor, convert_color_enum_to_string
from binarytrees._visualization.visualize_binary_tree import generate_binary_tree_image


class RedBlackTreeNode(BinaryTreeNode):
    """Class representing a node in a red-black tree.
    """
    def __init__(self, value: int, color: str = RedBlackTreeColor.RED, left_child: RedBlackTreeNode | None = None, right_child: RedBlackTreeNode | None = None, parent: RedBlackTreeNode | None = None):
        super().__init__(value, left_child, right_child, parent)
        self.set_color(color)

    def __repr__(self) -> str:
        color = convert_color_enum_to_string(self.get_color())
        return f"RedBlackTreeNode[{str(self.get_value())}, {color}]"

    def get_color(self) -> str | RedBlackTreeColor:
        return self._color

    def set_color(self, color: str | RedBlackTreeColor):
        if isinstance(color, str):
            try:
                color = RedBlackTreeColor(color)
            except ValueError:
                raise ValueError(
                    f"Invalid color '{color}'. Must be 'red' or 'black'.")
        if not isinstance(color, RedBlackTreeColor):
            raise TypeError(
                "Color must be an instance of RedBlackTreeColor Enum.")
        self._color = color

    def to_dict(self) -> dict[str, any]:
        return {
            "value": self._value,
            "color": self._color.value,
            "left": self._left.to_dict() if self._left else None,
            "right": self._right.to_dict() if self._right else None,
        }

    def print_tree(self, level: int = 0, prefix: str = "Root: "):
        print(" " * (level * 4) + prefix + f"{self._value} ({self._color})")
        self._print_child(self._left, level, "L--> ")
        self._print_child(self._right, level, "R--> ")
    
    def generate_tree_image(self) -> str:
        """Returns a Base64 encoded string containing the PNG image of the tree.
        """
        return generate_binary_tree_image(self, show_nil_nodes=True)

    def deep_copy(self) -> RedBlackTreeNode:
        """Creates and returns a hard copy of the node and all its subnodes.
        The copy can then be modified without changing the original.
        """
        node_copy = RedBlackTreeNode._from_binary_tree_node(
            super().deep_copy(), self.get_color())
        node_copy.set_color(self.get_color())
        return node_copy


    @classmethod
    def from_dict(cls, data: dict[str, any]) -> RedBlackTreeNode | None:
        return super().from_dict(data)

    @classmethod
    def _create_node_from_dict(cls, data: dict[str, any]) -> RedBlackTreeNode:
        if "color" not in data:
            raise ValueError(
                "Invalid JSON format: RedBlackTreeNode requires a 'color' key")
        return cls(data["value"], data["color"])

    @classmethod
    def _from_binary_tree_node(cls, binary_tree_node: BinaryTreeNode, color: str | RedBlackTreeColor = RedBlackTreeColor.BLACK):
        return cls(binary_tree_node.get_value(), color, binary_tree_node.get_left_child(), binary_tree_node.get_right_child(), binary_tree_node.get_parent())
