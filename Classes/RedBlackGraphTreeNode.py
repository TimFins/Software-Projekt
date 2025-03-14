from Classes.GraphTreeNode import GraphTreeNode


class RedBlackGraphTreeNode(GraphTreeNode):
    def __init__(self, value, color="red", right_child=None, left_child=None):
        super().__init__(value, right_child, left_child)
        self.set_color(color)

    def get_color(self):
        return self._color

    def set_color(self, color):
        if color not in {"red", "black"}:
            raise ValueError("Color must be either 'red' or 'black'")
        self._color = color

    def __repr__(self):
        return f"RedBlackGraphTreeNode(value={self._value}, color={self._color})"

    @classmethod
    def _create_node_from_json(cls, data):
        if "color" not in data:
            raise ValueError("Invalid JSON format: RedBlackGraphTreeNode requires a 'color' key")

        return cls(data["value"], data["color"])

    def to_json(self):
        data = super().to_json()
        data["color"] = self._color
        return data

    def print_tree(self, level=0, prefix="Root: "):
        print(" " * (level * 4) + prefix + f"{self._value} ({self._color})")

        if self._left:
            self._left.print_tree(level + 1, "L--> ")
        if self._right:
            self._right.print_tree(level + 1, "R--> ")