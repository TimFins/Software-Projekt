from flask import Flask, jsonify, request

from Classes.GraphTreeNode import GraphTreeNode
from Classes.RedBlackGraphTreeNode import RedBlackGraphTreeNode

app = Flask(__name__)

@app.route("/fix-tree", methods=["POST"])
def fix_tree():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    # get the graphs data
    graphJsonData = data.get("graph")
    studentGraphJsonData = data.get("student_graph")

    # parse the graphs into the structure based on the task (rb-tree or bin-search-tree)
    graph = GraphTreeNode.from_json(graphJsonData)
    # graph = RedBlackGraphTreeNode.from_json(graphJsonData)

    studentGraph = GraphTreeNode.from_json(studentGraphJsonData)
    # studentGraph = RedBlackGraphTreeNode.from_json(studentGraphJsonData)

    # print the received graph to the log if existing
    if graph:
        graph.print_tree()

    if studentGraph:
        studentGraph.print_tree()

    # get the values to be added or removed
    input = data.get("input")

    # Solve the task
    # Compare the solution with the student graph
    # Calculate the points and write a feedback

    return jsonify({"points": 100, "feedback": "Well done!", "graph": graph.to_json() if graph else None})

if __name__ == '__main__':
    app.run()
