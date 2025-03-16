class GraphTreeNode:
    def __init__(self, value, right_child=None, left_child=None):
        if value is None:
            raise ValueError("Value cannot be None")
        self._value = value
        self._right = right_child
        self._left = left_child

    def get_value(self):
        return self._value

    def get_left_child(self):
        return self._left

    def get_right_child(self):
        return self._right

    def set_value(self, value):
        if value is None:
            raise ValueError("Value cannot be None")
        self._value = value

    def set_left_child(self, node):
        if isinstance(node, GraphTreeNode) or node is None:
            self._left = node
        else:
            raise TypeError("Left child must be a GraphTreeNode or None")

    def set_right_child(self, node):
        if isinstance(node, GraphTreeNode) or node is None:
            self._right = node
        else:
            raise TypeError("Right child must be a GraphTreeNode or None")

    @classmethod
    def from_json(cls, data):
        if data is None:
            return None

        if not isinstance(data, dict) or "value" not in data:
            raise ValueError("Invalid JSON format: Each node must have a 'value' key")

        node = cls._create_node_from_json(data)

        if "left" in data and data["left"] is not None:
            node.set_left_child(cls.from_json(data["left"]))

        if "right" in data and data["right"] is not None:
            node.set_right_child(cls.from_json(data["right"]))

        return node

    @classmethod
    def _create_node_from_json(cls, data):
        if "color" in data:
            raise ValueError("GraphTreeNode does not accept a 'color' attribute")
        return cls(data["value"])

    def to_json(self):
        return {
            "value": self._value,
            "left": self._left.to_json() if self._left else None,
            "right": self._right.to_json() if self._right else None,
        }

    def _print_child(self, child, level, prefix):
        if child:
            child.print_tree(level + 1, prefix)
        else:
            print(" " * ((level + 1) * 4) + f"{prefix} null")

    def print_tree(self, level=0, prefix="Root: "):
        print(" " * (level * 4) + prefix + str(self._value))
        self._print_child(self._left, level, "L--> ")
        self._print_child(self._right, level, "R--> ")
