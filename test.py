from binarytrees import BinaryTreeNode, RedBlackTreeNode
import json

tree_json = """
{
    "existing_tree": null,
    "values": [2, 3, 1, 4],
    "student_tree": {
        "value": 2,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 3,
            "left": null,
            "right": {
                "value": 4,
                "left": null,
                "right": null
            }
        }
    }
}
"""

# Convert JSON to Python dictionary
json_as_dict = json.loads(tree_json)
student_tree_dict = json_as_dict["student_tree"]

# Create a binary tree object from tree dictonary
root = BinaryTreeNode.from_dict(student_tree_dict)
root = RedBlackTreeNode.from_binary_tree_node(root)

print(root.inorder_traverse())

root.display_tree_image()