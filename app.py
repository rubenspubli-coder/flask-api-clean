import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def debug_root():
    return {
        "cwd": os.getcwd(),
        "files_root": os.listdir("."),
        "files_frontend": os.listdir("frontend") if os.path.exists("frontend") else "no frontend folder"
    }

@app.route("/api/hello")
def hello():
    return jsonify({"message": "hello"})
