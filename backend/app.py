import os
from flask import Flask, jsonify, send_file

app = Flask(__name__)

# Caminho absoluto seguro até a raiz do projeto (/app no Railway)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

@app.route("/")
def serve_frontend():
    path = os.path.join(BASE_DIR, "frontend", "index.html")
    
    if not os.path.exists(path):
        return {
            "error": "index.html não encontrado",
            "path_procurado": path,
            "arquivos_na_raiz": os.listdir(BASE_DIR)
        }, 500

    return send_file(path)

@app.route("/api/hello")
def hello():
    return jsonify({"message": "hello"})

@app.route("/debug")
def debug():
    path = os.path.join(BASE_DIR, "frontend", "index.html")
    return {
        "BASE_DIR": BASE_DIR,
        "path": path,
        "exists": os.path.exists(path),
        "root_files": os.listdir(BASE_DIR),
        "frontend_files": os.listdir(os.path.join(BASE_DIR, "frontend")) if os.path.exists(os.path.join(BASE_DIR, "frontend")) else "frontend não existe"
    }
