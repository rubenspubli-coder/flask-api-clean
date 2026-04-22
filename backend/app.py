import os
from flask import Flask, jsonify, send_file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_PATH = os.path.join(BASE_DIR, "..", "frontend", "index.html")

app = Flask(__name__)

@app.route("/")
def serve_frontend():
    return send_file(FRONTEND_PATH)

@app.route("/api/hello")
def hello():
    return jsonify({"message": "hello"})
