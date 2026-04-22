from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder="../frontend", static_url_path="")

@app.route("/")
def serve_frontend():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/api/hello")
def hello():
    return jsonify({"message": "hello"})
