from flask import Flask, jsonify, send_file

app = Flask(__name__)

@app.route("/")
def serve_frontend():
    return send_file("frontend/index.html")

@app.route("/api/hello")
def hello():
    return jsonify({"message": "hello"})
