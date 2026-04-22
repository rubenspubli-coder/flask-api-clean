from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "ok"

@app.route("/api/hello")
def hello():
    return jsonify({"message": "hello"})
