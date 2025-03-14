from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is the service evaluating and grading graphs.'


@app.route("/fix-tree", methods=["POST"])
def fix_tree():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    graph = data.get("graph")

    # Evaluating the graph

    return jsonify({"points": 100, "feedback": "Well done!"})

if __name__ == '__main__':
    app.run()
