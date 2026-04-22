import os
from flask import Flask, jsonify, send_file

app = Flask(__name__)

@app.route("/")
def serve_frontend():
    base_dir = os.path.dirname(__file__)
    path = os.path.abspath(os.path.join(base_dir, "..", "frontend", "index.html"))
    return send_file(path)

@app.route("/api/hello")
def hello():
    return jsonify({"message": "hello"})
@app.route("/debug")
def debug():
    import os
    base_dir = os.path.dirname(__file__)
    path = os.path.abspath(os.path.join(base_dir, "..", "frontend", "index.html"))
    return {
        "base_dir": base_dir,
        "calculated_path": path,
        "exists": os.path.exists(path)
    }
