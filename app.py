import json
import os
import time

from flask import Flask, jsonify, render_template, request

from informed import a_star, greedy
from uninformed import bfs, dfs, ids, ucs

app = Flask(__name__)

with open("map_data.json", encoding="utf-8") as file:
    MAP_DATA = json.load(file)

GRAPH = MAP_DATA["graph"]
LOCATIONS = MAP_DATA["locations"]

UNINFORMED = {"bfs": bfs, "dfs": dfs, "ucs": ucs, "ids": ids}
INFORMED = {"greedy": greedy, "astar": a_star}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/map")
def get_map():
    return jsonify(MAP_DATA)


@app.route("/api/search", methods=["POST"])
def search():
    data = request.get_json() or {}
    start = data.get("start")
    goal = data.get("goal")
    algorithm = data.get("algorithm")

    if start not in GRAPH or goal not in GRAPH:
        return jsonify({"error": "Please pick a valid start and destination."}), 400

    started_at = time.perf_counter()

    if algorithm in UNINFORMED:
        result = UNINFORMED[algorithm](GRAPH, start, goal)
    elif algorithm in INFORMED:
        result = INFORMED[algorithm](GRAPH, LOCATIONS, start, goal)
    else:
        return jsonify({"error": f"Unknown algorithm: {algorithm}"}), 400

    result["time_ms"] = round((time.perf_counter() - started_at) * 1000, 3)
    return jsonify(result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
