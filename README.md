# Software-Projekt

## Router

The `app.py` file serves as the main entry point for handling requests in the Flask application. It defines the available endpoints, processes incoming data, and returns a response.

Each route requires the following JSON input:
- The **student graph** (the submitted solution, **mandatory**).
- Either the **graph** (initial state) or the **input values** (elements to be added or removed)—or **both**.

Inside the route's function, the task is programmatically solved using the **GraphTreeNode** or **RedBlackGraphTreeNode** classes. The student's submission is then **evaluated** against the expected solution, and feedback with an appropriate score is returned.

## Classes

These classes provide the foundation for handling graphs and evaluating student solutions.

### **GraphTreeNode**
A basic binary tree node with:
- A **value** (cannot be `None`).
- **Left and right children** (must be `GraphTreeNode` or `None`).
- **Getter and setter methods** for the value and child nodes.
- **Serialization and Deserialization**:
  - `to_json()`: Converts the tree into a JSON-compatible dictionary.
  - `from_json(data)`: Creates a tree structure from JSON input, ensuring no `color` attribute is present.
- **Printing Functionality**:
  - `print_tree()`: Outputs a formatted representation of the tree structure.

### **RedBlackGraphTreeNode** (inherits from `GraphTreeNode`)
Extends `GraphTreeNode` with:
- An additional **color** attribute (`red` or `black`).
- **Setter and getter methods** for the color.
- **Overridden serialization and deserialization**:
  - `to_json()`: Converts the tree to a JSON structure, including the `color` attribute.
  - `from_json(data)`: Ensures every node in the JSON input includes a `color` attribute.
- **Printing Functionality**:
  - `print_tree()`: Prints the tree with colors indicated in the output.

## JSON Handling in Routes

In `app.py`, the `/fix-tree` endpoint now utilizes these JSON functions:
- Parses the **graph** from JSON using `GraphTreeNode.from_json()`.
- Prints the parsed tree using `print_tree()`.
- Serializes the tree back to JSON using `to_json()` before returning the response.

### Example JSON request (GraphTreeNode):
```json
{
  "graph": {
    "value": 10,
    "left": {
      "value": 5
    },
    "right": {
      "value": 15
    }
  },
  "input": null,
  "student_graph": null
}
```

### Example JSON request (RedBlackGraphTreeNode):
```json
{
  "graph": {
    "value": 10,
    "color": "black",
    "left": {
      "value": 5,
      "color": "red"
    },
    "right": {
      "value": 15,
      "color": "red"
    }
  },
  "input": null,
  "student_graph": null
}
```