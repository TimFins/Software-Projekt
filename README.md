# Software-Projekt

## Prerequisites
### Software
One requires the programming language [Python](https://www.python.org/downloads/) and the package manager [pip](https://pip.pypa.io/en/stable/installation/).

As long as it is one of the relatively newer ones, the Python version should not really matter. This project was created with Python version 3.11.

### Install packages
This project requires the following Python packages:
- Flask (for running the HTTP server)
- graphviz (for generating PNG images of graphs)
- Pillow (for opening generated PNG images in file viewer)

The dependencies and exact versions are present in `requirements.txt`
One can install them directly using pip:
> pip install -r requirements.txt

## Usage
The file `example_usage.py` can just be run like a regular file.

### Start server
To start the HTTP server run the following:
> flask run

If the flask command cannot be located correctly, then you can also try:
> python -m flask run

Upon success, a HTTP server starts on localhost. You can terminate it using CTRL+C in the terminal.

Since flask usually takes localhost port 5000, you will probably find your HTTP server there. Alternatively, look for the adress in the terminal output. Usually it will look like this:
> * Running on http://127.0.0.1:5000

### Send request to server
If the server runs you can send a request to the given server by e.g., using command line tools like CURL or other API tools like Postman.
You will have to perform a post request on the endpoint and pass the contents as a JSON body.

#### Example body:
You can just use this JSON body as an example:
```json
{"existing_tree":{"value":10,"left":{"value":5,"left":{"value":6,"left":null,"right":null},"right":null},"right":{"value":15,"left":null,"right":null}},"values":[8],"student_tree":{"value":10,"left":{"value":5,"left":{"value":6,"left":null,"right":null},"right":{"value":8,"left":null,"right":null}},"right":{"value":15,"left":null,"right":null}}}
```

#### Example request on Windows
Assuming Flask uses the default port 5000, you can use this command in Windows Powershell to test the HTTP server.
```sh
Invoke-WebRequest -Uri "http://127.0.0.1:5000/example-route" -ContentType "application/json" -Method POST -Body '{"existing_tree":{"value":10,"left":{"value":5,"left":{"value":6,"left":null,"right":null},"right":null},"right":{"value":15,"left":null,"right":null}},"values":[8],"student_tree":{"value":10,"left":{"value":5,"left":{"value":6,"left":null,"right":null},"right":{"value":8,"left":null,"right":null}},"right":{"value":15,"left":null,"right":null}}}'
```

#### Other example request?

## HTTP Routing

The `app.py` file serves as the main entry point for handling requests in the Flask application. It defines the available endpoints, processes incoming data, and returns a response. You should implement your endpoints as HTTP POST endpoints.

Each route requires the following JSON input:
- The **student_tree** (the submitted solution, **mandatory**).
- Depending on task the **existing_tree** (initial state) and/or the **values** (elements to be added or removed, etc.) or **both** or **neither**.

Inside the route's function, the task is programmatically solved using the **BinaryTreeNode** or **RedBlackTreeNode** classes. The student's submission is then **evaluated** against the expected solution, and feedback with an appropriate score is returned.

## Classes

These classes provide the foundation for handling trees and evaluating student solutions.
They offer useful methods.

### Most relevant attributes and methods of BinaryTreeNode class

| Method/Attribute                   | Datatype(s)                                        | Notes                                                                                                                                                        |
| ---------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **value** _(setter, getter)_       | `int`                                              | Value of the node.                                                                                                                                           |
| **left_child** _(setter, getter)_  | `BinaryTreeNode` or `None`                         | Left child of the node.                                                                                                                                      |
| **right_child** _(setter, getter)_ | `BinaryTreeNode` or `None`                         | Right child of the node.                                                                                                                                     |
| **parent** _(setter, getter)_      | `BinaryTreeNode` or `None`                         | Parent of the node.                                                                                                                                          |
| **to_dict()**                      | returns `dict[str, any]`                           | Converts node and subtrees to dictionary, just like the one in the input.                                                                                    |
| **print_tree()**                   |                                                    | Prints formatted structure of node and subtrees to STDOUT.                                                                                                   |
| **generate_tree_image()**          | returns `str`                                      | Generate a base 64 encoded string containing the tree as PNG, which can e.g., be written to a file. The idea is, that one can use this method for debugging. |
| **display_tree_image()**           |                                                    | Generates an image of the tree and displays it in an image viewer. The idea is, that one can use this method for debugging.                                  |
| **hard_copy()**                    | returns `BinaryTreeNode`                           | Creates a deep copy of the node and subtrees. The copy can be modified without changing the original.                                                        |
| BinaryTreeNode.**from_dict()**     | accepts `dict[str, any]`, returns `BinaryTreeNode` | Class method, which takes a dictionary as input and converts it to a `BinaryTreeNode` with all its subtrees.                                                 |


### Most relevant attributes and methods of RedBlackTreeNode class

| Method/Attribute                   | Datatype(s)                                          | Notes                                                                                                                                                        |
| ---------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **value** _(setter, getter)_       | `int`                                                | Value of the node.                                                                                                                                           |
| **color** _(setter, getter)_       | `RedBlackTreeColor` or `str`                         | Color of the node. Either 'RED' or 'BLACK'. Enum RedBlackTreeColor is used to manage colors.                                                                 |
| **left_child** _(setter, getter)_  | `RedBlackTreeNode` or `None`                         | Left child of the node.                                                                                                                                      |
| **right_child** _(setter, getter)_ | `RedBlackTreeNode` or `None`                         | Right child of the node.                                                                                                                                     |
| **parent** _(setter, getter)_      | `RedBlackTreeNode` or `None`                         | Parent of the node.                                                                                                                                          |
| **to_dict()**                      | returns `dict[str, any]`                             | Converts node and subtrees to dictionary, just like the one in the input.                                                                                    |
| **print_tree()**                   |                                                      | Prints formatted structure of node and subtrees to STDOUT.                                                                                                   |
| **generate_tree_image()**          | returns `str`                                        | Generate a base 64 encoded string containing the tree as PNG, which can e.g., be written to a file. The idea is, that one can use this method for debugging. |
| **display_tree_image()**           |                                                      | Generates an image of the tree and displays it in an image viewer. The idea is, that one can use this method for debugging.                                  |
| **hard_copy()**                    | returns `RedBlackTreeNode`                           | Creates a deep copy of the node and subtrees. The copy can be modified without changing the original.                                                        |
| RedBlackTreeNode.**from_dict()**   | accepts `dict[str, any]`, returns `RedBlackTreeNode` | Class method, which takes a dictionary as input and converts it to a `RedBlackTreeNode` with all its subtrees.                                               |

### Example usage
The most relevant functions are showcased in the file `example_usage`. There one can get familiar with the functionality.

## JSON Handling in Routes

As an example, the endpoint `/example-route` in `app.py` was defined to showcase basic functionality. This route does the following:
- Accepts input
- Parses the **trees** from JSON using `BinaryTreeNode.from_dict()`.
- Does a trivial grading as example.
- Returns the score and feedback.

### Evaluation functions
Evaluation functions should ideally be stored in the `evaluation` directory. Create a new file containing your evaluations. Import it in `evaluation/__init__.py` and then import it in your route. 

### Example JSON request (Inserting values into a binary search tree):
This could be an example input where the task is to insert the values in the existing tree.
In this example the student has correctly created a new node with the value 8 and placed it at the correct location.
```json
{
     "existing_tree":{
          "value":10,
          "left":{
                "value":5,
                "left":{
                     "value":6,
                     "left":null,
                     "right":null
                },
                "right":null
          },
          "right":{
                "value":15,
                "left":null,
                "right":null
          }
     },
     "values": [8],
     "student_tree":{
          "value":10,
          "left":{
                "value":5,
                "left":{
                     "value":6,
                     "left":null,
                     "right":null
                },
                "right":{
                     "value":8,
                     "left":null,
                     "right":null
                }
          },
          "right":{
                "value":15,
                "left":null,
                "right":null
          }
     }
}
```

### Example JSON request (Construct binary search tree from values):
This could be an example input where the task is create a binary search tree from scratch with the given input `values`.

```json
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
```

### Example JSON request (Fix a red-black tree):
This could be an example input where the task is fix the provided red-black tree by restoring red-black properties and performing rebalancing.
Since the job is to only fix the tree instead of adding or removing nodes, the `values` field is null.
```json
{
    "existing_tree": {
        "value": 10,
        "color": "BLACK",
        "left": {
            "value": 5,
            "color": "RED",
            "left": null,
            "right": null
        },
        "right": {
            "value": 15,
            "color": "BLACK",
            "left": null,
            "right": null
        }
    },
    "values": null,
    "student_tree": {
        "value": 10,
        "color": "RED",
        "left": {
            "value": 5,
            "color": "RED",
            "left": null,
            "right": null
        },
        "right": {
            "value": 15,
            "color": "RED",
            "left": null,
            "right": null
        }
    }
}
```