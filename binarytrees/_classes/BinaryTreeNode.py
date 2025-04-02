from __future__ import annotations
from binarytrees._visualization.visualize_binary_tree import generate_binary_tree_image, display_binary_tree_image


class BinaryTreeNode:
    """Class representing a node in a binary tree.
    """
    def __init__(self, value: int, left_child: BinaryTreeNode | None = None, right_child: BinaryTreeNode | None = None, parent: BinaryTreeNode | None = None):
        self.set_value(value)
        self._left = left_child
        self._right = right_child
        self._parent = parent

    def __repr__(self) -> str:
        return f"BinaryTreeNode[{str(self.get_value())}]"

    def get_value(self) -> int:
        return self._value

    def set_value(self, value: int):
        if value is None:
            raise ValueError("Value cannot be None")
        if not isinstance(value, int):
            raise TypeError("Value must be a numeric type int")
        self._value = value

    def get_left_child(self) -> BinaryTreeNode | None:
        return self._left

    def set_left_child(self, node: BinaryTreeNode | None):
        if isinstance(node, BinaryTreeNode) or node is None:
            self._left = node
        else:
            raise TypeError("Left child must be a BinaryTreeNode/RedBlackTreeNode or None")

    def get_right_child(self) -> BinaryTreeNode | None:
        return self._right

    def set_right_child(self, node: BinaryTreeNode | None):
        if isinstance(node, BinaryTreeNode) or node is None:
            self._right = node
        else:
            raise TypeError("Right child must be a BinaryTreeNode/RedBlackTreeNode or None")

    def get_parent(self) -> BinaryTreeNode | None:
        return self._parent

    def set_parent(self, node: BinaryTreeNode | None):
        if isinstance(node, BinaryTreeNode) or node is None:
            self._parent = node
        else:
            raise TypeError("Parent must be a BinaryTreeNode/RedBlackTreeNode or None")

    def to_dict(self) -> dict[str, any]:
        return {
            "value": self._value,
            "left": self._left.to_dict() if self._left else None,
            "right": self._right.to_dict() if self._right else None,
        }

    def _print_child(self, child: BinaryTreeNode | None, level: int, prefix: str):
        if child:
            child.print_tree(level + 1, prefix)
        else:
            print(" " * ((level + 1) * 4) + f"{prefix} null")

    def print_tree(self, level: int = 0, prefix: str = "Root: "):
        print(" " * (level * 4) + prefix + str(self._value))
        self._print_child(self._left, level, "L--> ")
        self._print_child(self._right, level, "R--> ")

    def generate_tree_image(self) -> str:
        """Returns a Base64 encoded string containing the PNG image of the tree.
        """
        return generate_binary_tree_image(self, show_nil_nodes=False)

    def display_tree_image(self):
        """Display the image of the tree in a file viewer.
        """
        display_binary_tree_image(self.generate_tree_image())

    def deep_copy(self) -> BinaryTreeNode:
        """Creates and returns a hard copy of the node and all its subnodes.
        The copy can then be modified without changing the original.
        """
        left_child = self.get_left_child().deep_copy() if self.get_left_child() else None
        right_child = self.get_right_child().deep_copy() if self.get_right_child() else None
        node_copy = BinaryTreeNode(self.get_value(), left_child, right_child)
        if left_child:
            left_child.set_parent(node_copy)
        if right_child:
            right_child.set_parent(node_copy)
        return node_copy

    @classmethod
    def from_dict(cls, data: dict[str, any]) -> BinaryTreeNode | None:
        if data is None:
            return None
        if not isinstance(data, dict) or "value" not in data.keys():
            raise ValueError(
                "Invalid JSON format: Each node must have a 'value' key")
        node = cls._create_node_from_dict(data)
        if "left" in data and data["left"] is not None:
            node.set_left_child(cls.from_dict(data["left"]))
            node.get_left_child().set_parent(node)
        if "right" in data and data["right"] is not None:
            node.set_right_child(cls.from_dict(data["right"]))
            node.get_right_child().set_parent(node)
        return node

    @classmethod
    def _create_node_from_dict(cls, data: dict[str, any]) -> BinaryTreeNode:
        if "color" in data:
            raise ValueError(
                "BinaryTreeNode does not accept a 'color' attribute")
        return cls(data["value"])
