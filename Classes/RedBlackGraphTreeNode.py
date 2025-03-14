from Classes.GraphTreeNode import GraphTreeNode


class RedBlackTreeNode(GraphTreeNode):
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
        return f"RedBlackTreeNode(value={self._value}, color={self._color})"