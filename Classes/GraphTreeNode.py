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