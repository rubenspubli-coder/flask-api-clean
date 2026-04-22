import os
from flask import Flask, jsonify, send_file

app = Flask(__name__)

@app.route("/")
def serve_frontend():
    path = os.path.abspath(os.path.join(os.getcwd(), "..", "frontend", "index.html"))
    return send_file(path)

@app.route("/api/hello")
def hello():
    return jsonify({"message": "hello"})
